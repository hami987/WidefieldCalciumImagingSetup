from pycromanager import Core
import serial, time, os
from datetime import datetime
import numpy as np
import tifffile

def burst_acquisition(save_dir, num_images=50,
                      exposure_ms=10,
                      roi=None  # e.g. roi = (x, y, width, height)
                     ):
    core = Core()
    core.set_property('Core', 'AutoShutter', '0')

    # — 2 GB buffer for high‑speed burst —
    core.set_circular_buffer_memory_footprint(2048)
    core.initialize_circular_buffer()

    # — exposure & ROI —
    core.set_exposure(exposure_ms)
    if roi:
        x, y, w, h = roi
        core.set_roi(x, y, w, h)

    # — warm‑up to stabilize fps —
    warmup = 200
    core.start_sequence_acquisition(warmup, 0, True)
    while core.get_remaining_image_count() < warmup:
        time.sleep(0.001)
    for _ in range(warmup):
        try:
            core.pop_next_tagged_image()
        except:
            pass
    core.stop_sequence_acquisition()

    # — output paths —
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir = os.path.join(save_dir, f"Acq_{ts}")
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "stack.tif")

    # — trigger motor →
    time.sleep(3)
    with serial.Serial('COM5', 9600) as arduino:
        time.sleep(10)
        arduino.flushInput(); arduino.flushOutput()
        

        # — start burst →
        core.start_sequence_acquisition(num_images, 0, True)

        # — wait for first frame —
        while core.get_remaining_image_count() == 0:
            time.sleep(0.001)

        images = []
        t0 = time.time()
        for i in range(num_images):
            # ← blocking pop
            tagged = core.pop_next_tagged_image()

            pix = tagged.pix
            w = tagged.tags['Width']; h = tagged.tags['Height']
            dtype = np.uint16 if tagged.tags.get('PixelType','')=='GRAY16' else np.uint8
            img = np.frombuffer(pix, dtype=dtype).reshape((h, w))
            images.append(img)
            
       

            if (i % 10 == 0) or (i == num_images - 1):
                fps = (i + 1) / (time.time() - t0)
                print(f"{i+1}/{num_images} @ {fps:.1f} fps")
           
            arduino.write(b'l')

        core.stop_sequence_acquisition()

    # — save stack —
    stack = np.stack(images, axis=0)
    tifffile.imwrite(out_file,
                     stack,
                     imagej=True,
                     metadata={'mode':'composite'})
    size_mb = os.path.getsize(out_file) / (1024**2)
    print(f"Saved {len(images)} frames to {out_file} ({size_mb:.1f} MB)")

if __name__ == "__main__":
    save_path = r"C:\Temp\Rotations"
    NUM    = 1000         # total frames
    EXP_MS = 20          # ms (≤25 ms for ~40 fps)
    ROI    = None        # or (0,0,1024,1024)
    burst_acquisition(save_path, NUM, EXP_MS, ROI)
    print("Done")


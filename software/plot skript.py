#%%
import pandas as pd
import matplotlib.pyplot as plt

# Pfad zur CSV-Datei (aus ImageJ)
csv_file = "C:/Users/Ventral Pol/Desktop/Results.csv" 
df = pd.read_csv(csv_file)

# Alle Spaltennamen, die mit "Mean" beginnen (z.B. "Mean1", "Mean2", ...)
mean_cols = [col for col in df.columns if col.startswith("Mean")]

# Frames, die als Pre-Stimulus-Baseline dienen (z. B. erste 50 Frames)
baseline_frames = 30

# Ergebnis-DataFrame: ΔF/F₀ für jede ROI
deltaF_over_F0 = pd.DataFrame()

# Berechnung pro ROI
for col in mean_cols:
    F = df[col]
    F0 = F[:baseline_frames].mean()  # Mittelwert der ersten 150 Frames
    
    deltaF_over_F0[col] = (F - F0) / F0


# Optional: Plotte alle ROIs
plt.figure(figsize=(10, 6))
for col in deltaF_over_F0.columns:
    plt.plot(deltaF_over_F0[col], label=col)
plt.axvline(x=baseline_frames, color='gray', linestyle='--', label='Rotation onset')
plt.xlabel("Frame")
plt.ylabel("ΔF/F₀")
plt.title("GCaMP ΔF/F₀ traces per ROI")
plt.legend()
plt.tight_layout()
plt.show()


# %%

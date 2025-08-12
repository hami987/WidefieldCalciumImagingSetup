# Calcium Imaging Setup

An open-source hardware and software platform for calcium imaging experiments in neuroscience.

This repository contains:
- **Hardware designs** — 3D printed parts, CAD source files, electronics schematics, and BOM.
- **Firmware** — Arduino/microcontroller code for device control.
- **Software** — Python and MATLAB scripts for data acquisition and analysis.
- **Documentation** — Step-by-step assembly, setup, and troubleshooting guides.
- **Example Data** — Small datasets for testing the setup.

![Setup Photo](docs/images/setup_photo.jpg)

---

## 📦 Repository Structure

calcium-imaging-setup/
├── docs/ # Full documentation and guides
├── hardware/ # CAD, STL, and electronics files
├── firmware/ # Arduino/microcontroller code
├── software/ # Acquisition & analysis scripts
├── data_examples/ # Test datasets
├── LICENSE # Software license
├── LICENSE-HARDWARE # Hardware design license
├── LICENSE-DOCS # Documentation license
└── CHANGELOG.md # Project history

yaml
Copy
Edit

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/USERNAME/calcium-imaging-setup.git
cd calcium-imaging-setup
2. Set up hardware
Follow the instructions in Hardware Setup.

3. Install software
bash
Copy
Edit
pip install -r software/python/requirements.txt
4. Run acquisition example
bash
Copy
Edit
python software/python/acquisition_script.py
📖 Documentation
Full documentation is in the docs/ folder:

Overview

Hardware Setup

Software Setup

Usage Guide

Troubleshooting

📜 Licensing
Code: MIT License

Hardware: CERN Open Hardware License v2

Documentation: CC BY-SA 4.0

🤝 Contributing
Pull requests, bug reports, and suggestions are welcome.
Please see CONTRIBUTING.md for details.

🧪 Example Data
A small set of example videos and CSV files is available in data_examples/ for testing the acquisition and analysis pipeline.

📅 Changelog
All changes are tracked in CHANGELOG.md.

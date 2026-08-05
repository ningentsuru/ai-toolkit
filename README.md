# All-in-One AI Media Toolkit (Monorepo)

A scalable, professional monorepo collection of standalone AI tools and lightweight utilities, built using the modern `src` layout structure.

## 📁 Repository Structure

```text
python-random/
┣ assets/
┃ ┣ input/                      # Drop your raw source files here
┃ ┗ output/                     # Processed output directory
┣ src/
┃ ┣ ai_media/                  # 🤖 Domain 1: AI Media Engine
┃ ┃ ┣ __init__.py               # Shared GPU auto-detection logic
┃ ┃ ┣ bg_remover.py            # AI Background Removal Module
┃ ┃ ┣ transcriber.py           # [WIP] Future Whisper Audio Transcription
┃ ┃ ┗ upscaler.py              # [WIP] Future Real-ESRGAN Image Upscaler
┃ ┃
┃ ┣ utility_tools/              # 🧮 Domain 2: Classic / Random Utilities
┃ ┃ ┣ __init__.py
┃ ┃ ┗ number_cruncher.py       # Core Computation Module
┃ ┃
┃ ┗ cli/                       # 🎛️ Domain 3: Central Command Center
┃   ┣ __init__.py
┃   ┣ ai_cli.py                # Command parsing for AI tools
┃   ┣ main.py                  # Master entrypoint for terminal routing
┃   ┗ util_cli.py              # Command parsing for utility tools
┣ test/                         # Automated testing suits folder
┣ pyproject.toml                # Master project configuration setup
┗ README.md
```

---

## 🚀 Active Features

### 🖼️ Background Remover (`ai-toolkit bg-remover`)

- **GPU Acceleration**: Fully optimized to leverage NVIDIA CUDA & TensorRT pipelines natively on Windows.
- **Auto-Detection Setup**: Dynamically scans system installations at execution runtime to load CUDA/cuDNN DLL vectors automatically.
- **Batch Processing Suite**: Strips out backgrounds from entire folders of images seamlessly in a single pass.
- **Smart Memory Caching**: Reuses a single shared ONNX model session context to avoid system spin-up latency overheads.

### 🧮 Number Cruncher (`ai-toolkit calc`)

- Fast, lightweight numerical calculator processing core running locally on your CPU.

---

## 🛠️ Installation & Setup

### 1. Prerequisites (For GPU Acceleration)

To leverage maximum performance on your graphics card, ensure your system has the following native dependencies installed:

- [NVIDIA CUDA Toolkit (v12.x)](https://nvidia.com)
- [NVIDIA cuDNN (v9.x x86_64 Local Archive)](https://nvidia.com)

> 💡 **Tip:** Extract your cuDNN `.zip` contents and copy the inner payload folders (`bin`, `include`, `lib`) directly into your primary installation directory path at `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.5\` for instant system recognition.

### 2. Environment Installation

Clone the repository and install the monorepo package in editable development mode:

```bash
# Create and activate your virtual environment
python -m venv .venv
.venv\Scripts\activate

# Automatically download dependencies and link the global command
pip install -e .
```

---

## 💻 Usage Instructions

The toolkit uses a unified terminal controller router (`ai-toolkit`) to access individual internal sub-modules:

### Batch Background Removal

Place your raw image formats (`.jpg`, `.jpeg`, `.png`, `.webp`, `.bmp`) inside the `assets/input/` directory and execute:

```bash
ai-toolkit bg-remover --batch
```

### Custom Processing Target Paths

```bash
ai-toolkit bg-remover --batch --input-dir "path/to/raw/" --output-dir "path/to/results/"
```

### Single File Background Removal

```bash
ai-toolkit bg-remover -i assets/input/sample.jpg -o assets/output/result.png
```

---

## 🧑‍💻 Development

### Code Formatting

Ensure consistency across script branches using integrated format rules:

```bash
# Run styling linter checks
black src/
isort src/
```

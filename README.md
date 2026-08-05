# All-in-One AI Media Toolkit (Monorepo)

A scalable, professional monorepo collection of standalone AI tools and lightweight utilities, built using the modern `src` layout structure.

## 📁 Repository Structure

```text
ai-toolkit/
┣ assets/
┃ ┣ bg_remover/                 # ✂️ Background Remover Workspace
┃ ┃ ┣ input/                    # Drop source images for background removal here
┃ ┃ ┗ output/                   # Background-removed results
┃ ┣ upscale/                    # 📈 Upscaler Workspace
┃ ┃ ┣ input/                    # Drop blurry/low-res images here
┃ ┃ ┗ output/                   # Crisp 4x upscaled results
┣ src/
┃ ┣ ai_media/                   # 🤖 Domain 1: AI Media Engine
┃ ┃ ┣ __init__.py               # Shared GPU auto-detection logic
┃ ┃ ┣ bg_remover.py             # AI Background Removal Module
┃ ┃ ┣ transcriber.py            # [WIP] Future Whisper Audio Transcription
┃ ┃ ┗ upscaler.py               # AI 4x Super-Resolution Image Upscaler
┃ ┃
┃ ┣ utility_tools/              # 🧮 Domain 2: Classic / Random Utilities
┃ ┃ ┣ __init__.py
┃ ┃ ┗ number_cruncher.py        # Core Computation Module
┃ ┃
┃ ┗ cli/                        # 🎛️ Domain 3: Central Command Center
┃   ┣ __init__.py
┃   ┣ ai_cli.py                 # Command parsing for AI tools
┃   ┣ main.py                   # Master entrypoint for terminal routing
┃   ┗ util_cli.py               # Command parsing for utility tools
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

### 📈 Image Upscaler (`ai-toolkit upscale`)

- **Deep Learning Resolution Enhancement**: Reconstructs missing details using a pre-trained FSRCNN Neural Network.
- **4x Resolution Scaling**: Instantly multiplies your original image dimensions by 4x while eliminating pixelation and maintaining smooth gradients.
- **Local Offline Processing**: Automatically utilizes local caching directory checks to bypass external web access constraints.

### 🧮 Number Cruncher (`ai-toolkit calc`)

- Fast, lightweight numerical calculator processing core running locally on your CPU.

---

## 🛠️ Installation & Setup

### 1. Prerequisites (For GPU Acceleration)

To leverage maximum performance on your graphics card, ensure your system has the following native dependencies installed:

- [NVIDIA CUDA Toolkit (v12.x)](https://nvidia.com)
- [NVIDIA cuDNN (v9.x x86_64 Local Archive)](https://nvidia.com)

> 💡 **Tip:** Extract your cuDNN `.zip` contents and copy the inner payload folders (`bin`, `include`, `lib`) directly into your primary installation directory path at `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.5\` for instant system recognition.

### 2. Manual Model Setup (Upscaler)

To prevent network timeout blocks or firewall errors at runtime, download the upscaler model manually before invoking your first script trace:

1. Download the file **`FSRCNN_x4.pb`** from the [Official Repository Mirror](https://github.com/Saafke/FSRCNN_Tensorflow/blob/master/models/FSRCNN_x4.pb).
2. Open Windows File Explorer and navigate to: `%USERPROFILE%\.cache`
3. Create a folder named `ai-toolkit`, go inside it, and create another folder named `models`.
4. Paste the downloaded model file into that folder so its final location reads:
   `C:\Users\<YourUsername>\.cache\ai-toolkit\models\FSRCNN_x4.pb`

### 3. Environment Installation

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

Place your raw image formats inside the `assets/input/` directory and execute:

```bash
ai-toolkit bg-remover --batch
```

### 4x Image Upscaling

- **Single File Execution**:
  ```bash
  ai-toolkit upscale -i assets/input/sample.jpg
  ```
- **Folder Batch Processing**:
  ```bash
  ai-toolkit upscale --batch
  ```

### Lightweight Math Calculator

```bash
ai-toolkit calc add 15 25
```

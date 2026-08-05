import os
import glob
import onnxruntime as ort
from pathlib import Path
from PIL import Image
from rembg import remove, new_session


def _auto_load_nvidia_dlls():
    """Dynamically locates and loads standard Windows CUDA and cuDNN DLL paths."""
    if os.name != "nt":  # Only execute environment fixes on Windows machines
        return

    # 1. Scan and register the local CUDA installation
    cuda_base = r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA"
    if os.path.exists(cuda_base):
        # Finds paths matching pattern: ...\CUDA\v12.5\bin
        cuda_bins = glob.glob(os.path.join(cuda_base, "v*", "bin"))
        for bin_path in cuda_bins:
            os.add_dll_directory(bin_path)

    # 2. Scan and register the local cuDNN installation
    cudnn_base = r"C:\Program Files\NVIDIA\CUDNN"
    if os.path.exists(cudnn_base):
        # Checks if you integrated the correct standard architecture file setup
        # Searches deeply for any subfolder containing the key dependencies
        search_pattern = os.path.join(cudnn_base, "v*", "bin", "**", "*.dll")
        matched_dlls = glob.glob(search_pattern, recursive=True)

        # Extract unique directories containing valid cuDNN dll targets
        cudnn_dirs = {os.path.dirname(dll) for dll in matched_dlls}
        for dir_path in cudnn_dirs:
            # Skip invalid target frameworks like ARM64 if you are on x64
            if (
                "arm64" in dir_path.lower()
                and "arm" not in os.environ.get("PROCESSOR_ARCHITECTURE", "").lower()
            ):
                continue
            os.add_dll_directory(dir_path)

    # 3. Securely push initialization mappings onto ONNX Runtime state flags
    try:
        ort.preload_dlls()
    except AttributeError:
        pass


# Trigger environment resolution flags immediately during module initialization
_auto_load_nvidia_dlls()


def process_image(
    input_path: str, output_path: str, model: str = "u2net", session=None
):
    input_file = Path(input_path)
    if not input_file.exists():
        raise FileNotFoundError(f"Input file {input_path} not found")

    if session is None:
        providers = ["CUDAExecutionProvider", "CPUExecutionProvider"]
        session = new_session(model, providers=providers)

    with Image.open(input_file) as img:
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        output = remove(img, session=session, alpha_matting=True)

        output_path_obj = Path(output_path)
        output_path_obj.parent.mkdir(parents=True, exist_ok=True)
        output.save(output_path_obj)

    return output_path

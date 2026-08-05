import os
import urllib.request
from pathlib import Path
import cv2


def _ensure_model_exists() -> str:
    """Downloads the pre-trained FSRCNN 4x upscaler model if missing."""
    model_dir = Path(os.path.expanduser("~/.cache/ai-toolkit/models"))
    model_dir.mkdir(parents=True, exist_ok=True)

    model_path = model_dir / "FSRCNN_x4.pb"
    if not model_path.exists():
        print("📥 Downloading lightweight 4x Super-Resolution model...")
        url = "https://githubusercontent.com"
        urllib.request.urlretrieve(url, str(model_path))

    return str(model_path)


def upscale_image(input_path: str, output_path: str) -> str:
    """Upscales a low-resolution target image file 4x using deep learning."""
    input_file = Path(input_path)
    if not input_file.exists():
        raise FileNotFoundError(f"Input image target {input_path} missing.")

    # 1. Initialize OpenCV Super Resolution Engine Context
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    model_file_path = _ensure_model_exists()

    sr.readModel(model_file_path)
    sr.setModel("fsrcnn", 4)  # Configure model algorithm type and scale boundaries

    # 2. Process Image through deep learning layers
    img = cv2.imread(str(input_file))
    if img is None:
        raise ValueError(f"Failed to decode or parse target image matrix: {input_path}")

    upscaled_img = sr.upsample(img)

    # 3. Output back to filesystem path targets
    output_path_obj = Path(output_path)
    output_path_obj.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(output_path_obj), upscaled_img)

    return output_path

import argparse
from pathlib import Path

# 👈 REMOVED from rembg import new_session from top level
from ai_media.bg_remover import process_image


def register_ai_parser(subparsers):
    """Registers the bg-remover sub-command into the main CLI parser."""
    ai_parser = subparsers.add_parser("bg-remover", help="AI Background Removal Tools")

    ai_parser.add_argument("-i", "--input", type=str, help="Single input image path")
    ai_parser.add_argument("-o", "--output", type=str, help="Single output image path")
    ai_parser.add_argument(
        "--batch", action="store_true", help="Process all images in assets/input/"
    )
    ai_parser.add_argument(
        "--input-dir",
        type=str,
        default="assets/input",
        help="Input directory for batch mode",
    )
    ai_parser.add_argument(
        "--output-dir",
        type=str,
        default="assets/output",
        help="Output directory for batch mode",
    )


def handle_bg_remover(args):
    """Executes background removal based on parsed terminal arguments."""
    from rembg import new_session  # 👈 LAZY IMPORT: Only loads if bg-remover is called!

    # Pre-initialize the GPU session once before processing
    providers = ["CUDAExecutionProvider", "CPUExecutionProvider"]
    session = new_session("u2net", providers=providers)

    if args.batch:
        run_batch(args.input_dir, args.output_dir, session)
    elif args.input:
        output_path = args.output or "assets/output/result.png"
        try:
            process_image(args.input, output_path, session=session)
            print(f"✅ Success! Saved to {output_path}")
        except Exception as e:
            print(f"❌ Error: {e}")
    else:
        print("❌ Please specify an input file (-i) or use --batch mode.")
        print("   Example: ai-toolkit bg-remover --batch")


def run_batch(input_dir: str, output_dir: str, session):
    input_path = Path(input_dir)
    output_path = Path(output_dir)

    if not input_path.exists():
        print(f"❌ Error: Input directory '{input_dir}' not found.")
        return

    output_path.mkdir(parents=True, exist_ok=True)
    extensions = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

    files = [
        f
        for f in input_path.iterdir()
        if f.is_file() and f.suffix.lower() in extensions
    ]

    if not files:
        print(f"⚠️  No images found in '{input_dir}'.")
        return

    print(f"🚀 Found {len(files)} images. Starting batch processing...")

    for file in files:
        try:
            output_file = output_path / f"{file.stem}.png"
            print(f"⏳ Processing: {file.name} ...")
            process_image(str(file), str(output_file), session=session)
            print(f"   ✅ Saved: {output_file.name}")
        except Exception as e:
            print(f"   ❌ Failed {file.name}: {e}")

    print("🎉 Batch processing complete!")

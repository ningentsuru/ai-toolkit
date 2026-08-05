import argparse
from pathlib import Path
from ai_media.bg_remover import process_image


def register_ai_parser(subparsers):
    """Registers AI Media tools into the main command subparser array."""
    # 1. Background Removal Sub-command Menu
    ai_parser = subparsers.add_parser("bg-remover", help="AI Background Removal Tools")
    ai_parser.add_argument("-i", "--input", type=str, help="Single input image path")
    ai_parser.add_argument("-o", "--output", type=str, help="Single output image path")
    ai_parser.add_argument("--batch", action="store_true", help="Process all images")
    # 👇 UPDATED PATH
    ai_parser.add_argument(
        "--input-dir",
        type=str,
        default="assets/bg_remover/input",
        help="Input directory",
    )
    # 👇 UPDATED PATH
    ai_parser.add_argument(
        "--output-dir",
        type=str,
        default="assets/bg_remover/output",
        help="Output directory",
    )

    # 2. Upscaler Sub-command Menu Registration
    upscale_parser = subparsers.add_parser(
        "upscale", help="AI 4x Super-Resolution Image Upscaler"
    )
    upscale_parser.add_argument(
        "-i", "--input", type=str, help="Single target input image path"
    )
    upscale_parser.add_argument(
        "-o", "--output", type=str, help="Custom output image result path"
    )
    upscale_parser.add_argument(
        "--batch", action="store_true", help="Batch upscale all images"
    )
    # 👇 UPDATED PATH
    upscale_parser.add_argument(
        "--input-dir",
        type=str,
        default="assets/upscale/input",
        help="Batch source folder",
    )
    # 👇 UPDATED PATH
    upscale_parser.add_argument(
        "--output-dir",
        type=str,
        default="assets/upscale/output",
        help="Batch storage folder",
    )


def handle_bg_remover(args):
    """Executes background removal tasks."""
    from rembg import new_session

    providers = ["CUDAExecutionProvider", "CPUExecutionProvider"]
    session = new_session("u2net", providers=providers)

    if args.batch:
        run_batch_bg(args.input_dir, args.output_dir, session)
    elif args.input:
        output_path = args.output or "assets/bg_remover/output/result.png"
        try:
            process_image(args.input, output_path, session=session)
            print(f"✅ Success! Saved to {output_path}")
        except Exception as e:
            print(f"❌ Error: {e}")


# 👈 NEW: Handles routing execution for upscaler module triggers
def handle_upscaler(args):
    """Executes super resolution upscaling pipelines based on terminal inputs."""
    from ai_media.upscaler import (
        upscale_image,
    )  # Lazy load to keep engine startup clean

    if args.batch:
        run_batch_upscale(args.input_dir, args.output_dir)
    elif args.input:
        output_path = (
            args.output or f"assets/upscale/output/{Path(args.input).stem}_upscaled.png"
        )

        try:
            upscale_image(args.input, output_path)
            print(f"✨ Success! 4x Upscaled image saved to {output_path}")
        except Exception as e:
            print(f"❌ Upscaling Failure: {e}")
    else:
        print(
            "❌ Specify target input file (-i) or invoke --batch execution parameters."
        )


def run_batch_bg(input_dir, output_dir, session):
    """Batch loop processing logic wrapper for background deletion execution."""
    input_path, output_path = Path(input_dir), Path(output_dir)
    if not input_path.exists():
        return
    output_path.mkdir(parents=True, exist_ok=True)
    files = [
        f
        for f in input_path.iterdir()
        if f.is_file() and f.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}
    ]

    print(f"🚀 Found {len(files)} images. Starting batch background removal...")
    for file in files:
        try:
            output_file = output_path / f"{file.stem}.png"
            print(f"⏳ Processing Background Removal: {file.name} ...")
            process_image(str(file), str(output_file), session=session)
            print(f"   ✅ Saved: {output_file.name}")
        except Exception as e:
            print(f"   ❌ Failed {file.name}: {e}")


# 👈 NEW: Batch loop logic processing layout for upscaling directory groups
def run_batch_upscale(input_dir, output_dir):
    """Loops over a targeted workspace directory processing 4x upscale resolutions."""
    from ai_media.upscaler import upscale_image

    input_path, output_path = Path(input_dir), Path(output_dir)
    if not input_path.exists():
        return
    output_path.mkdir(parents=True, exist_ok=True)
    files = [
        f
        for f in input_path.iterdir()
        if f.is_file() and f.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}
    ]

    print(
        f"🚀 Found {len(files)} images. Starting batch 4x super-resolution upscaling..."
    )
    for file in files:
        try:
            output_file = output_path / f"{file.stem}_upscaled.png"
            print(f"⏳ Processing Upscale: {file.name} ...")
            upscale_image(str(file), str(output_file))
            print(f"   ✨ Saved: {output_file.name}")
        except Exception as e:
            print(f"   ❌ Failed Up-sampling {file.name}: {e}")
    print("🎉 Batch upscaling workflow complete!")

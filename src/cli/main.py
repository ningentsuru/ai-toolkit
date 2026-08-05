import argparse
import sys
from .ai_cli import (
    register_ai_parser,
    handle_bg_remover,
    handle_upscaler,
)  # 👈 Added handle_upscaler
from .util_cli import register_util_parser, handle_calculator


def main():
    parser = argparse.ArgumentParser(
        description="AI Toolkit Monorepo - Central Command Center Line Router"
    )
    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Available sub-tools"
    )

    register_ai_parser(subparsers)
    register_util_parser(subparsers)

    args = parser.parse_args()

    if args.command == "bg-remover":
        handle_bg_remover(args)
    elif (
        args.command == "upscale"
    ):  # 👈 NEW: Routes token calls directly to upscaler module execution
        handle_upscaler(args)
    elif args.command == "calc":
        handle_calculator(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()

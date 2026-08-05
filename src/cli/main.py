import argparse
import sys
from .ai_cli import register_ai_parser, handle_bg_remover
from .util_cli import register_util_parser, handle_calculator


def main():
    parser = argparse.ArgumentParser(
        description="AI Toolkit Monorepo - Central Command Center Line Router"
    )
    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Available sub-tools"
    )

    # Register arguments from sub-modules
    register_ai_parser(subparsers)
    register_util_parser(subparsers)

    # Parse system terminal inputs
    args = parser.parse_args()

    # Route tracking blocks to corresponding logic engines
    if args.command == "bg-remover":
        handle_bg_remover(args)
    elif args.command == "calc":
        handle_calculator(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()

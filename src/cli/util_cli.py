import argparse
from utility_tools.number_cruncher import basic_calculate


def register_util_parser(subparsers):
    """Registers the calc sub-command into the main CLI parser."""
    util_parser = subparsers.add_parser(
        "calc", help="Lightweight Basic Calculator Utility"
    )
    util_parser.add_argument(
        "operation", choices=["add", "sub", "mul", "div"], help="Math execution mode"
    )
    util_parser.add_argument("x", type=float, help="First digit input value")
    util_parser.add_argument("y", type=float, help="Second digit input value")


def handle_calculator(args):
    """Executes mathematical tasks based on parsed inputs."""
    try:
        result = basic_calculate(args.operation, args.x, args.y)
        print(f"🔢 Result: {result}")
    except Exception as e:
        print(f"❌ Calculation Error: {e}")

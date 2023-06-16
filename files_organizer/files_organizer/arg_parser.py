from argparse import ArgumentParser


def get_parser() -> ArgumentParser:   
    parser = ArgumentParser(add_help=False)
    parser.add_argument(
        "--filesDir",
        action="store",
        type=str,
        help="Path to the directory to sort",
        required=True
    )
    parser.add_argument(
        "--customize",
        action="store_true",
        help="Path to the directory to sort",
        required=False
    )

    return parser
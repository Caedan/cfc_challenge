import sys

from interfaces.cfc_underwriting import get_cfc_data


def main() -> int:
    """
    Entry point
    """
    exit_code = get_cfc_data()

    return exit_code


if __name__ == "__main__":
    sys.exit(main())

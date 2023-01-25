import sys

from interfaces.cfc_underwriting import get_cfc_data


def main() -> int:
    """
    Entry point
    """
    get_cfc_data()

    return 0


if __name__ == "__main__":
    sys.exit(main())

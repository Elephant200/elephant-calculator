from runpy import run_module


def main() -> None:
    run_module("elephant_calculator._legacy_cli", run_name="__main__")


if __name__ == "__main__":
    main()

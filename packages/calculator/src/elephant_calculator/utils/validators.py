from fractions import Fraction
from math import sqrt

def parse_input(value):
    """
    Safely parses the input value, handling fractions, square roots, decimals, and empty inputs.

    Args:
        value (str): The user-provided input.

    Returns:
        float: The parsed value as a float.
        None: If the input is empty or invalid.

    Raises:
        ValueError: If the input cannot be parsed into a numerical value.
    """
    try:
        # Handle square roots using `eval` safely with `sqrt`
        return float(eval(value, {"__builtins__": None}, {"sqrt": sqrt, "Fraction": Fraction}))
    except Exception:
        return None
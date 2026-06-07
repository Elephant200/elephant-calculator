"""Convert whole numbers between positional numeral systems.

Reads a number written in any base from 2 to 36 and reports it in the common
bases (decimal, binary, octal, hexadecimal). Raises ``ValueError`` for malformed
input so the API can return a 400.
"""

from __future__ import annotations

_DIGITS = "0123456789abcdefghijklmnopqrstuvwxyz"


def _to_base(value: int, base: int) -> str:
    """Render a non-negative integer in ``base`` (2–36)."""
    if value == 0:
        return "0"
    out = []
    while value:
        out.append(_DIGITS[value % base])
        value //= base
    return "".join(reversed(out))


def parse_in_base(number: str, from_base: int) -> int:
    """Parse ``number`` (written in ``from_base``) into a Python int."""
    if not 2 <= from_base <= 36:
        raise ValueError("Source base must be between 2 and 36.")

    text = number.strip().lower()
    if text in ("", "-", "+"):
        raise ValueError("Enter a number to convert.")

    negative = text[0] == "-"
    if text[0] in "+-":
        text = text[1:]

    value = 0
    for ch in text:
        digit = _DIGITS.find(ch)
        if digit < 0 or digit >= from_base:
            raise ValueError(f'"{ch}" is not a valid digit in base {from_base}.')
        value = value * from_base + digit

    return -value if negative else value


def convert(number: str, from_base: int) -> list[dict[str, str]]:
    """Convert ``number`` to the common bases as ordered ``{label, value}`` rows."""
    value = parse_in_base(number, from_base)
    sign = "-" if value < 0 else ""
    magnitude = abs(value)

    return [
        {"label": "Decimal (10)", "value": sign + _to_base(magnitude, 10)},
        {"label": "Binary (2)", "value": sign + _to_base(magnitude, 2)},
        {"label": "Octal (8)", "value": sign + _to_base(magnitude, 8)},
        {"label": "Hexadecimal (16)", "value": sign + _to_base(magnitude, 16).upper()},
    ]

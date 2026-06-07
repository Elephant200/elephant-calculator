"""Descriptive statistics for a data set.

All functions operate on a plain ``list[float]`` and raise ``ValueError`` for
inputs that have no meaningful answer (empty data, sample spread on a single
value, etc.). The API layer turns those into 400 responses.
"""

from __future__ import annotations

import statistics as _stats
from math import sqrt


def _require(data: list[float]) -> list[float]:
    if not data:
        raise ValueError("Provide at least one value.")
    return data


def mean(data: list[float]) -> float:
    """Arithmetic mean (average)."""
    return _stats.fmean(_require(data))


def median(data: list[float]) -> float:
    """Middle value of the sorted data set."""
    return _stats.median(_require(data))


def mode(data: list[float]) -> list[float]:
    """Most frequent value(s). Empty when every value occurs exactly once."""
    _require(data)
    counts = {}
    for x in data:
        counts[x] = counts.get(x, 0) + 1
    top = max(counts.values())
    if top == 1:
        return []
    return sorted(v for v, c in counts.items() if c == top)


def variance(data: list[float], sample: bool = True) -> float:
    """Variance. ``sample`` uses the n-1 (Bessel-corrected) denominator."""
    _require(data)
    if sample:
        if len(data) < 2:
            raise ValueError("Sample variance needs at least two values.")
        return _stats.variance(data)
    return _stats.pvariance(data)


def standard_deviation(data: list[float], sample: bool = True) -> float:
    """Standard deviation — the spread of the data about its mean."""
    return sqrt(variance(data, sample))


# --- helpers used only by the full summary ---------------------------------

def _central_moment(data: list[float], k: int, m: float) -> float:
    n = len(data)
    return sum((x - m) ** k for x in data) / n


def _geometric_mean(data: list[float]) -> float | None:
    if any(x <= 0 for x in data):
        return None
    return _stats.geometric_mean(data)


def _harmonic_mean(data: list[float]) -> float | None:
    if any(x <= 0 for x in data):
        return None
    return _stats.harmonic_mean(data)


def _fmt(value: float | int | None) -> str:
    """Render a number the way the rest of the app does: up to 12 significant
    figures, trailing zeros trimmed, scientific notation only at the extremes."""
    if value is None:
        return "—"  # em dash
    if isinstance(value, int):
        return str(value)
    if value != value:  # NaN
        return "nan"
    text = f"{value:.12g}"
    # Normalise exponent form like "1.5e+15" → "1.5e15" to match the UI.
    return text.replace("e+0", "e").replace("e+", "e").replace("e-0", "e-")


def summary(data: list[float]) -> list[dict[str, str]]:
    """A full descriptive summary as ordered ``{label, value}`` rows."""
    _require(data)
    n = len(data)
    ordered = sorted(data)
    total = sum(data)
    m = _stats.fmean(data)
    lo, hi = ordered[0], ordered[-1]

    rows: list[tuple[str, float | int | None]] = [
        ("Count", n),
        ("Sum", total),
        ("Mean", m),
        ("Median", _stats.median(data)),
        ("Minimum", lo),
        ("Maximum", hi),
        ("Range", hi - lo),
        ("Midrange", (lo + hi) / 2),
    ]

    if n >= 2:
        q1, q2, q3 = _stats.quantiles(data, n=4, method="inclusive")
        rows += [
            ("Lower quartile (Q1)", q1),
            ("Upper quartile (Q3)", q3),
            ("Interquartile range", q3 - q1),
        ]

    pvar = _stats.pvariance(data)
    pstd = sqrt(pvar)
    rows += [
        ("Population variance", pvar),
        ("Population std dev", pstd),
    ]
    if n >= 2:
        svar = _stats.variance(data)
        sstd = sqrt(svar)
        rows += [
            ("Sample variance", svar),
            ("Sample std dev", sstd),
            ("Std error of mean", sstd / sqrt(n)),
        ]
        rows.append(
            ("Coeff. of variation", (sstd / m) if m != 0 else None)
        )

    # Spread & shape
    mad = sum(abs(x - m) for x in data) / n
    rms = sqrt(sum(x * x for x in data) / n)
    rows += [
        ("Mean abs deviation", mad),
        ("Root mean square", rms),
        ("Sum of squares", sum(x * x for x in data)),
        ("Geometric mean", _geometric_mean(data)),
        ("Harmonic mean", _harmonic_mean(data)),
    ]

    m2 = _central_moment(data, 2, m)
    if n >= 2 and m2 > 0:
        skew = _central_moment(data, 3, m) / m2**1.5
        kurt = _central_moment(data, 4, m) / m2**2 - 3
        rows += [("Skewness", skew), ("Excess kurtosis", kurt)]

    out = [{"label": label, "value": _fmt(value)} for label, value in rows]

    modes = mode(data)
    out.append(
        {"label": "Mode", "value": ", ".join(_fmt(x) for x in modes) if modes else "none"}
    )
    return out

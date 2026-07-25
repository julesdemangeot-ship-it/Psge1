"""Mathematical utility functions."""

import math


def golden_ratio() -> float:
    """Calculate the golden ratio (φ) using the algebraic formula.

    The golden ratio is defined as:

        φ = (1 + √5) / 2

    Parameters
    ----------
    None

    Returns
    -------
    float
        The golden ratio φ ≈ 1.618033988749895, computed mathematically
        without hardcoding the decimal value.
    """
    return (1 + math.sqrt(5)) / 2

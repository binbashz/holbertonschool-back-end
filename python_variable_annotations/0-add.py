#!/usr/bin/python3
""" Basic annotations - add """


def add(a: float, b: float) -> float:

    """
    Add two floating-point numbers.

    Args:
        a (float): The first floating-point number.
        b (float): The second floating-point number.

    Returns:
        float: The sum of 'a' and 'b'.
    """
    # Arg annotations (a: float, b: float) indicate 'a' & 'b' are float values.
    # Return annotation (-> float) indicates function returns a float value.

    # Sum the input numbers and return the result
    return a + b

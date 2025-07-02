import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """

	give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]
	returns a list of BMI values based on 2 lists of integers or floats that come as input

    """
    assert len(height) == len(weight)
    return list(np.divide(np.array(weight), np.multiply(np.array(height), np.array(height))))


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """

	apply_limit(bmi: list[int | float], limit: int) -> list[bool]
	returns a list of booleans (True if above the limit) based on a list of integers or floats and an integer representing a limit as parameters

	"""
    return list(np.array(bmi) > limit)

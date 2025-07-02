import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """

    give_bmi(height: list[int | float], weight: \
        list[int | float]) -> list[int | float]
    returns a list of BMI values based on 2 lists \
        of integers or floats that come as input

    """
    try:
        return list(np.divide(np.array(weight),
                              np.multiply(np.array(height), np.array(height))))
    except (TypeError, ValueError):
        print("AssertionError: the arguments are bad")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """

    apply_limit(bmi: list[int | float], limit: int) -> list[bool]
    returns a list of booleans (True if above the limit) \
        based on a list of integers or floats and an integer \
            representing a limit as parameters

    """
    try:
        assert type(limit) is int
        return list(np.array(bmi) > limit)
    except (TypeError, ValueError, AssertionError):
        print("AssertionError: the arguments are bad")
        return []


# tests
# from give_bmi import give_bmi, apply_limit
# height = [2.71, 1.15]
# weight = [165.3, 38.4]
# bmi = give_bmi(height, weight)
# print(bmi, type(bmi))
# print(apply_limit(bmi, 26))
# print()
# height = [2.71, 1.15, "d"]
# weight = [165.3, 38.4]
# bmi = give_bmi(height, weight)
# print(bmi, type(bmi))
# print(apply_limit(bmi, 26))
# print()
# height = [2.71, 1.15, 2]
# weight = [165.3, 38.4]
# bmi = give_bmi(height, weight)
# print(bmi, type(bmi))
# print(apply_limit(bmi, 26))
# print()
# height = [2.71, 1.15, 2]
# weight = [165.3, 38.4]
# bmi = give_bmi(height, weight)
# print(bmi, type(bmi))
# print(apply_limit(bmi, "4"))
# print()

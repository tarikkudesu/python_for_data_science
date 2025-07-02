import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """

    takes as parameters a 2D array, prints its shape.
    returns a truncated version of the array based
    on the provided start and end arguments.

    """
    try:
        assert type(family) is list
        assert type(start) is int
        assert type(end) is int
        assert len(set(len(arr) for arr in family)) == 1
        arr = np.array(family)
        res = arr[start:end]
        print(f"My shape is : {arr.shape}")
        print(f"My new shape is : {res.shape}")
        return res
    except (AssertionError, ValueError, TypeError):
        print("AssertionError: the arguments are bad")


# from array2D import slice_me
# family = [[1.80, 78.4],
#             [2.15, 102.7],
#             [2.10, 98.5],
#             [1.88, 75.2]]
# print(slice_me(family, 0, 2))
# print(slice_me(family, 1, -2))
# print()
# family = [[1.80, 78.4, 3],
#           [2.15, 102.7],
#           [2.10, 98.5],
#           [1.88, 75.2]]
# print(slice_me(family, 0, 2))
# print(slice_me(family, 1, -2))
# print()
# family = [[1.80, 78.4, 3],
#           ["2.15", 102.7],
#           [2.10, 98.5],
#           [1.88, 75.2]]
# print(slice_me(family, 0, 2))
# print(slice_me(family, 1, -2))
# print()
# family = [[1.80, 78.4, 3],
#           [True, 102.7],
#           [2.10, 98.5],
#           [1.88, 75.2]]
# print(slice_me(family, 0, 2))
# print(slice_me(family, 1, -2))
# print()

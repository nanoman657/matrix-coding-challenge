from typing import Callable


def get_entries_in_proximity(
    row: int, col: int, proximity: int, matrix: list[list[int | float]]
) -> set:
    nearby_entries = set()
    row_range = range(max(0, row - proximity), min(row + proximity + 1, len(matrix)))
    col_range = range(max(0, col - proximity), min(col + proximity + 1, len(matrix[0])))

    for i in row_range:
        for j in col_range:
            if (abs(row - i) + abs(col - j)) <= proximity:
                nearby_entries.add((i, j))
    return nearby_entries


def get_entries_in_proximity_of_entry_condition(
    matrix: list[list[int]],
    distance_threshhold: int,
    condition_func: Callable,
) -> int:
    m = len(matrix)
    n = len(matrix[0])
    nearby_entries = set()
    for i in range(m):
        for j in range(n):
            if condition_func(matrix[i][j]):
                nearby_entries = nearby_entries.union(
                    get_entries_in_proximity(i, j, distance_threshhold, matrix)
                )
    return len(nearby_entries)


def check_value_is_positive(value: int) -> bool:
    return value > 0


def get_positive_entries_in_proximity(
    matrix: list[list[int | float]], distance_threshhold: int
) -> int:
    m = len(matrix)
    n = len(matrix[0])
    nearby_entries = set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] > 0:
                nearby_entries = nearby_entries.union(
                    get_entries_in_proximity(i, j, distance_threshhold, matrix)
                )
    return len(nearby_entries)


example_matrix = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]

matrix_with_ones = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]

matrix_with_zeroes = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

matrix_with_neg = [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]

matrix_with_neg_zeroes = [
    [-1, 0, -1, -1, -1],
    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1],
]

matrix_with_neg_zeroes_pos = [
    [-1, 0, 1, -1, -1],
    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1],
]

matrix_with_inf = [
    [-1, 0, float("inf"), -1, -1],
    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1],
]

matrix_with_min_size = [[0, 0], [0, 0]]


# Test main solution function

# Test main solution function

assert (
    get_positive_entries_in_proximity(example_matrix, 1) == 7
), "Function failed with the example matrix."
assert (
    get_positive_entries_in_proximity(matrix_with_ones, 1) == 15
), "Function failed with matrix with all positive values."
assert (
    get_positive_entries_in_proximity(matrix_with_ones, 0) == 15
), """Function failed with matrix with all positive values
    and zero proximity requirement"""
assert (
    get_positive_entries_in_proximity(matrix_with_zeroes, 1) == 0
), "Function failed with matrix with all zero values."
assert (
    get_positive_entries_in_proximity(matrix_with_neg_zeroes, 1) == 0
), "Function failed with matrix with all zero and negative values."
assert (
    get_positive_entries_in_proximity(matrix_with_neg_zeroes_pos, 1) == 4
), "Function failed with matrix with negative, zero, and positive values."
assert (
    get_positive_entries_in_proximity(matrix_with_inf, 1) == 4
), "Function failed with matrix containing an infinite positive value."
assert (
    get_positive_entries_in_proximity(matrix_with_min_size, 0) == 0
), "Function failed with matrix of minimum size."


# Test bonus solution function
assert (
    get_entries_in_proximity_of_entry_condition(
        example_matrix, 1, check_value_is_positive
    )
    == 7
), "Function failed with the example matrix."
assert (
    get_entries_in_proximity_of_entry_condition(
        matrix_with_ones, 1, check_value_is_positive
    )
    == 15
), "Function failed with matrix with all positive values."
assert (
    get_entries_in_proximity_of_entry_condition(
        matrix_with_ones, 0, check_value_is_positive
    )
    == 15
), """Function failed with matrix with all positive values
    and zero proximity requirement"""
assert (
    get_entries_in_proximity_of_entry_condition(
        matrix_with_zeroes, 1, check_value_is_positive
    )
    == 0
), "Function failed with matrix with all zero values."
assert (
    get_entries_in_proximity_of_entry_condition(
        matrix_with_neg_zeroes, 1, check_value_is_positive
    )
    == 0
), "Function failed with matrix with all zero and negative values."
assert (
    get_entries_in_proximity_of_entry_condition(
        matrix_with_neg_zeroes_pos, 1, check_value_is_positive
    )
    == 4
), "Function failed with matrix with negative, zero, and positive values."
assert (
    get_entries_in_proximity_of_entry_condition(
        matrix_with_inf, 1, check_value_is_positive
    )
    == 4
), "Function failed with matrix containing an infinite positive value."
assert (
    get_entries_in_proximity_of_entry_condition(
        matrix_with_min_size, 0, check_value_is_positive
    )
    == 0
), "Function failed with matrix of minimum size."

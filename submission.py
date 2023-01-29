def entries_in_proximity(row: int, col: int, proximity: int, matrix: list[list]) -> set:
    nearby_entries = set()
    row_range = range(max(0, row - proximity), min(row + proximity + 1, len(matrix)))
    col_range = range(max(0, col - proximity), min(col + proximity + 1, len(matrix[0])))

    for i in row_range:
        for j in col_range:
            if (abs(row - i) + abs(col - j)) <= proximity:
                nearby_entries.add((i, j))
    return nearby_entries


def positive_entries_in_proximity(
    matrix: list[list[int]], distance_threshhold: int
) -> int:
    m = len(matrix)
    n = len(matrix[0])
    nearby_entries = set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] > 0:
                nearby_entries = nearby_entries.union(
                    entries_in_proximity(i, j, distance_threshhold, matrix)
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


error_message = "The function did not return the correct number of cells."

assert (
    positive_entries_in_proximity(example_matrix, 1) == 7
), "Function failed with the example matrix."
assert (
    positive_entries_in_proximity(matrix_with_ones, 1) == 15
), "Function failed with matrix with all positive values."
assert (
    positive_entries_in_proximity(matrix_with_ones, 0) == 15
), """Function failed with matrix with all positive values
    and zero proximity requirement"""
assert (
    positive_entries_in_proximity(matrix_with_zeroes, 1) == 0
), "Function failed with matrix with all zero values."
assert (
    positive_entries_in_proximity(matrix_with_neg_zeroes, 1) == 0
), "Function failed with matrix with all zero and negative values."
assert (
    positive_entries_in_proximity(matrix_with_neg_zeroes_pos, 1) == 4
), "Function failed with matrix with negative, zero, and positive values."
assert (
    positive_entries_in_proximity(matrix_with_inf, 1) == 4
), "Function failed with matrix containing an infinite positive value."
assert (
    positive_entries_in_proximity(matrix_with_min_size, 0) == 0
), "Function failed with matrix of minimum size."

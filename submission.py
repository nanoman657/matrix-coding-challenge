def close_cells(row: int, col: int, proximity: int, matrix: list[list]):
    nearby = set()
    counter = 0
    row_range = range(max(0, row - proximity), min(row + proximity + 1, len(matrix)))
    col_range = range(max(0, col - proximity), min(col + proximity + 1, len(matrix[0])))
    for i in row_range:
        for j in col_range:
            if (abs(row - i) + abs(col - j)) <= proximity:
                nearby.add((i, j))
    return nearby

def cells_in_proximity(matrix: list[list], proximity: int) -> int:

    counter = 0
    m = len(matrix)
    n = len(matrix[0])
    nearby_cells = set()
    for i in range(m):
        for j in range(n): 
            if matrix[i][j] > 0:
                nearby_cells = nearby_cells.union(close_cells(i, j, proximity, matrix))
    return len(nearby_cells)
                




example_matrix = [  [ 0, 0, 0, 0, 0 ],
                    [ 0, 0, 1, 0, 0 ],
                    [ 0, 0, 1, 0, 0 ] ]

matrix_with_ones = [ [ 1, 1, 1, 1, 1 ],
                     [ 1, 1, 1, 1, 1 ],
                     [ 1, 1, 1, 1, 1 ] ]


matrix_with_zeroes = [ [ 0, 0, 0, 0, 0 ],
                       [ 0, 0, 0, 0, 0 ],
                       [ 0, 0, 0, 0, 0 ] ]

matrix_with_neg =    [ [ -1, -1, -1, -1, -1 ],
                       [ -1, -1, -1, -1, -1 ],
                       [ -1, -1, -1, -1, -1 ] ]

matrix_with_neg_zeroes =    [ [ -1, 0, -1, -1, -1 ],
                              [ -1, -1, -1, -1, -1 ],
                              [ -1, -1, -1, -1, -1 ] ]

matrix_with_neg_zeroes_pos =    [ [ -1, 0, 1, -1, -1 ],
                                  [ -1, -1, -1, -1, -1 ],
                                  [ -1, -1, -1, -1, -1 ] ]

matrix_with_inf =    [ [ -1, 0, float('inf'), -1, -1 ],
                       [ -1, -1, -1, -1, -1 ],
                       [ -1, -1, -1, -1, -1 ] ]

matrix_with_min_size = [[0, 0], [0, 0]]



error_message = 'The function did not return the correct number of cells.'

assert cells_in_proximity(example_matrix, 1) == 7, "Function failed with the example matrix."
assert cells_in_proximity(matrix_with_ones, 1) == 15, "Function failed with matrix with all positive values."
assert cells_in_proximity(matrix_with_ones, 0) == 15, "Function failed with matrix with all positive values and zero proximity requirement"
assert cells_in_proximity(matrix_with_zeroes, 1) == 0, "Function failed with matrix with all zero values."
assert cells_in_proximity(matrix_with_neg_zeroes, 1) == 0, "Function failed with matrix with all zero and negative values."
assert cells_in_proximity(matrix_with_neg_zeroes_pos, 1) == 4, "Function failed with matrix with negative, zero, and positive values."
assert cells_in_proximity(matrix_with_inf, 1) == 4, "Function failed with matrix containing an infinite positive value."
assert cells_in_proximity(matrix_with_min_size, 0)  == 0, "Function failed with matrix of minimum size."

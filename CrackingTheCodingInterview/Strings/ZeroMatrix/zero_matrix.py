# O(n^2) time | O(n^2) space
def zero_matrix1(matrix):
    zero_pos = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                zero_pos.append((row, col))

    for pos in zero_pos:
        row = pos[0]
        col = pos[1]
        for i in range(len(matrix[row])):
            matrix[row][i] = 0
        for i in range(len(matrix)):
            matrix[i][col] = 0

# O(n^2) time | O(1) space
def zero_matrix2(matrix):
    row_0_has_0 = False
    col_0_has_0 = False
    for col in range(len(matrix[0])):
        if matrix[0][col] == 0:
            row_0_has_0 = True
    for row in range(len(matrix)):
        if matrix[row][0] == 0:
            col_0_has_0 = True
    
    # Tracking where zeroes were found.
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[row])):
            if matrix[row][col] == 0:
                matrix[0][col] = 0
                matrix[row][0] = 0

    # Zeroing columns where a 0 was found.
    # Don't zero out column 0! Wait for the column_0_has_0
    for col in range(1, len(matrix[0])):
        if matrix[0][col] == 0:
            for row in range(1, len(matrix)):
                matrix[row][col] = 0

    # Zeroing rows where a 0 was found.
    for row in range(len(matrix)):
        if matrix[row][0] == 0:
            for col in range(1, len(matrix[row])):
                matrix[row][col] = 0

    if row_0_has_0:
        for col in range(len(matrix[0])):
            matrix[0][col] = 0

    if col_0_has_0:
        for row in range(len(matrix)):
            matrix[row][0] = 0



test1 = [[1, 1, 1, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
test2 = [[1, 1, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
test3 = [[1, 1, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1]]
test4 = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

zero_matrix1(test1)
zero_matrix2(test1)
print(test1)
zero_matrix2(test2)
print(test2)
zero_matrix2(test3)
print(test3)
zero_matrix2(test4)
print(test4)

def rotate_matrix(matrix):
    if len(matrix) != len(matrix[0]) or len(matrix) == 0:
        return

    n = len(matrix)
    for layer in range(0, n // 2):
        start = layer
        end = n - 1 - layer

        for i in range(start, end):
            offset = i - start
            #Store the top left item in a temporary variable.
            top = matrix[start][i]
            
            #Put the lower left item in the top left position.
            matrix[start][i] = matrix[end - offset][start]

            #Put the lower right item in the lower left position.
            matrix[end - offset][start] = matrix[end][end - offset]

            #Put the upper right item in the lower right position.
            matrix[end][end - offset] = matrix[i][end]

            #Put the top item in the upper right.
            matrix[i][end] = top


test = [[1,2,3],[4,5,6],[7,8,9]]

rotate_matrix(test)

print(test)
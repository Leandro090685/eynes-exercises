def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    new_matrix = []

    for col in range(cols):
        new_row = []

        for row in range(rows):
            new_row.append(matrix[row][col])
        new_matrix.append(new_row)

    return new_matrix

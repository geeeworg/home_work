def get_column_sum(matrix, column_index):
    column_sum = 0
    for row in matrix:
        column_sum += row[column_index]
    return column_sum




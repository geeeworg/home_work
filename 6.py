def get_row_average(matrix, row_index):
    row = matrix[row_index]
    row_sum = sum(row)
    row_average = row_sum / len(row)
    return row_average




import random

def generate_random_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = [random.randint(1, 100) for i in range(cols)]
        matrix.append(row)
    return matrix



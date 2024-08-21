def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        list_matrix = []
        for k in range(m):
            list_matrix.append(value)
        matrix.append(list_matrix)
    return matrix
result1 = get_matrix(4, 5, 15)
print(result1)
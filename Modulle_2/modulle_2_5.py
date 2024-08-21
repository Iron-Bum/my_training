def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        list_matrix = []
        for k in range(m):
            list_matrix.append(value)
        matrix.append(list_matrix)
    return matrix
result1 = get_matrix(2, 2, 15)
result2 = get_matrix(3, 5, 27)
result3 = get_matrix(5, 3, 88)
print(result1)
print(result2)
print(result3)
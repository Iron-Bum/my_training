def calculate_structure_sum(list_):  # функция сумм всех чисел и строк
    result = 0
    for i in list_:
        if isinstance(i, str):
            result += len(i)
        elif isinstance(i, int):
            result += i
        elif isinstance(i, dict):
            result += calculate_structure_sum(list(i.values())) + calculate_structure_sum(i)
        else:
            result += calculate_structure_sum(i)
    return result


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(calculate_structure_sum(data_structure))

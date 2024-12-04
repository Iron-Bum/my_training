first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (
    len(string_f) - len(string_s)
    for string_f, string_s in zip(first, second)
    if len(string_f) != len(string_s)
)
second_result = (
    len(first[i]) == len(second[i])
    for i in range(min(len(first), len(second)))
)
print(list(first_result))
print(list(second_result))

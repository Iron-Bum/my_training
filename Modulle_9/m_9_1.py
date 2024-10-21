def apply_all_func(int_list, *functions):
    try:
        result = {}
        for function in functions:
            result[function.__name__] = function(int_list)
        return result
    except TypeError:
        print('Функция не поддержиает такой тип данных')


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

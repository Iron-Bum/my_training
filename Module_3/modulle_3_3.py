def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = [25, 'true', True]
values_dict = {'a': 77, 'b': 'false', 'c': False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ['apple', 13]
print_params(*values_list_2, 42)
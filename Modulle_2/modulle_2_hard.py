import random

place = int(random.uniform(3, 20))
result = []
for i in range(1, place):
    if place % i == 0 and place / i != 2:
        divider = int(place / i)
    else:
        continue
    for k in range(1, divider):
        if k < (divider / 2):
            temp_value = [str(f'{divider - k}-{k}')]
            result.extend(temp_value)
        else:
            break
print(f'Число в первом поле {place}, ваш пароль: ')
print(result)

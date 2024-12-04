#import random

#place = int(random.uniform(3, 20))
place = 20
result = ''
for i in range(place, 0, -1):
    if place % i == 0 and place / i != 2 and place / i != 1:
        divider = int(place / i)
    else:
        continue
    for k in range(1, divider):
        if k < (divider / 2):
            result += f'{k}+{divider - k} '
        else:
            break
print(f'Число в первом поле {place}, ваш пароль: ')
print(result)

import random

num = int(random.uniform(3, 20))
result = ''
for i in range(1, num):
    for k in range(i +1, num):
        if num % (i + k) == 0:
            result += f'{i}+{k} '
print(f'Ваше число: {num}')
print(f'Ваш шифр : {result}')
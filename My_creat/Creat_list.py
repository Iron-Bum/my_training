import random


def creat_list(quantity=7):
    lst = []
    while len(lst) < quantity:
        lst.append(int(random.uniform(0, 100)))
    if int(random.uniform(1,8)) % 2 == 0:
        lst.append(creat_list())
    return lst

print(creat_list(10))

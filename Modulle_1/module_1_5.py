
immutable_war = 1,[2,5,8],"string", True #кортеж
print(immutable_war)
immutable_war[1][2]=13
#immutable_war[0]=7 Нельзя изменить значения элемента кортежа т.к. они неизменны!
print(immutable_war)
mutable_list = [3,7,"name", False] #список
print(mutable_list)
mutable_list[2]= 'age' # Значения в списке можно изменять
print(mutable_list)
my_dict={'Sergey':1984,'Inna':1983,'Mila':2013,'Anna':2009}
print(my_dict)
print(my_dict['Inna'])
print(my_dict.get('Roman'))
my_dict.update({'Andrey':1984,'Vika':1985})
temp_value=my_dict.pop('Sergey')
print(temp_value)
print(my_dict)

my_set={1,3,23,3,0,23,7,1,2,3,15,'Max','Bill','Max'}
print(my_set)
my_set.update({35,'Lisa'}) #нет возможности использовать метод .add , т.к. он может добавить только один элемент
print(my_set)
my_set.discard('Bill') #можно использовать метод ,remuve, но при отсутствии значения он будет выдавать ошибку
print(my_set)
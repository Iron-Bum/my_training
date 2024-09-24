class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.houses_history.append(args[0])
        return instance.houses_history
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


h1 = House('ЖК Эльбрус', 10)
print(h1)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
#del(h2)
# print(House.houses_history)

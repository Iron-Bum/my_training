class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_too(self, new_floor):
        if self.number_of_floors > new_floor > 0:
            print(new_floor)
        else:
            print('Такого этажа не существует')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_too(5)
h2.go_too(10)

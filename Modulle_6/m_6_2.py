class Vehicles:
    __COLOR_VARIANTS = ['black', 'white', 'blue', 'red', 'grey', 'green']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power

    def get_model(self):
        return print(f'Модель: {self.__model}')

    def get_horsepower(self):
        return print(f'Мощность: {self.__engine_power}')

    def color(self):
        return print(f'Цвет: {self.__color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.color()
        return print(f'Владелец: {self.owner}')

    def set_color(self, color):
        if color.lower() in self.__COLOR_VARIANTS:
            self.__color = color
        else:
            return print(f'Нельзя сменить на {color}')


class Sedan(Vehicles):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

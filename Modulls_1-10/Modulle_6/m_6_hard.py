import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color)
        if len(sides) == self.sides_count:
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count
        self.filled = True

    def __len__(self):
        sum_sides = 0
        for side in self.__sides:
            sum_sides += side
        return sum_sides

    def info(self):
        print(f'color: {self.__color}, sides: {self.__sides}, filled: {self.filled}')

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(colors):
        return (
                len(colors) == 3 and all(isinstance(color, int) and 0 <= color <= 255 for color in colors)
        )

    def set_color(self, *color_):
        if self.__is_valid_color(color_):
            self.__color = list(color_)

    def __is_valid_sides(self, *sides):
        return (
                len(sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in sides)
        )

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *side):
        super().__init__(color, *side)
        self.__radius = side[0] / (2 * math.pi)

    def get_square(self):
        if isinstance(self.__radius, (int, float)) and self.__radius > 0:
            return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        p = self.__len__() / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = list(sides) * self.sides_count
        else:
            sides = [1] * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        return (self.get_sides()[0]) ** 3


circle1 = Circle((200, 200, 100), 20, 5)  # (Цвет, стороны)
triangle = Triangle((100, 200, 200), 5, 10, 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

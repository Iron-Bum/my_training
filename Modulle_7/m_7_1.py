from pprint import pprint


class Shop:
    def __init__(self):
        self.__fill_name = 'products.txt'
        name = open(self.__fill_name, 'w')
        name.close()

    def get_product(self):
        name = open(self.__fill_name, 'r')
        file = name.read()
        name.close()
        return file

    def add(self, *products):
        for product_ in products:
            name = open(self.__fill_name, 'a')
            if product_ in name:
                name.write(f'\n{product_}')
                name.close()
            else:
                name.write(f'\nтакой продукт ужу существует')
                name.close()


class Product:
    def __init__(self, name, wight, category):
        self.name = name
        self.category = category
        self.weight = wight

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

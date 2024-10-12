class Shop:
    def __init__(self):
        self.__fill_name = 'products.txt'
        name = open(self.__fill_name, 'a+')
        name.close()

    def get_products(self):
        with open(self.__fill_name, 'r') as file:
            return file.read()

    def add(self, *products):
        for product in products:
            if str(product) in self.get_products():
                print('такой товар уже есть')
            else:
                with open(self.__fill_name, 'a') as file:
                    file.write(f'{str(product)}\n')


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

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

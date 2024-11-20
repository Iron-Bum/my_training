class Dog:
    def __init__(self, name, aggression=False):
        self.name = name
        self.aggression = aggression

    def pet_it(self):
        if self.aggression:
            print(f'{self.name} зарычал(а) и укусил(а) вас!')
        else:
            print(f'{self.name} завилял(а) хвостом и лег(ла) на спину ;)')


dog_first = Dog('Мухтар')
dog_second = Dog('Полкан', True)

# dog_first.pet_it()
# dog_second.pet_it()


def introspection_info(obj):
    result = {
        'type': str(type(obj)),
        'module': obj.__module__,
        'atributes': [method for method in dir(obj) if not callable(getattr(obj, method))],
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))]
    }
    return result


object_info = introspection_info(dog_first)
for key, value in object_info.items():
    print(f"{key}: {value}")

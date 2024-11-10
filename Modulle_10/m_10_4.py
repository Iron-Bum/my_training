import threading
from queue import Queue
import time
import random


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for i in guests:
            if any(_.guest is None for _ in self.tables):
                for table in self.tables:
                    if table.guest is None:
                        table.guest = i
                        i.start()
                        i.join()
                        print(f'{i.name} сел(а) за стол № {table.number}')
                        break
            else:
                self.queue.put(i)
                print(f'{i.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(_.guest is not None for _ in self.tables):
            for table in self.tables:
                if table.guest is not None:
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if not self.queue.empty() and any(_.guest is None for _ in self.tables):
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}"')
                    table.guest.start()
                    table.guest.join()


#Создание столов
tables = [Table(number) for number in range(1, 6)]
#Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
#Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()


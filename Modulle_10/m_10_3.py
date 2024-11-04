import threading
import time
import random


class Bank(threading.Thread):
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        counter = 100
        while counter:
            counter -= 1
            temp_num = random.randint(50, 500)
            time.sleep(0.001)
            with self.lock:
                if self.balance < 500:
                    self.balance += temp_num
                    print(f'Пополнение: {temp_num}. Баланс: {self.balance}')
                # elif self.balance >= 500 and self.lock.locked():
                #     self.lock.release()

    def take(self):
        counter = 100
        time.sleep(0.001)
        while counter:
            counter -= 1
            temp_num = random.randint(50, 500)
            with self.lock:
                print(f'Запрос на {temp_num}.')
                if temp_num <= self.balance:
                    self.balance -= temp_num
                    print(f'Снятие: {temp_num}. Текущий баланс: {self.balance}')
                # else:
                #     print(f'Запрос отклонён, недостаточно средств.')
                #     self.lock.acquire()


bk = Bank()
th1 = threading.Thread(target=Bank.deposit(bk, ))
th2 = threading.Thread(target=Bank.take(bk, ))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')


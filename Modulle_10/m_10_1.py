import threading
import time


def write_name(words_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(words_count):
            file.write(f'Какое-то слово №: {i}\n')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


def time_threads(start_threads, end_threads):
    return f'Время работы функций: {round((end_threads - start_threads), 6)}'

start_time = time.time()
write_name(10, 'example1.txt')
write_name(30, 'example2.txt')
write_name(200, 'example3.txt')
write_name(100, 'example4.txt')
end_time = time.time()
print(time_threads(start_time, end_time))

start_time = time.time()
thread_1 = threading.Thread(target=write_name, args=(10, 'example5.txt'))
thread_1.start()
thread_2 = threading.Thread(target=write_name, args=(30, 'example6.txt'))
thread_2.start()
thread_3 = threading.Thread(target=write_name, args=(200, 'example7.txt'))
thread_3.start()
thread_4 = threading.Thread(target=write_name, args=(100, 'example8.txt'))
thread_4.start()
thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
end_time = time.time()
print(time_threads(start_time, end_time))

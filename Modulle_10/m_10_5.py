import multiprocessing
import threading
import time


def read_info(name):
    all_data = []
    with open(name, "r") as file:
        line = file.readlines()
        all_data.append(line)
    return len(*all_data)


filenames = [f'file {number}.txt' for number in range(1, 5)]

threads = [threading.Thread(target=read_info, args=(filenames[i],)) for i in range(len(filenames))]
# start_time = time.time()
# for thread in threads:
#     thread.start()
# for thread in threads:
#     thread.join()
# finish_time = time.time()
# program_time = finish_time - start_time
# print(program_time)

if __name__ == '__main__':
    start_time = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        result = pool.map(read_info, filenames)
    finish_time = time.time()
    program_time = finish_time - start_time
    print(program_time)
    print(result)

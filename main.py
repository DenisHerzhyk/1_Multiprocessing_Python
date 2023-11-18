# 2.1 MULTIPROCESSING

from multiprocessing import cpu_count, Pool
from functools import partial


def is_prime(num):
    if num <= 1: return False
    if num == 2 or num == 3: return True
    for i in range(2, int(num ** 1 / 2) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    x = int(input("Input number: "))
    pool = Pool(processes = cpu_count())
    func = partial(is_prime)
    result = pool.map(func,range(2,x))
    pool.close()
    pool.join()

    if is_prime(x):
        print("Prime number")
    else:
        print("Not Prime number")

# 2.2

from multiprocessing import Process
from time import sleep


def first():
    for i in range(1, 11):
        if i % 2 != 0:
            print(i)
            sleep(1)


def second():
    for i in range(1, 11):
        if i % 2 == 0:
            print(i)
            sleep(1)


if __name__ == '__main__':
    process1 = Process(target=first)
    process2 = Process(target=second)

    process1.start()
    process2.start()

    process1.join()
    process2.join()

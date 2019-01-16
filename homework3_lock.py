# Thread synchronization using Lock

from threading import Thread
from threading import Lock
from time import sleep


def print_even_numbers(number_range, lock_object):
    """Print even numbers from input range of numbers

    :param number_range: range of numbers
    :param lock_object: lock object for threads synchronization
    :return:
    """
    even_numbers = filter(lambda number: number % 2 == 0, number_range)
    for even_number in even_numbers:
        with lock_object:
            print(even_number)
        sleep(0.1)


def print_odd_numbers(number_range, lock_object):
    """Print odd numbers from input range of numbers

    :param number_range: range of numbers
    :param lock_object: lock object for threads synchronization
    :return:
    """
    odd_numbers = filter(lambda number: number % 2 != 0, number_range)
    for odd_number in odd_numbers:
        with lock_object:
            print(odd_number)
        sleep(0.1)


if __name__ == "__main__":
    numbers = range(101)
    lock = Lock()
    thread1 = Thread(name="lock_even", target=print_even_numbers, args=(numbers, lock))
    thread2 = Thread(name="lock_odd", target=print_odd_numbers, args=(numbers, lock))
    thread1.start()
    thread2.start()

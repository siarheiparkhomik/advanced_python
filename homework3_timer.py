# Thread synchronization using Timer

from threading import Timer
from time import sleep


def print_even_numbers(number_range):
    """
    Prints even numbers from input range of numbers
    :param number_range: range of numbers
    :return:
    """
    even_numbers = filter(lambda number: number % 2 == 0, number_range)
    for even_number in even_numbers:
        print(even_number)
        sleep(0.2)


def print_odd_numbers(number_range):
    """
    Prints odd numbers from input range of numbers
    :param number_range: range of numbers
    :return:
    """
    odd_numbers = filter(lambda number: number % 2 != 0, number_range)
    for odd_number in odd_numbers:
        print(odd_number)
        sleep(0.2)


if __name__ == "__main__":
    numbers = range(101)
    thread1 = Timer(0.1, print_even_numbers, args=[numbers])
    thread2 = Timer(0.2, print_odd_numbers, args=[numbers])
    thread1.start()
    thread2.start()

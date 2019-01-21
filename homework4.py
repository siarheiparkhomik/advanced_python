"""
Output numbers from 0..100 in order.

First thread outputs even numbers. Second thread outputs odd numbers.
Pipe is used for process synchronization purposes.
"""


from multiprocessing import Pipe
from multiprocessing import Process


def print_even_numbers(number_range, connection):
    """Print even numbers from input range.

    :param number_range: range of numbers.
    :param connection: connection for synchronization
    purposes.
    :return: None
    """
    even_numbers = filter(lambda number: number % 2 == 0, number_range)
    for even_number in even_numbers:
        connection.recv()
        print(even_number)
        connection.send("start")


def print_odd_numbers(number_range, connection):
    """Print odd numbers from input range.

    :param number_range: range of numbers.
    :param connection: connection for synchronization
    purposes.
    :return: None
    """
    odd_numbers = filter(lambda number: number % 2 != 0, number_range)
    for odd_number in odd_numbers:
        connection.recv()
        print(odd_number)
        connection.send("start")


if __name__ == "__main__":
    numbers = range(101)
    even_connect, odd_connect = Pipe()
    even_process = Process(target=print_even_numbers, args=(numbers, even_connect))
    odd_process = Process(target=print_odd_numbers, args=(numbers, odd_connect))
    even_process.start()
    odd_process.start()
    odd_connect.send("start")

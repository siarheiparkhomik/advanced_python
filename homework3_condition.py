# Thread synchronization using Condition

from threading import Condition
from threading import Thread


def print_even_numbers(number_range, condition_obj):
    """Prints even numbers from input range of numbers

    :param number_range: range of numbers
    :param condition_obj: condition object for threads synchronization
    :return:
    """
    even_numbers = filter(lambda number: number % 2 == 0, number_range)
    for even_number in even_numbers:
        with condition_obj:
            condition_obj.wait()
            print(even_number)
            condition_obj.notify()


def print_odd_numbers(number_range, condition_obj):
    """Prints odd numbers from input range of numbers

    :param number_range: range of numbers
    :param condition_obj: condition object for threads synchronization
    :return:
    """
    odd_numbers = filter(lambda number: number % 2 != 0, number_range)
    for odd_number in odd_numbers:
        with condition_obj:
            condition_obj.wait()
            print(odd_number)
            condition_obj.notify()


def producer(condition_object):
    """Starts threads execution by notifying

    :param condition_object: condition object for threads synchronization
    :return:
    """
    with condition_object:
        condition_object.notify()


if __name__ == "__main__":
    numbers = range(101)
    condition = Condition()
    thread1 = Thread(name="cond_even", target=print_even_numbers, args=(numbers, condition))
    thread2 = Thread(name="cond_odd", target=print_odd_numbers, args=(numbers, condition))
    thread3 = Thread(name="producer", target=producer, args=(condition,))
    thread1.start()
    thread2.start()
    thread3.start()

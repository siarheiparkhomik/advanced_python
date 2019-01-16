# Thread synchronization using Semaphore

from threading import Semaphore
from threading import Thread


def print_even_numbers(number_range, even_semaphore, odd_semaphore):
    """Prints even numbers from input range of numbers

    :param number_range: range of numbers
    :param even_semaphore: Semaphore object for even Thread synchronization
    :param odd_semaphore: Semaphore object for odd Thread synchronization
    :return:
    """
    even_numbers = filter(lambda number: number % 2 == 0, number_range)
    for even_number in even_numbers:
        even_semaphore.acquire()
        print(even_number)
        odd_semaphore.release()
    even_semaphore.release()


def print_odd_numbers(number_range, even_semaphore, odd_semaphore):
    """Prints odd numbers from input range of numbers

    :param number_range: range of numbers
    :param even_semaphore: Semaphore object for even Thread synchronization
    :param odd_semaphore: Semaphore object for odd Thread synchronization
    :return:
    """
    odd_numbers = filter(lambda number: number % 2 != 0, number_range)
    for odd_number in odd_numbers:
        odd_semaphore.acquire()
        print(odd_number)
        even_semaphore.release()
    odd_semaphore.release()


if __name__ == "__main__":
    numbers = range(101)
    even_sem = Semaphore(1)
    odd_sem = Semaphore(0)
    thread1 = Thread(name="sem_even", target=print_even_numbers, args=(numbers, even_sem, odd_sem))
    thread2 = Thread(name="sem_odd", target=print_odd_numbers, args=(numbers, even_sem, odd_sem))
    thread1.start()
    thread2.start()

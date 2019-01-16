# Thread synchronization using Event

from threading import Thread, Event


def print_even_numbers(number_range, even_event_obj, odd_event_obj):
    """
    Prints even numbers from input range of numbers
    :param number_range: range of numbers
    :param even_event_obj: Event object for even Thread synchronization
    :param odd_event_obj: Event object for odd Thread synchronization
    :return:
    """
    even_numbers = filter(lambda number: number % 2 == 0, number_range)
    for even_number in even_numbers:
        while not even_event_obj.is_set():
            pass
        print(even_number)
        even_event_obj.clear()
        odd_event_obj.set()


def print_odd_numbers(number_range, even_event_obj, odd_event_obj):
    """
    Prints odd numbers from input range of numbers
    :param number_range: range of numbers
    :param even_event_obj: Event object for even Thread synchronization
    :param odd_event_obj: Event object for odd Thread synchronization
    :return:
    """
    odd_numbers = filter(lambda number: number % 2 != 0, number_range)
    for odd_number in odd_numbers:
        while not odd_event_obj.is_set():
            pass
        print(odd_number)
        even_event_obj.set()
        odd_event_obj.clear()


if __name__ == "__main__":
    numbers = range(101)
    even_event = Event()
    odd_event = Event()
    thread1 = Thread(name="event_env", target=print_even_numbers, args=(numbers, even_event, odd_event))
    thread2 = Thread(name="event_odd", target=print_odd_numbers, args=(numbers, even_event, odd_event))
    thread1.start()
    thread2.start()
    even_event.set()

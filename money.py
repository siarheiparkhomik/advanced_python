"""Contains Money class realization
"""
from converter import Converter


class Money(object):
    """Class represents money object
    """

    CONVERTER = Converter()

    def __init__(self, value, currency="EUR"):
        self.value = value
        self.currency = currency

    def __mul__(self, other):
        value = self.value * other
        return self.__class__(value, self.currency)

    def __rmul__(self, other):
        value = self.value * other
        return self.__class__(value, self.currency)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            currency_multiplier = self.CONVERTER.get_currencies_ratio(
                other.currency,
                self.currency)
            value = self.value + other.value * currency_multiplier
            return self.__class__(value, self.currency)
        else:
            return self + self.__class__(other, self.currency)

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(other, self.currency) + self
        return self

    def __str__(self):
        return "{} {}".format(self.value, self.currency)


if __name__ == "__main__":
    x = Money(10, "BYN")
    y = Money(11)
    z = Money(12.34, "EUR")
    print(z + 3.11 * x + y * 0.8)
    lst = [Money(10, "BYN"), Money(11), Money(12.01, "JPY")]
    print(sum(lst))

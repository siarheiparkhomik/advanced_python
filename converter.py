"""Module contains converter realization

"""
import json
import requests


class Converter(object):
    """Class that represents converter object

    """
    URL = "http://free.currencyconverterapi.com/"

    @classmethod
    def get_currencies_ratio(cls, from_currency, to_currency):
        """Return the ration of two specified currencies

        :param from_currency: the currency to convert from
        :param to_currency: the currency to convert to
        :return: currencies ratio
        """

        currencies = "{}_{}".format(from_currency, to_currency)
        request = "{}api/v5/convert?q={}&compact=ultra".format(cls.URL,
                                                               currencies)
        responce = requests.get(request)
        return json.loads(responce.text)[currencies]

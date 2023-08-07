import logging
import time
from json import JSONDecodeError

from test.api.base import Endpoint


class LondonWeather(Endpoint):
    # ---------------------------------------- Add Journey---------------------------------------------------
    @staticmethod
    def add_card(token, merchant, invalid_data=None):
        url = Endpoint.BASE_URL + api.ENDPOINT_WEATHER_API
        header = Endpoint.request_header(token)

        return Endpoint.call(url, header, "GET")

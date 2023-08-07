import logging
# import time
# from json import JSONDecodeError

from tests import api
from tests.api.base import Endpoint


class LondonWeather(Endpoint):
    @staticmethod
    def call_weather_api() -> str:
        url = Endpoint.BASE_URL + api.ENDPOINT_WEATHER_API
        logging.info(f"the url is", {url})
        header = Endpoint.request_header()
        return Endpoint.call(url, header, "GET")

from tests.api.base import Endpoint

from tests import api


class WeatherAPI:
    @staticmethod
    def call_weather_api():
        url = Endpoint.BASE_URL + api.ENDPOINT_WEATHER_API
        header = Endpoint.request_header()
        response = Endpoint.call(url, header, "GET")

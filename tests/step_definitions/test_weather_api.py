import datetime
import json
import logging
from json import JSONDecodeError

from pytest_bdd import given, parsers, scenarios, then, when

from tests import api
from tests.api.base import Endpoint
from tests.requests.get_weather import LondonWeather

scenarios("weather_api/")

"""Step definitions"""


@given(parsers.parse('I am Sample Weather API user'))
def sample_user_login():
    """No login is needed as calling the APi using the key generated via web
    Key is 7XG3DR5L6NP3QACLMW8FS55D4"""


@then(parsers.parse('I want to call the weather api to know the current weather'))
def check_weather_response() -> None:
    response = LondonWeather.call_weather_api()
    response_json = response_to_json(response)
    logging.info(
        "Current weather in London is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_WEATHER_API
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    assert (
            response.status_code == 200
            and response_json["address"] == "London,UK"
            and response_json["resolvedAddress"] == "London, England, United Kingdom"
        # and response_json["days"]["datetime"] == "curremt date/time"
    ), "Unable to fetch current weather in London"


def response_to_json(response):
    try:
        response_json = response.json()
    except JSONDecodeError or Exception:
        raise Exception(f"Empty response and the response Status Code is {str(response.status_code)}")
    return response_json

import datetime
import json
import logging
from pytest_bdd import given, parsers, scenarios, then, when



scenarios("weather_api/")


"""Step definitions - Add Journey """


@when(parsers.parse('I am Sample Weather API user'))
def sample_user_login():
    response = MembershipCards.add_card(TestContext.token, merchant)
    response_json = response_to_json(response)
    TestContext.current_scheme_account_id = response_json.get("id")
    logging.info(
        "The response of Add Journey (POST) is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    assert (
        response.status_code == 201
        and response_json["membership_plan"] == TestData.get_membership_plan_id(merchant)
        and response_json["payment_cards"] == []
        and response_json["membership_transactions"] == []
        and response_json["status"]["state"] == TestData.get_membership_card_status_states().get(constants.PENDING)
        and response_json["status"]["reason_codes"][0]
        == TestData.get_membership_card_status_reason_codes().get(constants.REASON_CODE_PENDING_ADD)
        and response_json["card"] is not None
        and response_json["images"] is not None
        and response_json["account"]["tier"] == 0
        and response_json["balances"] == []
    ), ("Add Journey for " + merchant + " failed")


@then(parsers.parse('I want to call the weather api to know the current weather'))
def check_weather_response():
    response = MembershipCards.add_ghost_card(TestContext.token, merchant)
    response_json = response_to_json(response)
    TestContext.current_scheme_account_id = response_json.get("id")
    logging.info(
        "The response of Add Ghost Journey (POST) is:"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    assert (
        response.status_code == 201
        and response_json["status"]["state"] == TestData.get_membership_card_status_states().get(constants.PENDING)
        and response_json["status"]["reason_codes"][0]
        == TestData.get_membership_card_status_reason_codes().get(constants.REASON_CODE_PENDING_ADD)
    ), ("Add Ghost Journey for " + merchant + " failed")


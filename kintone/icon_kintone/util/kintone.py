import requests
from logging import Logger
from komand.exceptions import PluginException
from json import JSONDecodeError


RECORD_ENDPOINT = "https://komand.kintone.com/k/v1/record.json"
APIS_ENDPOINT = "https://komand.kintone.com/k/v1/apis.json"


# This function is used for the connection test
def get_api_list(logger: Logger, api_key: str, verify_ssl: bool) -> dict:
    headers = {
        "X-Cybozu-API-Token": api_key
    }

    body = {
        "Content-Type": "application/json"
    }

    logger.info(f"Getting API List")
    logger.info(f"URL: {APIS_ENDPOINT}")

    response = requests.get(APIS_ENDPOINT, headers=headers, data=body, verify=verify_ssl)

    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        raise PluginException(cause="Request for APIs",
                              assistance="This is usually an invalid parameter, verify your API Key is correct",
                              data=e) from e

    try:
        output = response.json()
    except JSONDecodeError as e:
        raise PluginException(preset=PluginException.Preset.INVALID_JSON,
                              data=e) from e

    return output


def get_record(logger: Logger, api_key: str, app_id: str, record_id: str, verify_ssl: bool) -> dict:
    headers = {
        "X-Cybozu-API-Token": api_key
    }

    body = {
        "Content-Type": "application/json"
    }

    params = {
        "app": app_id,
        "id": record_id
    }

    logger.info(f"Getting record: {record_id} from application {app_id}")
    logger.info(f"URL: {RECORD_ENDPOINT}")

    response = requests.get(RECORD_ENDPOINT, params=params, headers=headers, data=body, verify=verify_ssl)

    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        raise PluginException(cause="Request for record failed",
                              assistance=f"This is usually an invalid parameter, make sure Record ID: {record_id} and "
                                         f"App ID: {app_id} exist.",
                              data=e)

    try:
        output = response.json().get("record")
    except Exception as e:
        raise PluginException(preset=PluginException.Preset.INVALID_JSON,
                              data=e)

    return output


def write_record(logger: Logger, api_key: str, app_id: str, record_body: object, verify_ssl: bool) -> dict:
    headers = {
        "X-Cybozu-API-Token": api_key,
        "Content-Type": "application/json"
    }

    body = {
        "app": app_id,
        "record": [record_body]
    }

    logger.info(f"Writing record: to application {app_id}")
    logger.info(f"URL: {RECORD_ENDPOINT}")

    logger.info(body)

    response = requests.post(RECORD_ENDPOINT, headers=headers, json=body, verify=verify_ssl)

    logger.info(f"Response Text:\n{response.text}")

    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        logger.error(f"Response Text:\n{response.text}")
        raise PluginException(cause="Write record failed",
                              assistance=f"This is usually an invalid parameter.\n"
                                         f"Verify the App ID: {app_id}\n"
                                         f"Verify the Record Body:\n{app_id}",
                              data=e)

    try:
        output = response.json()
    except Exception as e:
        raise PluginException(preset=PluginException.Preset.INVALID_JSON,
                              data=e)

    return output

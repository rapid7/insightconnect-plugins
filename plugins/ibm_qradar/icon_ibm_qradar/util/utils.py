import json

from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from requests import Response

from icon_ibm_qradar.util.constants.constant import (
    SUCCESS_RESPONSE_CODES,
)
from icon_ibm_qradar.util.constants.messages import INVALID_RANGE_FOUND
from icon_ibm_qradar.util.url import URL
from insightconnect_plugin_runtime.helper import clean


def prepare_request_params(
    params: {},
    logger,
    url_obj: URL,
    input_fields: list,
    query_params: dict = None,
):
    """Parse the common input provided including range, sort, filter and fields.

    :param params: Input Dict
    :param logger: Logging logger
    :param url_obj: URL object
    :param input_fields: Possible input fields for the action
    :param query_params: pre set query params
    :return:
    """
    if not query_params:
        query_params = {}

    headers = get_default_header()
    basic_url = url_obj.get_basic_url()

    for field in input_fields:
        query_value = params.get(field, "")

        if field == "range" and query_value != "":
            check, query_range = validate_query_range(query_value)
            if not check:
                logger.error(query_range)
                logger.info("Terminating: Query Range provided is invalid")
                raise PluginException(cause=INVALID_RANGE_FOUND)
            headers["Range"] = f"items={query_range}"
        else:
            if query_value != "":
                query_params[field] = query_value

    final_queries = []
    for key in query_params:
        final_queries.append(f"{key}={query_params[key]}")

    if len(final_queries) > 0:
        basic_url = f"{basic_url}?{'&'.join(final_queries)}"

    return basic_url, headers


def validate_query_range(query_range: str) -> (bool, str):
    """To validate the provided range for the output list.

    :param query_range: string representation of range
    :return: boolean
    """
    try:
        start, end = query_range.split("-")
        start = int(start.strip())
        end = int(end.strip())
        if start < 1:
            return False, "Start of range should be >= 1"
        if end < 1:
            return False, "End of range should be >= 1"

        return True, f"{start-1}-{end-1}"  # subtract by one as index always start with 0

    except ValueError as err:
        return False, err


def get_default_header() -> dict:
    """To get the default headers."""
    return {"Accept": "application/json"}


def delete_none(dict_):
    """To remove the key having none value in the dict.

    :param dict_: input dict.
    :return:
    """
    if isinstance(dict_, dict):
        for key, value in list(dict_.items()):
            if isinstance(value, dict):
                delete_none(value)
            elif value is None:
                del dict_[key]
            elif isinstance(value, list):
                for v_i in value:
                    delete_none(v_i)

    return dict_


def handle_response(response: Response) -> dict:
    """
    To handles the http response.

    :param response:
    :return:
    """
    try:
        response_data = response.json()
    except json.decoder.JSONDecodeError as err:
        raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=err)

    if response.status_code in SUCCESS_RESPONSE_CODES:
        return clean(response_data)

    if response.status_code == 401:
        raise ConnectionTestException(preset=PluginException.Preset.USERNAME_PASSWORD)
    if response.status_code == 403:
        raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
    if response.status_code == 429:
        raise PluginException(preset=PluginException.Preset.RATE_LIMIT, data=response.text)
    if response.status_code >= 500:
        raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)

    raise PluginException(cause=response_data["description"], assistance=response_data["message"])

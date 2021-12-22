"""Include util methods."""
import json
from insightconnect_plugin_runtime.exceptions import (
    ConnectionTestException,
    PluginException,
)

from icon_ibm_qradar.util.constants.constant import SUCCESS_RESPONSE_CODE


def get_default_header():
    """To get the default headers."""
    return {"Accept": "application/json"}


def handle_response(response):
    """
    To handles the http response.

    :param response:
    :return:
    """
    try:
        response_data = response.json()
    except json.decoder.JSONDecodeError as err:
        raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=err)

    if response.status_code in SUCCESS_RESPONSE_CODE:
        return {"data": response_data}

    if response.status_code == 401:
        raise ConnectionTestException(preset=ConnectionTestException.Preset.USERNAME_PASSWORD)
    if response.status_code >= 500:
        raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)
    raise PluginException(cause=response_data["description"])

from insightconnect_plugin_runtime.exceptions import PluginException
import requests


def raise_for_status(response: requests.Response):
    if response.status_code == 401:
        raise PluginException(
            cause="Invalid tenant ID, application ID or application secret provided.",
            assistance="Verify your connection inputs are correct and try again.",
            data=response.text,
        )
    elif response.status_code == 403:
        raise PluginException(
            preset=PluginException.Preset.UNAUTHORIZED,
            data=response.text,
        )
    elif response.status_code == 404:
        raise PluginException(
            cause="Resource not found.",
            assistance="Please provide valid inputs and try again.",
            data=response.text,
        )
    elif response.status_code == 400:
        raise PluginException(
            preset=PluginException.Preset.BAD_REQUEST,
            data=response.text,
        )
    elif response.status_code == 429:
        raise PluginException(
            preset=PluginException.Preset.RATE_LIMIT,
            data=response.text,
        )
    elif 400 < response.status_code < 500:
        raise PluginException(
            preset=PluginException.Preset.UNKNOWN,
            data=response.text,
        )
    elif response.status_code >= 500:
        raise PluginException(
            preset=PluginException.Preset.SERVER_ERROR,
            data=response.text,
        )

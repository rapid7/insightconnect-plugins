import github
import requests
from insightconnect_plugin_runtime.exceptions import PluginException

TIMEOUT = 60


def handle_gihub_exceptions(error: github.GithubException):
    if error.status == 403:
        raise PluginException(
            cause="Forbidden response returned from Github.",
            assistance="Account may need org permissions added.",
            data=error,
        )

    elif error.status == 404:
        raise PluginException(
            cause="Not Found response returned from Github.",
            assistance="The requested resource could not be found.",
            data=error,
        )

    else:
        raise PluginException(
            cause="Error occoured",
            assistance="Please check that the provided inputs are correct and try again.",
            data=error,
        )


def handle_http_exceptions(response):

    if 200 <= response.status_code <= 204:
        return

    elif response.status_code == 403:
        raise PluginException(
            cause="Forbidden response returned from Github.",
            assistance="Account may need org permissions added.",
            data=response.text,
        )

    elif response.status_code == 404:
        raise PluginException(
            cause="Not Found response returned from Github.",
            assistance="The requested resource could not be found.",
            data=response.text,
        )

    else:
        raise PluginException(
            cause="Error occoured.",
            assistance="Please check that the provided inputs are correct and try again.",
            data=response.text,
        )

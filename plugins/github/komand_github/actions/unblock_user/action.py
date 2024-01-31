import requests
import insightconnect_plugin_runtime
import urllib.parse

from komand_github.util.util import TIMEOUT, handle_http_exceptions
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_github.actions.unblock_user.schema import UnblockUserInput, UnblockUserOutput, Input, Output, Component


class UnblockUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="unblock_user",
            description=Component.DESCRIPTION,
            input=UnblockUserInput(),
            output=UnblockUserOutput(),
        )

    def run(self, params={}):
        username = urllib.parse.quote(params.get(Input.USERNAME))

        url = requests.compat.urljoin(self.connection.api_prefix, f"/user/blocks/{username}")

        headers = self.connection.auth_header
        headers["Accept"] = "application/vnd.github.giant-sentry-fist-preview+json"
        headers["Content-Type"] = "application/json"

        try:
            response = requests.delete(url=url, headers=headers, timeout=TIMEOUT)
            handle_http_exceptions(response)

            return {Output.SUCCESS: True}

        except Exception as error:
            if isinstance(error, PluginException):
                raise PluginException(cause=error.cause, assistance=error.assistance, data=error.data)
            else:
                raise PluginException(
                    cause="An error has occurred while trying to unblock a user.",
                    assistance="Please check that the provided inputs are correct and try again.",
                    data=error,
                )

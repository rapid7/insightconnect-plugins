import requests
import insightconnect_plugin_runtime
import urllib.parse

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_github.actions.block_user.schema import BlockUserInput, BlockUserOutput, Input, Output, Component


class BlockUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="block_user",
            description=Component.DESCRIPTION,
            input=BlockUserInput(),
            output=BlockUserOutput(),
        )

    def run(self, params={}):

        username = urllib.parse.quote(params.get(Input.USERNAME))

        url = requests.compat.urljoin(self.connection.api_prefix, f"/user/blocks/{username}")
        headers = self.connection.auth_header
        headers["Accept"] = "application/vnd.github.giant-sentry-fist-preview+json"
        headers["Content-Type"] = "application/json"

        try:
            response = requests.put(url=url, headers=headers, timeout=60)

            if response.status_code == 204:
                self.logger.info("Successfully blocked user")
                return {Output.SUCCESS: True}

            elif response.status_code == 404:
                raise PluginException(
                    cause=f"The user: {username}, could not be found",
                    assistance="Please check that the provided inputs are correct and try again.",
                )

            elif response.status_code == 422:
                raise PluginException(
                    cause=f"The user: {username}, has already been blocked",
                    assistance="Please check that the provided inputs are correct and try again.",
                )

            raise PluginException(
                cause="An error has occurred while trying to block a user",
                assistance="Please check that the provided inputs are correct and try again.",
            )

        except Exception as error:
            if isinstance(error, PluginException):
                raise PluginException(cause=error.cause, assistance=error.assistance)
            else:
                raise PluginException(
                    cause="An error has occurred while trying to block a user",
                    assistance="Please check that the provided inputs are correct and try again.",
                    data=error,
                )

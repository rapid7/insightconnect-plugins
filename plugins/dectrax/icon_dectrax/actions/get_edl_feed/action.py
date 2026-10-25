import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetEdlFeedInput, GetEdlFeedOutput, Input, Output, Component

# Custom imports below
import requests
from insightconnect_plugin_runtime.exceptions import PluginException


class GetEdlFeed(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_edl_feed",
            description=Component.DESCRIPTION,
            input=GetEdlFeedInput(),
            output=GetEdlFeedOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        # END INPUT BINDING - DO NOT REMOVE

        url = f"{self.connection.base_url}/api/v1/edl/attackers.txt"

        try:
            response = requests.get(
                url,
                headers=self.connection.headers,
                verify=self.connection.verify,
                timeout=15,
            )
            if response.status_code == 200:
                return {
                    Output.FEED_CONTENT: response.text,
                    Output.SUCCESS: True,
                }
            raise PluginException(
                cause=f"Failed to fetch EDL feed. HTTP status code: {response.status_code}.",
                assistance="Please verify that the EDL service is enabled on the DECTRAX instance.",
            )
        except requests.exceptions.RequestException as err:
            raise PluginException(
                cause=f"Network error downloading EDL feed: {err}",
                assistance="Check network connectivity and firewall rules.",
            )

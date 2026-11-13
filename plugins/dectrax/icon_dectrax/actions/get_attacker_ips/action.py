import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetAttackerIpsInput, GetAttackerIpsOutput, Input, Output, Component

# Custom imports below
import requests
from insightconnect_plugin_runtime.exceptions import PluginException


class GetAttackerIps(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_attacker_ips",
            description=Component.DESCRIPTION,
            input=GetAttackerIpsInput(),
            output=GetAttackerIpsOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        limit = params.get(Input.LIMIT, 100)
        # END INPUT BINDING - DO NOT REMOVE

        url = f"{self.connection.base_url}/api/v1/attackers"
        request_params = {"limit": limit} if limit else {}

        try:
            response = requests.get(
                url,
                params=request_params,
                headers=self.connection.headers,
                verify=self.connection.verify,
                timeout=15,
            )
            if response.status_code == 200:
                data = response.json()
                attackers = data.get("attackers", []) if isinstance(data, dict) else data
                if not isinstance(attackers, list):
                    attackers = []
                return {
                    Output.ATTACKERS: attackers,
                    Output.COUNT: len(attackers),
                }
            raise PluginException(
                cause=f"DECTRAX API returned status code {response.status_code}.",
                assistance="Please verify API credentials and instance health.",
            )
        except requests.exceptions.RequestException as err:
            raise PluginException(
                cause=f"Error connecting to DECTRAX API: {err}",
                assistance="Verify the instance hostname and network route.",
            )

import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import QueryTelemetryInput, QueryTelemetryOutput, Input, Output, Component

# Custom imports below
import requests
from insightconnect_plugin_runtime.exceptions import PluginException


class QueryTelemetry(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="query_telemetry",
            description=Component.DESCRIPTION,
            input=QueryTelemetryInput(),
            output=QueryTelemetryOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        ip = params.get(Input.IP)
        # END INPUT BINDING - DO NOT REMOVE

        url = f"{self.connection.base_url}/api/v1/telemetry/{ip}"

        try:
            response = requests.get(
                url,
                headers=self.connection.headers,
                verify=self.connection.verify,
                timeout=15,
            )
            if response.status_code == 200:
                data = response.json()
                events = data.get("events", [])
                protocols = list({ev.get("protocol") for ev in events if ev.get("protocol")})
                return {
                    Output.FOUND: bool(events),
                    Output.EVENTS_COUNT: len(events),
                    Output.PROTOCOLS: protocols,
                }
            elif response.status_code == 404:
                return {
                    Output.FOUND: False,
                    Output.EVENTS_COUNT: 0,
                    Output.PROTOCOLS: [],
                }
            raise PluginException(
                cause=f"DECTRAX API returned unexpected status code {response.status_code}.",
                assistance="Please verify your request parameters.",
            )
        except requests.exceptions.RequestException as err:
            raise PluginException(
                cause=f"Network error querying telemetry for IP {ip}: {err}",
                assistance="Check that DECTRAX is reachable.",
            )

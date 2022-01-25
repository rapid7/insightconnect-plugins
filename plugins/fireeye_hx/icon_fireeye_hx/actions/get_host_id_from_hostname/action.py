import komand
from .schema import (
    GetHostIdFromHostnameInput,
    GetHostIdFromHostnameOutput,
    Input,
    Output,
    Component,
)

# Custom imports below


class GetHostIdFromHostname(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_host_id_from_hostname",
            description=Component.DESCRIPTION,
            input=GetHostIdFromHostnameInput(),
            output=GetHostIdFromHostnameOutput(),
        )

    def run(self, params={}):
        response = self.connection.api.get_host_id_from_hostname({"search": params.get(Input.HOSTNAME)})
        entries = response.get("data", {}).get("entries", [])
        if entries and isinstance(entries, list):
            host_id = entries[0].get("_id")
            if host_id:
                return {Output.SUCCESS: True, Output.HOST_ID: host_id}
        return {Output.SUCCESS: False}

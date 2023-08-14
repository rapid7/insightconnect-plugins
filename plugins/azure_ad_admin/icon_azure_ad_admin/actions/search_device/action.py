import insightconnect_plugin_runtime
import requests
from insightconnect_plugin_runtime.helper import clean

from .schema import SearchDeviceInput, SearchDeviceOutput, Input, Output, Component

# Custom imports below
from ...util.api_utils import raise_for_status
from ...util.constants import Endpoint


class SearchDevice(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_device",
            description=Component.DESCRIPTION,
            input=SearchDeviceInput(),
            output=SearchDeviceOutput(),
        )

    # TODO: Przeniesc do api (?) i dodac obsluge bledow
    def run(self, params={}):
        url = Endpoint.DEVICES.format(self.connection.tenant)
        headers = self.connection.get_headers(self.connection.get_auth_token())
        search = params.get(Input.SEARCH)
        select = params.get(Input.SELECT)
        headers["ConsistencyLevel"] = "eventual"
        search_params = {
            "$search": f'"{search}"' if search else "",
            "$filter": params.get(Input.FILTER),
            "$orderBy": params.get(Input.ORDERBY),
            "$select": ", ".join(select) if select else [],
            "$count": "true",
        }
        response = requests.request(method="GET", url=url, params=clean(search_params), headers=headers)
        raise_for_status(response)
        devices = response.json().get("value", [])
        return {Output.DEVICES: clean(devices)}

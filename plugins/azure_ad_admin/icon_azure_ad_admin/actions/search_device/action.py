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

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        filter_ = params.get(Input.FILTER, "")
        order_by = params.get(Input.ORDERBY, "")
        search = params.get(Input.SEARCH, "")
        select = params.get(Input.SELECT, [])
        # END INPUT BINDING - DO NOT REMOVE

        # Get headers with authentication token
        headers = self.connection.get_headers(self.connection.get_auth_token())
        headers["ConsistencyLevel"] = "eventual"

        # Prepare search parameters
        search_params = {
            "$search": f'"{search}"' if search else "",
            "$filter": filter_,
            "$orderBy": order_by,
            "$select": ", ".join(select) if select else [],
            "$count": "true",
        }

        # Configure initial URL
        url = Endpoint.DEVICES.format(self.connection.tenant)

        # Limit to 1,000 iterations to avoid infinite loops (which gives total of max 100 000 devices)
        devices, total_devices = [], 0
        for _ in range(1_000):
            response = requests.request(
                method="GET",
                url=url,
                params=clean(search_params) if url == Endpoint.DEVICES.format(self.connection.tenant) else None,
                headers=headers,
            )
            raise_for_status(response)
            response_data = response.json()
            devices.extend(response_data.get("value", []))

            # Check for next page
            if not (url := response_data.get("@odata.nextLink")):
                self.logger.info("No more pages found. Ending pagination.")
                break

            # Parse total count if available
            if "@odata.count" in response_data:
                total_devices = response_data.get("@odata.count", 0)

            if total_devices:
                self.logger.info(
                    f"The next page of results has been found. Fetched {len(devices)} out of {total_devices} devices so far."
                )
        self.logger.info(f"Found total of {len(devices)} devices matching the criteria.")
        return {Output.DEVICES: clean(devices)}

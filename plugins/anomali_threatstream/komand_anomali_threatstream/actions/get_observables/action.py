import komand
from .schema import GetObservablesInput, GetObservablesOutput, Component

# Custom imports below
import logging
from requests.exceptions import ConnectionError
from copy import copy
from json import JSONDecodeError
from komand.exceptions import PluginException
from komand_anomali_threatstream.util.utils import hide_api_key


class GetObservables(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_observables",
            description=Component.DESCRIPTION,
            input=GetObservablesInput(),
            output=GetObservablesOutput(),
        )

    def run(self, params={}):
        # Copy and update the base request to avoid mutating the original
        self.request = copy(self.connection.request)
        self.request.url, self.request.method = self.request.url + "/intelligence", "GET"

        # Pagination flag and results placeholder
        self.continue_paging, self.results = True, list()
        # Update the request with the supplied domain, page size, and offset
        self.request.params.update({"value": "{value}".format(value=params.get("value")), "limit": 1000, "offset": 0})

        while self.continue_paging:
            try:
                response = self.connection.session.send(self.request.prepare(), verify=self.request.verify)
            except ConnectionError as e:
                raise PluginException(
                    cause=f"The following ConnectionError was raised: {hide_api_key(str(e))}",
                    assistance="Please verify your ThreatStream server status and try again. "
                    "If the issue persists please contact support."
                ) from ConnectionError  # Suppresses the exception context from the original error that exposes API key

            if response.status_code not in range(200, 299):
                raise PluginException(
                    cause="Received %d HTTP status code from ThreatStream." % response.status_code,
                    assistance="Please verify your ThreatStream server status and try again. "
                    "If the issue persists please contact support. "
                    "Server response was: %s" % response.text,
                )
            try:
                response_data = response.json()
            except JSONDecodeError:
                raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)

            try:
                # Check pagination indicator. A "null" value means no more pages.
                if not response_data["meta"]["next"]:
                    self.continue_paging = False
            except KeyError:
                raise PluginException(
                    cause="The output did not contain expected keys.",
                    assistance="Contact support for help.",
                    data=response_data,
                )

            self.request.params["offset"] += 1000
            self.results.extend(response_data["objects"])

        self.results = komand.helper.clean(self.results)
        return {"results": self.results}

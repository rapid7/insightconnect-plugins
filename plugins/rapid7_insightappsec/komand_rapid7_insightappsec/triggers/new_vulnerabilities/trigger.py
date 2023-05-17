import insightconnect_plugin_runtime
import time
from .schema import NewVulnerabilitiesInput, NewVulnerabilitiesOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper
from komand_rapid7_insightappsec.util.endpoints import Search
from komand_rapid7_insightappsec.util.helpers import clean, convert_dict_keys_to_camel_case
from datetime import datetime, timedelta, timezone
import json


class NewVulnerabilities(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="new_vulnerabilities",
            description=Component.DESCRIPTION,
            input=NewVulnerabilitiesInput(),
            output=NewVulnerabilitiesOutput(),
        )

    def run(self, params={}):
        interval = params.get(Input.FREQUENCY)
        request = ResourceHelper(self.connection.session, self.logger)
        now = self.get_current_time()
        get_from = now - timedelta(hours=interval)
        parameters = {"size": 1000}

        while True:
            json_data = {
                "query": f"vulnerability.first_discovered BETWEEN '{get_from.isoformat()}' AND '{now.isoformat()}'",
                "type": "VULNERABILITY",
            }
            new_vulnerabilities = []

            # get all pages
            for index in range(9999):
                parameters["index"] = index
                response = json.loads(
                    request.resource_request(
                        Search.search(self.connection.url), "POST", params=parameters, payload=json_data
                    ).get("resource")
                )
                vulnerabilities = response.get("data", [])
                if not vulnerabilities:
                    break
                new_vulnerabilities.extend(vulnerabilities)

            if new_vulnerabilities:
                self.send({Output.VULNERABILITIES: convert_dict_keys_to_camel_case(clean(new_vulnerabilities))})
            time.sleep(interval * 3600)
            get_from = now
            now = self.get_current_time()

    @staticmethod
    def get_current_time():
        return datetime.now(timezone.utc)

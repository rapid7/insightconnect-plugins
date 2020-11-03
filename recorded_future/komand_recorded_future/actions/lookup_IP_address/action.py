import komand
from .schema import LookupIPAddressInput, LookupIPAddressOutput, Input
from komand.exceptions import PluginException
import requests
import json


class LookupIPAddress(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="lookup_IP_address",
            description="This action is used to query for data related to a specific IP address",
            input=LookupIPAddressInput(),
            output=LookupIPAddressOutput(),
        )

    def run(self, params={}):
        try:
            ip_address = params.get(Input.IP_ADDRESS)
            comment = params.get(Input.COMMENT)

            query_params = {
                "fields": ",".join([
                    "analystNotes",
                    "counts",
                    "enterpriseLists",
                    "entity",
                    "intelCard",
                    "metrics",
                    "relatedEntities",
                    "risk",
                    "sightings",
                    "threatLists",
                    "timestamps",
                    "location",
                    "riskyCIDRIPs"
                ])
            }

            if comment and len(comment):
                query_params["comment"] = comment

            # move to raw, API was unable to handle error data returned
            headers = self.connection.headers
            resp = requests.get(
                f"https://api.recordedfuture.com/v2/ip/{ip_address}",
                params=query_params,
                headers=headers,
            )
            data = resp.json()

            # IP Not found
            if data.get("error", {}).get("message", "") == "Not found":
                self.logger.error("Error: " + json.dumps(data.get("error")))
                self.logger.error(f"IP {ip_address} not found")
                return {"found": False}

            if data.get("error", False):
                self.logger.error("Error:" + json.dumps(data.get("error")))
                return {"found": False}

            data["data"]["found"] = True
            return komand.helper.clean(data["data"])

        except Exception as e:
            if isinstance(e, dict):
                raise PluginException(cause=("Error: ", json.dumps(e)))

            raise PluginException(cause=f"Error: {e}")

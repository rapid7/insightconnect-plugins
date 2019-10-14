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
            fields = params.get(Input.FIELDS)
            comment = params.get(Input.COMMENT)

            if not len(fields):
                fields = None

            if not len(comment):
                comment = None
            # move to raw, API was unable to handle error data returned
            qparams = {"fields": ",".join(fields), "comment": comment}
            headers = {"X-RFToken": self.connection.token}
            resp = requests.get(
                f"https://api.recordedfuture.com/v2/ip/{ip_address}",
                params=qparams,
                headers=headers,
            )
            data = resp.json()

            if data.get("warnings", False):
                self.logger.info(
                    'Option for fields are: ["sightings","threatLists","analystNotes","counts","entity","hashAlgorithm","intelCard","metrics", "relatedEntities" ,"risk" ,"timestamps"]'
                )

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
                raise PluginException(cause=(f"Error: ", json.dumps(e)))

            raise PluginException(cause=f"Error: {e}")

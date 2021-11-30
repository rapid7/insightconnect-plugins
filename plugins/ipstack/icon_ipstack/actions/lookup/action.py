import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import LookupInput, LookupOutput

# Custom imports below
import json


class Lookup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="lookup",
            description="Lookup IPStack Information for a Host",
            input=LookupInput(),
            output=LookupOutput(),
        )

    def run(self, params={}):
        token = self.connection.token
        url = "http://api.ipstack.com/" + params["host"] + "?access_key=" + token + "&output=json"
        resp = insightconnect_plugin_runtime.helper.open_url(url)
        dic = json.loads(resp.read())

        # Rename key to fit schema and catch if there is no ip found
        # bad requests seem to never contain ip in the response
        try:
            dic["address"] = dic.pop("ip")
        except KeyError:
            raise PluginException(cause=f"Request lookup for {params['host']} failed",
                                  assistance="Check the input host domain and data in this error",
                                  data=dic)
        # Change types to conform to schema: int -> str
        dic["latitude"] = str(dic.get("latitude"))
        dic["longitude"] = str(dic.get("longitude"))

        results = insightconnect_plugin_runtime.helper.clean_dict(dic)
        return results

    def test(self, params={}):
        return {}

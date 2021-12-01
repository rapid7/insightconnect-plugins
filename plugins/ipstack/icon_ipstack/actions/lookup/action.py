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
            # check to see if unauthorized or just bad req, if cant categorize into either of these return generic
            if "error" in dic:
                code = dic["error"].get("code")
                if code == 404:
                    raise PluginException(
                        cause="The requested resource does not exist, Error 404",
                        assistance="Check if your plugin can be updated, if not contact support",
                        data=dic,
                    )
                elif code == 101:
                    raise PluginException(
                        cause="The access key is blank or invalid",
                        assistance="Check the API key as input to the connection",
                        data=dic,
                    )
                elif code == 102:
                    raise PluginException(
                        cause="The access key was recognized but the user account is not active",
                        assistance="Contact ipstack support",
                        data=dic,
                    )
                elif code == 104:
                    raise PluginException(
                        cause="The maximum monthly ip lookups has been hit",
                        assistance="Contact ipstack to increase limit",
                        data=dic,
                    )
                elif code == 106:
                    raise PluginException(
                        cause="The supplied host address/domain is invalid",
                        assistance="Check the host input field for this action",
                        data=dic,
                    )

            raise PluginException(
                cause=f"Request lookup for {params['host']} failed for unknown reason",
                assistance="Check the input host domain and data in this error",
                data=dic,
            )
        # Change types to conform to schema: int -> str
        dic["latitude"] = str(dic.get("latitude"))
        dic["longitude"] = str(dic.get("longitude"))

        results = insightconnect_plugin_runtime.helper.clean_dict(dic)
        return results

    def test(self, params={}):  # pylint: disable=unused-argument
        return {}

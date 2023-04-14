import insightconnect_plugin_runtime
from .schema import GetZonesInput, GetZonesOutput, Input, Output, Component

# Custom imports below
from icon_cloudflare.util.helpers import clean, convert_dict_keys_to_camel_case
from icon_cloudflare.util.constants import order_by


class GetZones(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="getZones", description=Component.DESCRIPTION, input=GetZonesInput(), output=GetZonesOutput()
        )

    def run(self, params={}):
        status = params.get(Input.STATUS)
        parameters = {
            "match": params.get(Input.MATCH),
            "name": params.get(Input.NAME),
            "account.name": params.get(Input.ACCOUNTNAME),
            "account.id": params.get(Input.ACCOUNTID),
            "status": status if status != "all" else None,
            "page": params.get(Input.PAGE),
            "per_page": params.get(Input.PERPAGE),
            "order": order_by.get(params.get(Input.ORDER)),
            "direction": params.get(Input.DIRECTION),
        }
        return {
            Output.ZONES: convert_dict_keys_to_camel_case(
                self.connection.api_client.get_zones(clean(parameters)).get("result", [])
            )
        }

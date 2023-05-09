import insightconnect_plugin_runtime
from .schema import UpdateBlacklistZonesInput, UpdateBlacklistZonesOutput, Input, Output, Component

# Custom imports below
import validators
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_okta.util.helpers import clean


class UpdateBlacklistZones(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_blacklist_zones",
            description=Component.DESCRIPTION,
            input=UpdateBlacklistZonesInput(),
            output=UpdateBlacklistZonesOutput(),
        )

    def run(self, params={}):  # noqa: C901
        name = params.get(Input.NAME)
        value = params.get(Input.ADDRESS)

        if validators.ipv4_cidr(value) or validators.ipv6_cidr(value):
            value_type = "CIDR"
        else:
            value_type = "RANGE"

        searched_zone = None
        for zone in self.connection.api_client.get_zones():
            if zone.get("name") == name:
                searched_zone = zone
                break

        if not searched_zone:
            raise PluginException(
                cause=f"Name {name} does not exist in Okta zones.",
                assistance="Please enter valid zone name and try again.",
            )

        if searched_zone.get("type") == "DYNAMIC":
            raise PluginException(
                cause=f"Cannot perform operation on {value} because the provided zone '{name}' is of dynamic type.",
                assistance="To perform the requested operation, the specified zone must be of IP type. Please check if "
                "the given zone name is correct and try again.",
            )

        zone_id = searched_zone.get("id")
        gateways = searched_zone.get("gateways", [])
        if params.get(Input.BLACKLISTSTATE):
            for gateway in gateways:
                if self.check_value(gateway, value):
                    raise PluginException(
                        cause=f"The address {value} already exist in provided Okta zone {name}.",
                        assistance="Please enter an address that is not in the blacklist zone.",
                    )

            gateways.append({"type": value_type, "value": value})
            searched_zone["gateways"] = gateways
        else:
            new_gateways = []
            for gateway in gateways:
                if not self.check_value(gateway, value):
                    new_gateways.append(gateway)

            if len(new_gateways) != len(gateways):
                searched_zone["gateways"] = new_gateways
            else:
                raise PluginException(
                    cause=f"The address {value} does not exist in provided Okta zone {name}.",
                    assistance="Please enter an address that is blacklisted and try again.",
                )
        response = self.connection.api_client.update_zone(zone_id, searched_zone)
        response["links"] = response.pop("_links")
        return {Output.ZONE: clean(response)}

    @staticmethod
    def check_value(gateway: dict, value: str) -> bool:
        return gateway.get("value") == value or gateway.get("value").replace(" ", "") == f"{value}-{value}"

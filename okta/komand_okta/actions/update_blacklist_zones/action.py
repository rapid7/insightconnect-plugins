import komand
from .schema import UpdateBlacklistZonesInput, UpdateBlacklistZonesOutput, Input, Output, Component
# Custom imports below
import validators
import requests
from komand.exceptions import PluginException


class UpdateBlacklistZones(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='update_blacklist_zones',
            description=Component.DESCRIPTION,
            input=UpdateBlacklistZonesInput(),
            output=UpdateBlacklistZonesOutput())

    def run(self, params={}):
        name = params.get(Input.NAME)
        value = params.get(Input.ADDRESS)

        if validators.ipv4_cidr(value) or validators.ipv6_cidr(value):
            value_type = "CIDR"
        else:
            value_type = "RANGE"

        url = requests.compat.urljoin(
            self.connection.okta_url,
            '/api/v1/zones'
        )

        response = self.connection.session.get(url)
        zones = response.json()
        zone = None
        for search_zone in zones:
            if search_zone.get("name") == name:
                zone = search_zone
                break

        if not zone:
            raise PluginException(cause=f"Name {name} does not exist in Okta zones. ",
                                  assistance="Please enter valid zone name and try again.")

        zone_id = zone.get("id")
        gateways = zone.get("gateways", [])
        if params.get(Input.BLACKLIST_STATE):
            for gateway in gateways:
                if self.check_value(gateway, value):
                    raise PluginException(cause=f"The address {value} already exist in provided Okta zone {name}.",
                                          assistance="Please enter valid address and try again.")

            gateways.append({
                "type": value_type,
                "value": value
            })
            zone["gateways"] = gateways

            update_url = requests.compat.urljoin(
                self.connection.okta_url,
                f'/api/v1/zones/{zone_id}'
            )
        else:
            new_gateways = []
            for gateway in gateways:
                if self.check_value(gateway, value):
                    continue

                new_gateways.append(gateway)

            if len(new_gateways) == len(gateways):
                raise PluginException(
                    cause=f"The address {value} does not exist in provided Okta zone {name}.",
                    assistance="Please enter valid address and try again."
                )
            else:
                update_url = requests.compat.urljoin(
                    self.connection.okta_url,
                    f'/api/v1/zones/{zone_id}'
                )
                zone["gateways"] = new_gateways

        response = self.connection.session.put(update_url, json=zone)
        if response.status_code < 200 or response.status_code >= 400:
            raise PluginException(
                preset=PluginException.Preset.SERVER_ERROR,
                data=response.text
            )

        return {
            Output.SUCCESS: True,
            Output.ZONE_LIST: komand.helper.clean(response.json())
        }

    @staticmethod
    def check_value(gateway: dict, value: str):
        return gateway.get("value") == value or gateway.get("value").replace(" ", "") == f"{value}-{value}"

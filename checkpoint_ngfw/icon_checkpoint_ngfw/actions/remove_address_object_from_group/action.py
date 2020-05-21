import komand
from .schema import RemoveAddressObjectFromGroupInput, RemoveAddressObjectFromGroupOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException


class RemoveAddressObjectFromGroup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='remove_address_object_from_group',
                description=Component.DESCRIPTION,
                input=RemoveAddressObjectFromGroupInput(),
                output=RemoveAddressObjectFromGroupOutput())

    def run(self, params={}):
        url = f"{self.connection.server_and_port}/web_api/set-group"

        group_name = params.get(Input.GROUP)
        address_name = params.get(Input.ADDRESS_OBJECT)
        discard_other_changes = params.get(Input.DISCARD_OTHER_SESSIONS)

        payload = {
            "name": group_name,
            "members": {
                "remove": address_name
            }
        }

        headers = self.connection.get_headers()

        response = self.connection.post_and_publish(headers, discard_other_changes, payload, url)
        if response.status_code == 200:
            return {Output.SUCCESS}
        elif response.status_code in [400, 401, 403, 404, 409, 500, 501]:
            raise PluginException(cause=response["errors"]["message"],
                                  assistance="Remediate the issue noted in the error message above and try again.",
                                  data=response.text)

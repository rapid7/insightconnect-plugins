import json

import komand
from komand.exceptions import PluginException

from .schema import AddComputerToGroupInput, AddComputerToGroupOutput, Input, Output, Component
# Custom imports below


class AddComputerToGroup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_computer_to_group',
                description=Component.DESCRIPTION,
                input=AddComputerToGroupInput(),
                output=AddComputerToGroupOutput())

    def run(self, params={}):
        base_url = self.connection.base_url
        computer_group_id = params.get(Input.ID)
        computer_ids = params.get(Input.COMPUTER_IDS)
        endpoint = f'/JSSResource/computergroups/id/{computer_group_id}'
        url = f'{base_url}/{endpoint}'
        computer_id_payload = ""

        headers = {
                "Accept": "application/xml"
            }

        for c_id in computer_ids:
            computer_id_payload = f'<computer><id>{c_id}</id></computer>' + computer_id_payload

        payload = f'<computer_group><computer_additions>{computer_id_payload}</computer_additions></computer_group>'

        result = self.connection.session.put(url, auth=self.connection.session.auth,
                                             headers=headers, data=payload)

        if result.status_code != 201:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=result.text)

        return {
            Output.STATUS: result.status_code
        }

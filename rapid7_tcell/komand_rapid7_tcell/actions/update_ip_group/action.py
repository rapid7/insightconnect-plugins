import komand
from .schema import UpdateIpGroupInput, UpdateIpGroupOutput
# Custom imports below
from komand.helper import clean


class UpdateIpGroup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_ip_group',
                description='Upload new items for an IP address group',
                input=UpdateIpGroupInput(),
                output=UpdateIpGroupOutput())

    def run(self, params={}):
        group_name = params.get('group_name')
        items = params.get('items')
        result = self.connection.api.update_ip_group(group_name, items)

        output = {
            'id': result.get('result').get('id'),
            'message': result.get('result').get('message')
        }

        return clean(output)

    def test(self):
        return {}

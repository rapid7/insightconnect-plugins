import komand
from .schema import CreateIpGroupInput, CreateIpGroupOutput
# Custom imports below


class CreateIpGroup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_ip_group',
                description='Upload an IP address group definition to tCell',
                input=CreateIpGroupInput(),
                output=CreateIpGroupOutput())

    def run(self, params={}):
        group = params.get('group')
        result = self.connection.api.create_ip_group(group)
        return {'id': result.get('result').get('id')}

    def test(self):
        return {}

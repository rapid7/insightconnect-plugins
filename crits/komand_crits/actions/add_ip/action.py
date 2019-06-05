import komand
from .schema import AddIpInput, AddIpOutput
# Custom imports below
from komand_crits.util import utils


class AddIp(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_ip',
                description='Creates a new IP',
                input=AddIpInput(),
                output=AddIpOutput())

    def run(self, params={}):
        response = self.connection.crits.add_ip(
            ip=params['ip'],
            type_=params['type'],
            source=params['source']
        )
        return {'response': utils.make_response(response)}

    def test(self):
        """TODO: Test action"""
        return {}

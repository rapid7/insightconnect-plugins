import komand
from .schema import AddCampaignInput, AddCampaignOutput
# Custom imports below
from komand_crits.util import utils


class AddCampaign(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_campaign',
                description='Creates a new campaign',
                input=AddCampaignInput(),
                output=AddCampaignOutput())

    def run(self, params={}):
        response = self.connection.crits.add_campaign(
            name=params['name'],
            params=params['params']
        )
        return {'response': utils.make_response(response)}

    def test(self):
        """TODO: Test action"""
        return {}

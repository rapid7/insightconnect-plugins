import komand
from .schema import SetStatusOfInvestigationActionInput, SetStatusOfInvestigationActionOutput, Component, Input, Output
from komand.exceptions import PluginException
# Custom imports below
from komand_rapid7_insightidr.util.endpoints import Investigations
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
import json


class SetStatusOfInvestigationAction(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='set_status_of_investigation_action',
                description=Component.DESCRIPTION,
                input=SetStatusOfInvestigationActionInput(),
                output=SetStatusOfInvestigationActionOutput())

    def run(self, params={}):
        idr_id = params.get(Input.ID)
        status = params.get(Input.STATUS)
        request = ResourceHelper(self.connection.session, self.logger)

        endpoint = Investigations.set_the_status_of_an_investigation(self.connection.url, idr_id, status)
        response = request.resource_request(endpoint, 'put')

        try:
            result = json.loads(response['resource'])
        except json.decoder.JSONDecodeError:
            self.logger.error(f'InsightIDR response: {response}')
            raise PluginException(cause='The response from InsightIDR was not in the correct format.',
                                  assistance='Contact support for help. See log for more details')
        try:
            return {Output.INVESTIGATION: result}
        except KeyError:
            self.logger.error(result)
            raise PluginException(cause='The response from InsightIDR was not in the correct format.',
                                  assistance='Contact support for help. See log for more details')

import komand
from .schema import ListInvestigationsInput, ListInvestigationsOutput, Component, Output
from komand.exceptions import PluginException
# Custom imports below
from komand_rapid7_insightidr.util.endpoints import Investigations
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
import json


class ListInvestigations(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_investigations',
                description=Component.DESCRIPTION,
                input=ListInvestigationsInput(),
                output=ListInvestigationsOutput())

    def run(self, params={}):
        rest_params = {}
        for key in params:
            if params[key]:
                rest_params[key] = params[key]
        if not rest_params.get('statuses'):
            raise PluginException(cause='The statuses parameter cannot be blank.',
                                  assistance='choose a statues parameter, and please report this bug to support.')
        if rest_params.get('statuses') == 'EITHER':
            del rest_params['statuses']

        request = ResourceHelper(self.connection.session, self.logger)

        endpoint = Investigations.list_investigations(self.connection.url)
        response = request.resource_request(endpoint, 'get', params=rest_params)

        try:
            result = json.loads(response['resource'])
        except json.decoder.JSONDecodeError:
            self.logger.error(f'InsightIDR response: {response}')
            raise PluginException(cause='The response from InsightIDR was not in the correct format.',
                                  assistance='Contact support for help. See log for more details')
        try:
            investigations = result['data']
            metadata = result['metadata']
            return {Output.INVESTIGATIONS: investigations, Output.METADATA: metadata}
        except KeyError:
            self.logger.error(result)
            raise PluginException(cause='The response from InsightIDR was not in the correct format.',
                                  assistance='Contact support for help. See log for more details')

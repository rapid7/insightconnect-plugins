import komand
from .schema import CreateExceptionInput, CreateExceptionOutput, Component
# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_helper import ResourceHelper


class CreateException(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_exception',
                description=Component.DESCRIPTION,
                input=CreateExceptionInput(),
                output=CreateExceptionOutput())

    def run(self, params={}):
        resource_helper = ResourceHelper(self.connection.session, self.logger)
        payload = {}
        scope = {}
        submit = {}
        scope['id'] = params.get('scope')
        scope['type'] = params.get('type')
        if scope['type'] == 'Instance':
            if params.get('key', '') != '':
                scope['key'] = params.get('key')
            if params.get('port', 0) != 0:
                scope['port'] = params.get('port')
        scope['vulnerability'] = params.get('vulnerability')
        submit['reason'] = params.get('reason', 'Other')
        submit['comment'] = params.get('comment', 'Created with InsightConnect')

        payload['scope'] = scope
        payload['submit'] = submit
        payload['expires'] = params.get('expiration', '')
        if payload['expires'] == '':
            payload.pop('expires', None)
        payload['state'] = 'Under Review'

        endpoint = endpoints.VulnerabilityException.vulnerability_exceptions(self.connection.console_url)
        response = resource_helper.resource_request(endpoint=endpoint, method='post', payload=payload)
        return response

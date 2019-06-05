import komand
from .schema import FindEventInput, FindEventOutput, Output
# Custom imports below
import requests


class FindEvent(komand.Action):

    # URI for Find Event
    _URI = '/integrationServices/v3/event/'

    def __init__(self):
        super(self.__class__, self).__init__(
                name='find_event',
                description='Retrieves all events matching the input search criteria. Response is a list of events in JSON format. Resulting events are sorted in descending order of time',
                input=FindEventInput(),
                output=FindEventOutput())

    def run(self, params={}):
        host = self.connection.host
        token = self.connection.token
        connector = self.connection.connector
        payload = dict()
        for param in params:
            if params[param]:
                payload[param] = params[param]
        self.logger.info(payload)
        headers = {'X-Auth-Token': f'{token}/{connector}'}
        url = host + FindEvent._URI

        if payload:
            result = requests.get(url, headers=headers, params=payload)
        else:
            result = requests.get(url, headers=headers)
        try:
            data = komand.helper.clean(result.json())
        except ValueError:
            self.logger.error(result.text)
            raise Exception(f'Error: Received an unexpected response'
                            f' (non-JSON or no response was received). Raw response in logs.')
        if result.status_code == 200:
            return {Output.SUCCESS: data['success'], Output.LATESTTIME: data['latestTime'],
                    Output.RESULTS: data['results'], Output.ELAPSED: data['elapsed'],
                    Output.MESSAGE: data['message'], Output.TOTALRESULTS: data['totalResults']}
        if result.status_code in range(400, 499):
            raise Exception(f'Carbon Black returned a {result.status_code} code.'
                            f' Verify the token and host configuration in the connection. Response was: {result.text}')
        if result.status_code in range(500, 599):
            raise Exception(f'Carbon Black returned a {result.status_code} code.'
                            f' If the problem persists please contact support for help. Response was: {result.text}')
        self.logger.error(result.text)
        raise Exception(f'An unknown error occurred.'
                        f' Carbon Black returned a {result.status_code} code. Contact support for help. Raw response in logs.')

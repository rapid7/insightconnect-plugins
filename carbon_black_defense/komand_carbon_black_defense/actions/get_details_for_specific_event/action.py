import komand
from .schema import GetDetailsForSpecificEventInput, GetDetailsForSpecificEventOutput, Input, Output
# Custom imports below
import requests


class GetDetailsForSpecificEvent(komand.Action):

    # URI for Get Details
    _URI = '/integrationServices/v3/event/'

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_details_for_specific_event',
                description='Retrieve details for an individual event given the event ID',
                input=GetDetailsForSpecificEventInput(),
                output=GetDetailsForSpecificEventOutput())

    def run(self, params={}):
        host = self.connection.host
        token = self.connection.token
        connector = self.connection.connector
        event_id = params.get(Input.EVENT_ID)

        headers = {'X-Auth-Token': f'{token}/{connector}'}
        url = host + GetDetailsForSpecificEvent._URI + event_id

        result = requests.get(url, headers=headers)
        try:
            data = komand.helper.clean(result.json())
        except ValueError:
            self.logger.error(result.text)
            raise Exception(f'Error: Received an unexpected response'
                            f' (non-JSON or no response was received). Raw response in logs.')
        if result.status_code == 200:
            return {Output.SUCCESS: data['success'], Output.MESSAGE: data['message'], Output.EVENTINFO: data['eventInfo']}
        if result.status_code in range(400, 499):
            raise Exception(f'Carbon Black returned a {result.status_code} code.'
                            f' Verify the token and host configuration in the connection. Response was: {result.text}')
        if result.status_code in range(500, 599):
            raise Exception(f'Carbon Black returned a {result.status_code} code.'
                            f' If the problem persists please contact support for help. Response was: {result.text}')
        self.logger.error(result.text)
        raise Exception(f'An unknown error occurred.'
                        f' Carbon Black returned a {result.status_code} code. Contact support for help. Raw response in logs.')

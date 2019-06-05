import komand
import time
from .schema import GetNotificationsInput, GetNotificationsOutput, Input
# Custom imports below
import requests


class GetNotifications(komand.Trigger):

    # Notification URI
    _URI = '/integrationServices/v3/notification'

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_notifications',
                description='Allows consumers to get alert and policy action notifications that a connector is subscribed to. Only API keys of type "SIEM" can call the notifications API',
                input=GetNotificationsInput(),
                output=GetNotificationsOutput())

    def run(self, params={}):
        host = self.connection.host
        token = self.connection.token
        connector = self.connection.connector
        url = host + GetNotifications._URI
        headers = {'X-Auth-Token': f'{token}/{connector}'}

        while True:
            result = requests.get(url, headers=headers)
            try:
                data = komand.helper.clean(result.json())
            except ValueError:
                self.logger.error(result.text)
                raise Exception(f'Error: Received an unexpected response'
                                f' (non-JSON or no response was received). Raw response in logs.')
            if 'notifications' in data and len(data['notifications']) > 0:
                self.send({'notifications': data['notifications'], 'message': data['message'], 'success': data['success']})
            time.sleep(params.get(Input.FREQUENCY))

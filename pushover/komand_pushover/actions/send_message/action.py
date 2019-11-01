import komand
from .schema import SendMessageInput, SendMessageOutput
# Custom imports below
import requests
import json
from komand.exceptions import PluginException


class SendMessage(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='send_message',
                description='Send a pushover notification to a user or group.',
                input=SendMessageInput(),
                output=SendMessageOutput())

    def run(self, params={}):
        headers = {'Content-Type': 'application/json'}
        params['token'] = self.connection.token

        priorities = {
                        'Lowest': -2,
                        'Low': -1,
                        'Normal': 0,
                        'High': 1,
                        'Emergency': 2
                        }
        params['priority'] = priorities[params.get('priority','Normal')]

        if(params.get('priority', 0) == 2):
            if(params.get('retry', 0) < 30):
                self.logger.info("SendMessage: retry interval too short - setting to 30 seconds")
                params['retry'] = 30
            if(params.get('expire', 0) == 0):
                self.logger.info("SendMessage: emergency priority set but expiry not defined, setting expiry to 1 hour")
                params['expiry'] = 3600
        else:
            params.pop('retry', None)
            params.pop('expire', None)

        if(params.get('timestamp', '000').startswith("000")):
            params.pop('timestamp', None)

        res = requests.post(self.connection.api_url, data=json.dumps(params), headers=headers)
        if(res.status_code != 200):
            raise PluginException(preset=PluginException.Preset.UNKNOWN)
        try:
            return res.json()
        except json.decoder.JSONDecodeError:
            raise ConnectionTestException(preset=PluginException.Preset.INVALID_JSON, data=res.text)

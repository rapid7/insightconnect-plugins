import time

import insightconnect_plugin_runtime

# Custom imports below
import requests
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import GetNotificationsInput, GetNotificationsOutput, Input


class GetNotifications(insightconnect_plugin_runtime.Trigger):

    # Notification URI
    _URI = "/integrationServices/v3/notification"

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_notifications",
            description='Allows consumers to get alert and policy action notifications that a connector is subscribed to. Only API keys of type "SIEM" can call the notifications API',
            input=GetNotificationsInput(),
            output=GetNotificationsOutput(),
        )

    def run(self, params={}):
        host = self.connection.host
        token = self.connection.token
        connector = self.connection.connector
        url = host + GetNotifications._URI
        headers = {"X-Auth-Token": f"{token}/{connector}"}

        while True:
            result = requests.get(url, headers=headers)
            try:
                data = insightconnect_plugin_runtime.helper.clean(result.json())
            except ValueError:
                self.logger.error(result.text)
                raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=result.text)
            if "notifications" in data and len(data["notifications"]) > 0:
                self.send(
                    {
                        "notifications": data["notifications"],
                        "message": data["message"],
                        "success": data["success"],
                    }
                )
            time.sleep(params.get(Input.FREQUENCY))

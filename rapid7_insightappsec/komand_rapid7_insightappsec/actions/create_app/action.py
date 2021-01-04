import insightconnect_plugin_runtime
from .schema import CreateAppInput, CreateAppOutput, Input, Output, Component
# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import Apps
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper
from insightconnect_plugin_runtime.exceptions import PluginException
import json

class CreateApp(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_app',
                description=Component.DESCRIPTION,
                input=CreateAppInput(),
                output=CreateAppOutput())

    def run(self, params={}):
        # TODO: Implement run function
        app_name = params.get(Input.APP_NAME)
        app_description = params.get(Input.APP_DESCRIPTION)
        request = ResourceHelper(self.connection.session, self.logger)

        url = Apps.create_app(self.connection.url)
        payload = {'name': app_name, 'description': app_description}

        response = request.resource_request(url, 'post', payload=payload)
        uuid = response.get("headers")
        uuid = uuid.get("Location")
        parts = uuid.split('/')
        app_id = parts[-1]
        return {Output.APP_ID:app_id}

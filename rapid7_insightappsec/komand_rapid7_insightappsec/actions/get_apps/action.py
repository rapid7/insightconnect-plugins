import insightconnect_plugin_runtime
from .schema import GetAppsInput, GetAppsOutput, Input, Output, Component
# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import Apps
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper
import json
from insightconnect_plugin_runtime.exceptions import PluginException

class GetApps(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_apps',
                description=Component.DESCRIPTION,
                input=GetAppsInput(),
                output=GetAppsOutput())

    def run(self, params={}):
        # TODO: Implement run function
        sort = params.get(Input.SORT)
        index = params.get(Input.INDEX)
        size = params.get(Input.SIZE)
        resource_helper = ResourceHelper(self.connection.session, self.logger)
        endpoint = Apps.get_apps(self.connection.url)
        response = resource_helper.resource_request(endpoint, method="GET", params={"sort":sort, "index":index, "size":size})
        try:
            response = json.loads(response["resource"])
        except (json.decoder.JSONDecodeError, TypeError, KeyError):
            self.logger.error(f'InsightAppSec response: {response}')
            raise PluginException(cause=PluginException.Preset.INVALID_JSON, assistance=PluginException.Preset.INVALID_JSON)
        try:
            metadata = response['metadata']
            data = response['data']
            links = response['links']
        except KeyError:
            self.logger.error(f'InsightAppSec response: {response}')
            raise PluginException(cause=PluginException.Preset.INVALID_JSON, assistance=PluginException.Preset.INVALID_JSON)
        return {Output.METADATA:metadata, Output.DATA:data, Output.LINKS:links}

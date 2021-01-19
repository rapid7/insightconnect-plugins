import insightconnect_plugin_runtime
from .schema import GetScanConfigsInput, GetScanConfigsOutput, Input, Output
# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import ScanConfig
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper
from insightconnect_plugin_runtime.exceptions import PluginException
import json


class GetScanConfigs(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_scan_configs',
                description='Get a page of scan configurations, based on supplied pagination parameters',
                input=GetScanConfigsInput(),
                output=GetScanConfigsOutput())

    def run(self, params={}):
        sort = params.get(Input.SORT)
        index = params.get(Input.INDEX)
        size = params.get(Input.SIZE)
        include_errors = params.get(Input.INCLUDEERRORS)
        resource_helper = ResourceHelper(self.connection.session, self.logger)
        endpoint = ScanConfig.scan_config(self.connection.url)
        response = resource_helper.resource_request(endpoint, method="GET", params={"sort":sort, "index":index, "size":size, "include-errors":include_errors})
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

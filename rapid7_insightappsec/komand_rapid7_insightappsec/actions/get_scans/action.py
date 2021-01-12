import insightconnect_plugin_runtime
from .schema import GetScansInput, GetScansOutput, Input, Output
# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import Scans
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper
from insightconnect_plugin_runtime.exceptions import PluginException
import json


class GetScans(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_scans',
                description='Get a page of scans, based on supplied pagination parameters',
                input=GetScansInput(),
                output=GetScansOutput())

    def run(self, params={}):
        sort = params.get(Input.SORT)
        index = params.get(Input.INDEX)
        size = params.get(Input.SIZE)
        resource_helper = ResourceHelper(self.connection.session, self.logger)
        endpoint = Scans.scans(self.connection.url)
        response = resource_helper.resource_request(endpoint, method="GET", params={"sort":sort, "index":index, "size":size})
        try:
            response = json.loads(response["resource"])
        except json.decoder.JSONDecodeError:
            self.logger.error(f'InsightAppSec response: {response}')
            raise PluginException(cause='The response from InsightAppSec was not in JSON format.', assistance='Contact support for help.'
                            ' See log for more details')
        try:
            metadata = response['metadata']
            data = response['data']
            links = response['links']
        except KeyError:
            self.logger.error(f'InsightAppSec response: {response}')
            raise PluginException(cause='The response from InsightAppSec was malformed.', assistance='Contact support for help.'
                            ' See log for more details')
        return {Output.METADATA:metadata, Output.DATA:data, Output.LINKS:links}

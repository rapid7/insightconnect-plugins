import insightconnect_plugin_runtime
from .schema import GetTagAssetsInput, GetTagAssetsOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class GetTagAssets(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_tag_assets",
            description="Tag ID for which to retrieve asset associations",
            input=GetTagAssetsInput(),
            output=GetTagAssetsOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        tag_id = params.get("id")
        endpoint = endpoints.Tag.tag_assets(self.connection.console_url, tag_id)
        self.logger.info("Using %s ..." % endpoint)

        response = resource_helper.resource_request(endpoint=endpoint)

        if "resources" in response:
            return {"assets": response["resources"]}
        else:
            return {"assets": []}

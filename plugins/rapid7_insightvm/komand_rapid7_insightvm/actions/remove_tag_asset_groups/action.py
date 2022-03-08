import insightconnect_plugin_runtime
from .schema import RemoveTagAssetGroupsInput, RemoveTagAssetGroupsOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class RemoveTagAssetGroups(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="remove_tag_asset_groups",
            description="Removes all asset group associations from a tag",
            input=RemoveTagAssetGroupsInput(),
            output=RemoveTagAssetGroupsOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        tag_id = params.get("id")
        endpoint = endpoints.Tag.tag_asset_groups(self.connection.console_url, tag_id)
        self.logger.info("Using %s ..." % endpoint)

        response = resource_helper.resource_request(endpoint=endpoint, method="delete")

        return response

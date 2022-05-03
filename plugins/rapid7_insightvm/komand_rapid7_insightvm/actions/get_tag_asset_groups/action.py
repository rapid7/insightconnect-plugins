import insightconnect_plugin_runtime
from .schema import GetTagAssetGroupsInput, GetTagAssetGroupsOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class GetTagAssetGroups(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_tag_asset_groups",
            description="Get asset groups associated with a tag",
            input=GetTagAssetGroupsInput(),
            output=GetTagAssetGroupsOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        tag_id = params.get("id")
        endpoint = endpoints.Tag.tag_asset_groups(self.connection.console_url, tag_id)
        self.logger.info(f"Using {endpoint}")

        response = resource_helper.resource_request(endpoint=endpoint)

        if "resources" in response:
            return {"asset_group_ids": response["resources"]}
        else:
            return {"asset_group_ids": []}

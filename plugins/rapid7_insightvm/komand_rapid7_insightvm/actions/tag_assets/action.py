import insightconnect_plugin_runtime
from .schema import TagAssetsInput, TagAssetsOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class TagAssets(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="tag_assets", description=Component.DESCRIPTION, input=TagAssetsInput(), output=TagAssetsOutput()
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger, self.connection.ssl_verify)
        asset_ids = params.get(Input.ASSET_IDS)
        tag_id = params.get(Input.TAG_ID)
        tag_name = params.get(Input.TAG_NAME)
        tag_type = params.get(Input.TAG_TYPE)
        tag_source = params.get(Input.TAG_SOURCE)

        # Allows output from 'Get Tag' to be used (as action requires uppercase and V3 returns lower). Issue with V3 API
        tag_source = tag_source.upper() if tag_source.lower() != "built-in" else tag_source

        tag = {
            "attributes": [{"tag_attribute_name": "SOURCE", "tag_attribute_value": tag_source}],
            "tag_name": tag_name,
            "tag_config": {"tag_associated_asset_ids": asset_ids},
            "tag_type": tag_type,
        }

        endpoint = endpoints.Asset.tag_assets(self.connection.console_url, tag_id)
        self.logger.info(f"Using {endpoint}")

        resource_helper.resource_request(endpoint=endpoint, method="put", payload=tag, json_response=False)

        return {Output.SUCCESS: True}

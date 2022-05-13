import json

import insightconnect_plugin_runtime
from .schema import TagAssetsInput, TagAssetsOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests

class TagAssets(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='tag_assets',
                description=Component.DESCRIPTION,
                input=TagAssetsInput(),
                output=TagAssetsOutput())

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        asset_ids = params.get(Input.ASSET_IDS)
        tag_id = params.get(Input.TAG_ID)
        tag_name = params.get(Input.TAG_NAME)
        tag_type = params.get(Input.TAG_TYPE)
        tag_source = params.get(Input.TAG_SOURCE)

        tag_payload = {}
        tag_payload['tag_name'] = tag_name
        tag_payload['tag_type'] = tag_type
        tag_payload['tag_id'] = tag_id
        tag_payload['attributes'] = []
        tag_payload['attributes'].append({})
        tag_payload['attributes'][0]['tag_attribute_name'] = 'SOURCE'
        tag_payload['attributes'][0]['tag_attribute_value'] = tag_source.upper()
        tag_payload['tag_config'] = {}
        tag_payload['tag_config']['tag_associated_asset_ids'] = []
        tag_payload['tag_config']['tag_group_ids'] = []
        tag_payload['tag_config']['site_ids'] = []
        tag_payload['tag_config']['search_criteria'] = None
        for asset in asset_ids:
            tag_payload['tag_config']['tag_associated_asset_ids'].append(asset)

        endpoint = endpoints.Asset.tag_assets(self.connection.console_url, tag_id)
        self.logger.info(f"Using {endpoint}")

        response = resource_helper.resource_request(endpoint=endpoint, method="put", payload=tag_payload)

        return response

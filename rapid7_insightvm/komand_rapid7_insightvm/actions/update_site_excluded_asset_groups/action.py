import komand
from .schema import UpdateSiteExcludedAssetGroupsInput, UpdateSiteExcludedAssetGroupsOutput, Input
# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class UpdateSiteExcludedAssetGroups(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_site_excluded_asset_groups',
                description='Update an existing site scope of excluded asset groups',
                input=UpdateSiteExcludedAssetGroupsInput(),
                output=UpdateSiteExcludedAssetGroupsOutput())

    def run(self, params={}):
        scope = params.get(Input.EXCLUDED_ASSET_GROUPS)
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        endpoint = endpoints.Site.site_excluded_asset_groups(self.connection.console_url, params.get(Input.ID))

        # Pull current site scope in order to append to list instead of overwriting
        if not params.get(Input.OVERWRITE):
            current_scope = resource_helper.resource_request(endpoint=endpoint,
                                                             method='get')
            current_asset_group_ids = [group['id'] for group in current_scope['resources']]
            self.logger.info(f"Appending to current list of excluded asset groups")
            scope.extend(current_asset_group_ids)

        self.logger.info(f"Using {endpoint} ...")
        response = resource_helper.resource_request(endpoint=endpoint,
                                                    method='put',
                                                    payload=scope)

        return {
            "id": params.get(Input.ID),
            "links": response['links']
        }

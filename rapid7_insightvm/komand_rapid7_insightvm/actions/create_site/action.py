import komand
from .schema import CreateSiteInput, CreateSiteOutput
# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_helper import ResourceHelper


class CreateSite(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_site',
                description='Create a new site',
                input=CreateSiteInput(),
                output=CreateSiteOutput())

    def run(self, params={}):
        resource_helper = ResourceHelper(self.connection.session, self.logger)
        endpoint = endpoints.Site.sites(self.connection.console_url)
        self.logger.info(f"Using {endpoint} ...")

        payload = params
        # Construct Scan Scope for site
        assets = {
            "includedTargets": {"addresses": params['included_addresses']},
            "excludedTargets": {"addresses": params['excluded_addresses']},
            "includedAssetGroups": {"assetGroupIDs": params['included_asset_groups']},
            "excludedAssetGroups": {"assetGroupIDs": params['excluded_asset_groups']}
        }
        scan_scope = {"assets": assets}
        payload['scan'] = scan_scope

        delete_keys = ['excluded_addresses', 'excluded_asset_groups', 'included_addresses',
                       'included_asset_groups']

        for k in list(payload.keys()):
            if k in delete_keys:
                del(payload[k])

        self.logger.info(f"Sending Payload: {payload}")
        response = resource_helper.resource_request(endpoint=endpoint, method='post', payload=payload)

        return response

import komand
from .schema import GetAssetGroupsInput, GetAssetGroupsOutput

# Custom imports below
import re
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class GetAssetGroups(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_asset_groups",
            description="Get a list of asset groups",
            input=GetAssetGroupsInput(),
            output=GetAssetGroupsOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        name = params.get("name")

        endpoint = endpoints.AssetGroup.asset_groups(self.connection.console_url)
        self.logger.info("Using %s ..." % endpoint)

        groups = resource_helper.paged_resource_request(endpoint=endpoint)

        if name == "":
            name = None

        if name:
            regex = re.compile(name, re.IGNORECASE)
            filtered_groups = []
            for g in groups:
                if regex.match(g["name"]):
                    filtered_groups.append(g)
            self.logger.info("Returning %d asset groups based on filters..." % (len(filtered_groups)))
            groups = filtered_groups

        return {"asset_groups": groups}

import komand
from .schema import CreateAssetGroupInput, CreateAssetGroupOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class CreateAssetGroup(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_asset_group",
            description="Create an asset group",
            input=CreateAssetGroupInput(),
            output=CreateAssetGroupOutput(),
        )

    def run(self, params={}):

        # Remove the searchCriteria if not defined
        if params.get("searchCriteria") == {}:
            params.pop("searchCriteria")

        resource_helper = ResourceRequests(self.connection.session, self.logger)
        self.logger.info("Creating asset group with name %s and type %s" % (params["name"], params["type"]))
        endpoint = endpoints.AssetGroup.asset_groups(self.connection.console_url)

        response = resource_helper.resource_request(endpoint=endpoint, method="post", payload=params)

        return {"id": response["id"]}

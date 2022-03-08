import insightconnect_plugin_runtime
from .schema import CreateTagInput, CreateTagOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class CreateTag(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_tag",
            description="Create a new tag",
            input=CreateTagInput(),
            output=CreateTagOutput(),
        )

    def run(self, params={}):

        # Remove the searchCriteria if not defined
        if params.get("searchCriteria") == {}:
            params.pop("searchCriteria")

        resource_helper = ResourceRequests(self.connection.session, self.logger)
        self.logger.info("Creating tag with name %s and type %s" % (params["name"], params["type"]))
        endpoint = endpoints.Tag.tags(self.connection.console_url)

        response = resource_helper.resource_request(endpoint=endpoint, method="post", payload=params)

        return {"id": response["id"]}

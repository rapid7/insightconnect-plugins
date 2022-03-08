import insightconnect_plugin_runtime
from .schema import GetTagInput, GetTagOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class GetTag(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_tag",
            description="Get tag details by tag ID",
            input=GetTagInput(),
            output=GetTagOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        tag_id = params.get("id")
        endpoint = endpoints.Tag.tags(self.connection.console_url, tag_id)
        self.logger.info("Using %s ..." % endpoint)
        tag = resource_helper.resource_request(endpoint)

        return {"tag": tag}

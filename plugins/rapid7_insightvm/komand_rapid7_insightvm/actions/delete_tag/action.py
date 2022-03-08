import insightconnect_plugin_runtime
from .schema import DeleteTagInput, DeleteTagOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class DeleteTag(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_tag",
            description="Deletes an existing tag",
            input=DeleteTagInput(),
            output=DeleteTagOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        tag_id = params.get("id")
        self.logger.info("Deleting tag ID %d" % tag_id)
        endpoint = endpoints.Tag.tags(self.connection.console_url, tag_id)

        response = resource_helper.resource_request(endpoint=endpoint, method="delete")

        return response

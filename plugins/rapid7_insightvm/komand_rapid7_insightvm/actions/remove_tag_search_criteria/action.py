import insightconnect_plugin_runtime
from .schema import RemoveTagSearchCriteriaInput, RemoveTagSearchCriteriaOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class RemoveTagSearchCriteria(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="remove_tag_search_criteria",
            description="Removes all search criteria from a tag",
            input=RemoveTagSearchCriteriaInput(),
            output=RemoveTagSearchCriteriaOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        tag_id = params.get("id")
        endpoint = endpoints.Tag.tag_search_criteria(self.connection.console_url, tag_id)
        self.logger.info(f"Using {endpoint}")

        response = resource_helper.resource_request(endpoint=endpoint, method="delete")

        return response

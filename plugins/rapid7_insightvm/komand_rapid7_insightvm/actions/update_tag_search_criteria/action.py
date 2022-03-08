import insightconnect_plugin_runtime
from .schema import UpdateTagSearchCriteriaInput, UpdateTagSearchCriteriaOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class UpdateTagSearchCriteria(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_tag_search_criteria",
            description="Update an existing tag",
            input=UpdateTagSearchCriteriaInput(),
            output=UpdateTagSearchCriteriaOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        tag_id = params.get("id")
        search_criteria = params.get("searchCriteria")
        endpoint = endpoints.Tag.tag_search_criteria(self.connection.console_url, tag_id)
        self.logger.info("Using %s ..." % endpoint)

        response = resource_helper.resource_request(endpoint=endpoint, method="put", payload=search_criteria)

        return response

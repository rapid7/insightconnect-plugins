import insightconnect_plugin_runtime
from .schema import GetTagsInput, GetTagsOutput

# Custom imports below
import re
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class GetTags(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_tags",
            description="Get a listing of all tags and return their details",
            input=GetTagsInput(),
            output=GetTagsOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        tag_name = params.get("name")
        tag_type = params.get("type")

        endpoint = endpoints.Tag.tags(self.connection.console_url)
        self.logger.info("Using %s ..." % endpoint)

        tags = resource_helper.paged_resource_request(endpoint=endpoint)

        if tag_name == "":
            tag_name = None
        if tag_type == "":
            tag_type = None

        if tag_name or tag_type:
            regex = re.compile(tag_name, re.IGNORECASE)
            filtered_tags = []
            for t in tags:
                if tag_name and tag_type:
                    if (regex.match(t["name"])) and (t["type"] == tag_type):
                        filtered_tags.append(t)
                else:
                    if (regex.match(t["name"])) or (t["type"] == tag_type):
                        filtered_tags.append(t)
            self.logger.info("Returning %d tags based on filters..." % (len(filtered_tags)))
            tags = filtered_tags

        return {"tags": tags}

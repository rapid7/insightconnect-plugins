import insightconnect_plugin_runtime
from .schema import GetTagDetailsInput, GetTagDetailsOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from greynoise.exceptions import RateLimitError, RequestFailure


class GetTagDetails(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_tag_details",
            description=Component.DESCRIPTION,
            input=GetTagDetailsInput(),
            output=GetTagDetailsOutput(),
        )

    def run(self, params={}):
        tag_name = params.get(Input.TAG_NAME)
        output = {}
        try:
            resp = self.connection.gn_client.tags(name=tag_name)
            tags = resp.get("tags") if isinstance(resp, dict) else None
            wanted = (tag_name or "").lower()
            for tag in tags or []:
                if isinstance(tag, dict) and str(tag.get("name", "")).lower() == wanted:
                    output = tag
                    break
        except RateLimitError as error:
            raise PluginException(
                cause="GreyNoise API rate limit exceeded.",
                assistance="Wait and try again.",
                data=str(error),
            )

        except RequestFailure as error:
            raise PluginException(
                cause=f"API responded with ERROR: {error.args[0]} - {error.args[1]}.",
                assistance="Please check error and try again.",
            )

        if not output:
            output = {"name": tag_name, "description": "Tag Not Found"}

        return {
            Output.CATEGORY: output.get("category"),
            Output.CREATED_AT: output.get("created_at"),
            Output.CVES: output.get("cves"),
            Output.DESCRIPTION: output.get("description"),
            Output.ID: output.get("id"),
            Output.INTENTION: output.get("intention"),
            Output.LABEL: output.get("label"),
            Output.NAME: output.get("name"),
            Output.RECOMMEND_BLOCK: output.get("recommend_block"),
            Output.REFERENCES: output.get("references"),
            Output.RELATED_TAGS: output.get("related_tags"),
            Output.SLUG: output.get("slug"),
        }

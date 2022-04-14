import insightconnect_plugin_runtime
from .schema import FindGroupsInput, FindGroupsOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_mimecast.util.constants import DATA_FIELD


class FindGroups(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="find_groups",
            description=Component.DESCRIPTION,
            input=FindGroupsInput(),
            output=FindGroupsOutput(),
        )

    def run(self, params={}):
        query = params.get(Input.QUERY)
        source = params.get(Input.SOURCE)
        if query:
            data = {"query": query, "source": source}
        else:
            data = {"source": source}
        response = self.connection.client.find_groups(data)

        try:
            output = response[DATA_FIELD][0]["folders"]
        except KeyError:
            self.logger.error(response)
            raise PluginException(
                cause="Unexpected output format.",
                assistance="The output from Mimecast was not in the expected format. Please contact support for help.",
                data=response,
            )

        return {Output.GROUPS: output}

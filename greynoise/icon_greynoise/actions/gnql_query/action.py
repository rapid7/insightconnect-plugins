import insightconnect_plugin_runtime
from .schema import GnqlQueryInput, GnqlQueryOutput, Input, Component

# Custom imports below
from greynoise.exceptions import RequestFailure
from insightconnect_plugin_runtime.exceptions import PluginException


class GnqlQuery(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="gnql_query", description=Component.DESCRIPTION, input=GnqlQueryInput(), output=GnqlQueryOutput()
        )

    def run(self, params={}):
        query = params.get(Input.QUERY)
        size = params.get(Input.SIZE)
        if size and size.isdigit():
            if int(size) < 0 or int(size) > 10000:
                raise PluginException(
                    cause="Invalid Size Input Provided", assistance="Size must be a valid integer between 1 and 10000"
                )
        try:
            resp = self.connection.gn_client.query(query, size=size)

        except RequestFailure as e:
            raise PluginException(
                cause="Received HTTP %d status code from GreyNoise. Verify your input and try again." % e.args[0],
                assistance="If the issue persists please contact support.",
                data=f"{e.args[0]}, {e.args[1]['message']}",
            )

        return resp

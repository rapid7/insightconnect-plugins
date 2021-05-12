import insightconnect_plugin_runtime
from .schema import GnqlQueryInput, GnqlQueryOutput, Input, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_greynoise.util.util import GNRequestFailure
from greynoise.exceptions import RequestFailure


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
                    cause="Invalid Size Input Provided.", assistance="Size must be a valid integer between 1 and 10000."
                )
        try:
            resp = self.connection.gn_client.query(query, size=size)

        except RequestFailure as e:
            raise GNRequestFailure(e.args[0], e.args[1])

        return resp

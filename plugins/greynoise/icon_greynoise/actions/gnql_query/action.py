import insightconnect_plugin_runtime
from .schema import GnqlQueryInput, GnqlQueryOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from greynoise.exceptions import RateLimitError, RequestFailure


def _omit_none(value):
    if isinstance(value, dict):
        return {key: _omit_none(item) for key, item in value.items() if item is not None}
    if isinstance(value, list):
        return [_omit_none(item) for item in value if item is not None]
    return value


class GnqlQuery(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="gnql_query", description=Component.DESCRIPTION, input=GnqlQueryInput(), output=GnqlQueryOutput()
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        query = params.get(Input.QUERY)
        size = params.get(Input.SIZE)
        scroll = params.get(Input.SCROLL)
        # END INPUT BINDING - DO NOT REMOVE

        if size and str(size).isdigit():
            if int(size) < 0 or int(size) > 10000:
                raise PluginException(
                    cause="Invalid Size Input Provided.", assistance="Size must be a valid integer between 1 and 10000."
                )
        try:
            resp = self.connection.gn_client.query(query, size=size or None, scroll=scroll or None)

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

        if not isinstance(resp, dict):
            resp = {}
        data = resp.get("data")
        results = [_omit_none(item) for item in data if isinstance(item, dict)] if isinstance(data, list) else []
        output = {Output.DATA: results}
        metadata = resp.get("request_metadata")
        if isinstance(metadata, dict):
            output[Output.REQUEST_METADATA] = _omit_none(metadata)
        return output

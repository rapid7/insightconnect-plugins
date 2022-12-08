import insightconnect_plugin_runtime
from .schema import GetIocsByFilterInput, GetIocsByFilterOutput, Input, Output, Component

# Custom imports below
from icon_rapid7_intsights.util.api import IOCParams
from insightconnect_plugin_runtime.helper import clean

class GetIocsByFilter(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_iocs_by_filter',
                description=Component.DESCRIPTION,
                input=GetIocsByFilterInput(),
                output=GetIocsByFilterOutput())

    def run(self, params={}):
        ioc_params = IOCParams(
            last_updated_from=params.get(Input.LAST_UPDATED_FROM),
            last_updated_to=params.get(Input.LAST_UPDATED_TO),
            last_seen_from=params.get(Input.LAST_SEEN_FROM),
            last_seen_to=params.get(Input.LAST_SEEN_TO),
            first_seen_from=params.get(Input.FIRST_SEEN_FROM),
            first_seen_to=params.get(Input.FIRST_SEEN_TO),
            status=params.get(Input.STATUS),
            type=params.get(Input.TYPE),
            severity=params.get(Input.SEVERITY),
            source_ids=params.get(Input.SOURCE_IDS),
            kill_chain_phases=params.get(Input.KILL_CHAIN_PHASES),
            limit=params.get(Input.LIMIT),
            offset=params.get(Input.OFFSET),
        )
        response = self.connection.client.get_indicators_by_filter(ioc_params)
        return clean({Output.CONTENT: response.get("content"), Output.NEXTOFFSET: response.get("nextOffset")})

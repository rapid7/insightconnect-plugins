import insightconnect_plugin_runtime
from .schema import QuarantineInput, QuarantineOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_rapid7_insight_agent.util.graphql_api.api_exception import APIException


class Quarantine(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='quarantine',
                description=Component.DESCRIPTION,
                input=QuarantineInput(),
                output=QuarantineOutput())

    def run(self, params={}):
        agent_id = params.get(Input.AGENT_ID)
        advertisement_period = params.get(Input.INTERVAL)
        quarantine_state = params.get(Input.QUARANTINE_STATE)

        try:
            if quarantine_state:
                success = self.connection.api.quarantine(advertisement_period, agent_id)
            else:
                success = self.connection.api.unquarantine(agent_id)
        except APIException as e:
            raise PluginException(cause=e.cause,
                                  assistance=e.assistance,
                                  data=e.data)

        return {Output.SUCCESS: success}

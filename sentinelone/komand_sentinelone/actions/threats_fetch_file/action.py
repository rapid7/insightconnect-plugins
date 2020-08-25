import komand
from .schema import ThreatsFetchFileInput, ThreatsFetchFileOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException


class ThreatsFetchFile(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='threats_fetch_file',
                description=Component.DESCRIPTION,
                input=ThreatsFetchFileInput(),
                output=ThreatsFetchFileOutput())

    def run(self, params={}):
        agent_filter = params.get(Input.FILTER, None)
        password = params.get(Input.PASSWORD)
        if "ids" not in agent_filter and "groupIds" not in agent_filter and "filterId" not in agent_filter:
            self.logger.error("One of the following filter arguments must be supplied - ids, groupIds, filterId")
            raise PluginException(
                cause="Wrong filter parameter",
                assistance="One of the following filter arguments must be supplied - ids, groupIds, filterId"
            )

        if len(password) <= 10 or " " in password:
            raise PluginException(
                cause="Wrong password",
                assistance="Password must have more than 10 characters and cannot contain whitespace"
            )

        return {
            Output.AFFECTED: self.connection.threats_fetch_file(
                params.get(Input.PASSWORD),
                agent_filter
            ).get("data", {}).get("affected", 0)
        }

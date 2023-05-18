import insightconnect_plugin_runtime
from .schema import (
    GetSuspiciousListInput,
    GetSuspiciousListOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import json


class GetSuspiciousList(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_suspicious_list",
            description=Component.DESCRIPTION,
            input=GetSuspiciousListInput(),
            output=GetSuspiciousListOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        new_suspicions = []
        # Make Action API Call
        self.logger.info("Making API Call...")
        try:
            client.consume_suspicious_list(
                lambda suspicion: new_suspicions.append(suspicion.dict())
            )
        except Exception as e:
            raise PluginException(
                cause="An error occurred while getting the Suspicious List.",
                assistance="Please check the logs for more details.",
                data=e,
            )
        # Load json objects to list
        suspicious_objects = []
        for i in new_suspicions:
            i["description"] = "" if not i["description"] else i["description"]
            i = json.dumps(i)
            suspicious_objects.append(json.loads(i))
        # Return results
        self.logger.info("Returning Results...")
        return {Output.SUSPICIOUS_OBJECTS: suspicious_objects}

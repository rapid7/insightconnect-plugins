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

    def run(self, params={}):  # pylint: disable=unused-argument
        # Get Connection Client
        client = self.connection.client
        new_suspicions = []
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.object.consume_suspicious(lambda suspicion: new_suspicions.append(suspicion.model_dump()))
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while getting the Suspicious List.",
                assistance="Please check the logs for more details.",
                data=response.error,
            )
        # Load json objects to list
        suspicious_objects = []
        for new_suspicion in new_suspicions:
            new_suspicion["description"] = "" if not new_suspicion["description"] else new_suspicion["description"]
            new_suspicion = json.dumps(new_suspicion)
            suspicious_objects.append(json.loads(new_suspicion))
        # Return results
        self.logger.info("Returning Results...")
        return {Output.SUSPICIOUS_OBJECTS: suspicious_objects}

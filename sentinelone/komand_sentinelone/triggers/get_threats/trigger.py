import insightconnect_plugin_runtime
import time
from .schema import GetThreatsInput, GetThreatsOutput, Input, Output

# Custom imports below
from datetime import datetime


class GetThreats(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_threats", description="Get threats", input=GetThreatsInput(), output=GetThreatsOutput()
        )

    def run(self, params={}):
        self.logger.info("Get Threats: trigger started")

        frequency = params.get("frequency", 5)

        trigger_params = {
            "resolved": params.get(Input.RESOLVED),
            "classifications": params.get(Input.CLASSIFICATIONS),
            "agentIsActive": params.get(Input.AGENT_IS_ACTIVE, True),
            "engines": params.get(Input.ENGINES),
            "limit": 1,
        }

        since = datetime.now()

        while True:
            if since:
                trigger_params["createdAt__gt"] = since

            response = self.connection.get_threats(trigger_params)

            while response["data"]:
                self.send_first_threat(response["data"])
                cursor = response["pagination"]["nextCursor"]
                if cursor:
                    response = self.connection.get_threats({"cursor": cursor, "limit": 1})
                else:
                    break

            since = datetime.now()
            time.sleep(frequency)

    def send_first_threat(self, data):
        threat = data[0]
        self.logger.info("Threat found: " + threat["id"])
        self.send({Output.THREAT: insightconnect_plugin_runtime.helper.clean(threat)})

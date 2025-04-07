import insightconnect_plugin_runtime
import time

from .schema import GetThreatsInput, GetThreatsOutput, Input, Output, Component

# Custom imports below
from datetime import datetime
from komand_sentinelone.util.helper import clean


class GetThreats(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_threats",
            description=Component.DESCRIPTION,
            input=GetThreatsInput(),
            output=GetThreatsOutput(),
        )

    def run(self, params={}):
        self.logger.info("Get Threats: trigger started")

        frequency = params.get("frequency", 5)

        trigger_params = {
            "resolved": params.get(Input.RESOLVED),
            "classifications": ",".join(params.get(Input.CLASSIFICATIONS)),
            "agentIsActive": params.get(Input.AGENTISACTIVE, True),
            "engines": params.get(Input.ENGINES),
            "limit": 1,
        }
        since = datetime.now()
        while True:
            trigger_params["createdAt__gt"] = since
            trigger_params["cursor"] = None

            response = self.connection.client.get_threats(trigger_params)
            while response.get("data", [{}]):
                self.send_threat(response.get("data", [{}])[0])
                cursor = response.get("pagination", {}).get("nextCursor")
                if cursor:
                    trigger_params["cursor"] = cursor
                    response = self.connection.client.get_threats(trigger_params)
                else:
                    break

            since = datetime.now()
            time.sleep(frequency)

    def send_threat(self, threat: dict):
        self.logger.info(f"Threat found: {threat.get('id')}")
        self.send({Output.THREAT: clean(threat)})

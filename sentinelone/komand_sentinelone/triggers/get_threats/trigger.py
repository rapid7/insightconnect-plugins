import komand
import time
from .schema import GetThreatsInput, GetThreatsOutput, Input, Output
# Custom imports below
from datetime import datetime


class GetThreats(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_threats',
                description='Get threats',
                input=GetThreatsInput(),
                output=GetThreatsOutput())

    def run(self, params={}):
        self.logger.info("Get Threats: trigger started")

        params = {
            "resolved": params.get(Input.RESOLVED),
            "classifications": params.get(Input.CLASSIFICATIONS),
            "agentIsActive": params.get(Input.AGENT_IS_ACTIVE),
            "engines": params.get(Input.ENGINES),
            "limit": 1,
        }

        frequency = params.get("frequency", 5)
        since = None

        while True:
            if since:
                params["createdAt__gt"] = since

            response = self.connection.get_threats(params)

            while response["data"]:
                self.send_first_threat(response["data"])
                cursor = response["pagination"]["nextCursor"]
                if cursor:
                    response = self.connection.get_threats(
                        {"cursor": cursor, "limit": 1}
                    )
                else:
                    break

            since = datetime.now()
            time.sleep(frequency)

    def send_first_threat(self, data):
        threat = data[0]
        self.logger.info("Threat found: " + threat["id"])
        self.send({Output.THREAT: komand.helper.clean(threat)})

import insightconnect_plugin_runtime
from .schema import CloseCaseInput, CloseCaseOutput, Input, Output, Component

# Custom imports below
import requests


class CloseCase(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="close_case",
            description=Component.DESCRIPTION,
            input=CloseCaseInput(),
            output=CloseCaseOutput(),
        )

    def run(self, params={}):

        client = self.connection.client
        case_id = params.get(Input.ID)
        summary = params.get(Input.SUMMARY)
        resolution_status = params.get(Input.RESOLUTION_STATUS)
        impact_status = params.get(Input.IMPACT_STATUS)
        url = f"{client.url}/api/case/{case_id}"
        data = {
            "summary": summary,
            "resolutionStatus": resolution_status,
            "impactStatus": impact_status,
        }

        try:
            user = requests.delete(
                url,
                json=data,
                auth=(self.connection.username, self.connection.password),
                verify=self.connection.verify,
            )
            user.raise_for_status()
        except requests.exceptions.HTTPError:
            self.logger.error(user.json())
            return {Output.TYPE: "NotFound", Output.MESSAGE: "NotClosed"}
        except:
            self.logger.error("Failed to close case")
            raise

        return {Output.TYPE: "Found", Output.MESSAGE: "Closed"}

import insightconnect_plugin_runtime
from .schema import GetAlertsByHostIdInput, GetAlertsByHostIdOutput, Input, Output, Component

# Custom imports below
import json
from json import JSONDecodeError


class GetAlertsByHostId(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_alerts_by_host_id",
            description=Component.DESCRIPTION,
            input=GetAlertsByHostIdInput(),
            output=GetAlertsByHostIdOutput(),
        )

    def run(self, params={}):
        host_id = params.get(Input.HOST_ID)
        url = f"{self.connection.url}/hx/api/v3/alerts/filter"

        payload = json.dumps({"agent._id": [host_id]})

        response = self.connection.session.post(url=url, data=payload)

        if response.status_code == 200:
            raw: str = response.text

            # Unkludge the kludgefest "valid JSON" (lol) response from FireEye
            objects = [
                insightconnect_plugin_runtime.helper.clean(json.loads(l))
                for l in raw.splitlines()
                if (not l.isnumeric() and len(l))
            ]

            return {Output.ALERTS: objects}
        else:
            try:
                details = response.json()["details"][0]
                code, message = details["code"], details["message"]

                raise Exception(f"Error: {message} (error code {code}")

            except JSONDecodeError as e:
                raise Exception(
                    f"Error: Malformed response received from FireEye HX appliance. " f"Got: {response.text}"
                ) from e
            except (KeyError, IndexError) as e:
                raise Exception(
                    "Error: Unknown error received from FireEye HX appliance " "(no error cause reported)."
                ) from e

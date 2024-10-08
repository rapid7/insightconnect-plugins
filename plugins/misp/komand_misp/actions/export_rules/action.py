import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import ExportRulesInput, ExportRulesOutput, Input, Output, Component

# Custom imports below
import requests
import base64


class ExportRules(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="export_rules",
            description=Component.DESCRIPTION,
            input=ExportRulesInput(),
            output=ExportRulesOutput(),
        )

    def run(self, params={}):
        key = self.connection.key
        ssl = self.connection.ssl
        _format = params.get(Input.FORMAT)
        event_id = params.get(Input.EVENT_ID)
        frame = params.get(Input.FRAME)
        tags = params.get(Input.TAGS)
        _from = params.get(Input.FROM)
        _to = params.get(Input.TO)
        last = params.get(Input.LAST)

        path = f"/events/nids/{_format}/download"
        if event_id:
            path = f"{path}/{event_id}"
        else:
            path = f"{path}/null"
        path = f"{path}/{str(frame)}"
        if tags:
            # If more than 1 tag, separate with &&
            if len(tags) > 1:
                tags_str = tags[0]
                tags.pop(0)
                for i in tags:
                    tags_str = f"{tags_str}&&{i}"
                path = f"{path}/{tags_str}"
            else:
                path = f"{path}/{tags}"
        else:
            path = f"{path}/null"
        if _from:
            path = f"{path}/{_from}"
        else:
            path = f"{path}/null"
        if _to:
            path = f"{path}/{_to}"
        else:
            path = f"{path}/null"
        if last:
            path = f"{path}/{last}"
        else:
            path = f"{path}/null"
        url = self.connection.url + path
        headers = {"content-type": "application/json", "Authorization": key}

        # Generate request
        response = requests.get(url, headers=headers, verify=ssl)  # noqa: B501

        # Raise exception if 200 response is not returned
        if response.status_code != 200:
            response_json = response.json()
            message = str(response_json["message"])
            self.logger.error(message)
            raise PluginException(preset=PluginException.Preset.BAD_REQUEST, cause=message)

        # Encode data as b64
        rules = base64.b64encode(response.text.encode("ascii"))

        return {Output.RULES: rules.decode("utf-8")}

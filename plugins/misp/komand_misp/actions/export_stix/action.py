import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import ExportStixInput, ExportStixOutput, Input, Output, Component

# Custom imports below
import json
import requests
import base64


class ExportStix(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="export_stix",
            description=Component.DESCRIPTION,
            input=ExportStixInput(),
            output=ExportStixOutput(),
        )

    def run(self, params={}):
        key = self.connection.key
        ssl = self.connection.ssl
        event_id = params.get(Input.EVENT_ID)
        with_attachment = params.get(Input.ENCODE_ATTACHMENTS)
        tags = params.get(Input.TAGS)
        from_ = params.get(Input.FROM)
        to_ = params.get(Input.TO)
        last = params.get(Input.LAST)

        path = "/events/stix/download.json"
        url = self.connection.url + path
        headers = {
            "Accept": "application/json",
            "content-type": "application/json",
            "Authorization": key,
        }

        request = {}
        request["withAttachment"] = with_attachment
        if event_id:
            request["id"] = int(event_id)
        if tags:
            final_tags = []
            for i in tags:
                final_tags.append(str(i))
            request["tags"] = final_tags
        if from_:
            request["from"] = str(from_)
        if to_:
            request["to"] = str(to_)
        if last:
            request["last"] = str(last)

        post = {"request": request}

        # Generate request
        response = requests.post(url, data=json.dumps(post), headers=headers, verify=ssl)  # noqa: B501

        # Raise exception if 200 response is not returned
        if response.status_code != 200:
            response_json = response.json()
            message = str(response_json["message"])
            self.logger.error(message)
            raise PluginException(preset=PluginException.Preset.BAD_REQUEST, cause=message)

        # Encode data as b64
        stix = base64.b64encode(response.text.encode("ascii"))

        return {Output.STIX: stix.decode("utf-8")}

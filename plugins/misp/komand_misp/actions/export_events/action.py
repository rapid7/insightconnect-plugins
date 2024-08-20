import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import ExportEventsInput, ExportEventsOutput, Input, Output, Component

# Custom imports below
import requests
import base64
import json


class ExportEvents(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="export_events",
            description=Component.DESCRIPTION,
            input=ExportEventsInput(),
            output=ExportEventsOutput(),
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

        path = "/events/xml/download.json"
        url = self.connection.url + path
        headers = {
            "Accept": "application/json",
            "content-type": "application/json",
            "Authorization": key,
        }

        request = {}
        request["withAttachment"] = with_attachment
        if event_id:
            request["eventid"] = event_id
        if tags:
            request["tags"] = tags
        if from_:
            request["from"] = from_
        if to_:
            request["to"] = to_
        if last:
            request["last"] = last

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
        events = base64.b64encode(response.text.encode("ascii"))

        return {Output.EVENTS: events.decode("utf-8")}

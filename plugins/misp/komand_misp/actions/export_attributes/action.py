import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import ExportAttributesInput, ExportAttributesOutput, Input, Output, Component

import json
import requests
import base64


class ExportAttributes(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="export_attributes",
            description=Component.DESCRIPTION,
            input=ExportAttributesInput(),
            output=ExportAttributesOutput(),
        )

    def run(self, params={}):
        key = self.connection.key
        ssl = self.connection.ssl
        event_id = params.get(Input.EVENT_ID)
        ignore = params.get(Input.INCLUDE)
        tags = params.get("tags")
        category = params.get(Input.CATEGORY)
        type_ = params.get(Input.TYPE)
        include_context = params.get(Input.INCLUDE_CONTEXT)
        from_ = params.get(Input.FROM)
        to_ = params.get(Input.TO)
        last = params.get(Input.LAST)

        path = "/events/csv/download"
        url = self.connection.url + path
        headers = {"content-type": "application/json", "Authorization": key}

        request = {}
        request["ignore"] = ignore
        request["includeContext"] = include_context
        if event_id:
            request["eventid"] = event_id
        if tags:
            request["tags"] = tags
        if category:
            request["category"] = category
        if type_:
            request["type"] = type_
        if from_:
            request["from"] = from_
        if to_:
            request["to"] = to_
        if last:
            request["last"] = last

        # Generate request
        response = requests.post(url, data=json.dumps(request), headers=headers, verify=ssl)  # noqa: B501

        # Raise exception if 200 response is not returned
        if response.status_code != 200:
            response_json = response.json()
            message = str(response_json["message"])
            self.logger.error(message)
            raise PluginException(preset=PluginException.Preset.BAD_REQUEST, cause=message)

        # Encode data as b64
        attributes = base64.b64encode(response.text.encode("ascii"))

        return {Output.ATTRIBUTES: attributes.decode("utf-8")}

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import ExportRpzInput, ExportRpzOutput, Input, Output, Component

# Custom imports below
import requests
import base64


class ExportRpz(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="export_rpz", description=Component.DESCRIPTION, input=ExportRpzInput(), output=ExportRpzOutput()
        )

    def run(self, params={}):
        key = self.connection.key
        ssl = self.connection.ssl
        event_id = params.get("event_id")
        tags = params.get("tags")
        from_ = params.get("from")
        to_ = params.get("to")
        path = "/attributes/rpz/download"
        if tags:
            # If more than 1 tag, separate with &&
            if len(tags) > 1:
                tags_str = tags[0]
                tags.pop(0)
                for i in tags:
                    tags_str = f"{tags_str}&&{i}"
                path = f"{path}/{tags_str}"
            else:
                tags_str = str(tags[0])
                path = f"{path}/{tags_str}"
        else:
            path = f"{path}/null"
        if event_id:
            path = f"{path}/{event_id}"
        else:
            path = f"{path}/null"
        if from_:
            path = f"{path}/{from_}"
        else:
            path = f"{path}/null"
        if to_:
            path = f"{path}/{to_}"

        url = self.connection.url + path
        headers = {"content-type": "application/json", "Authorization": key}

        # Generate request
        response = requests.get(url, headers=headers, verify=ssl)  # noqa: B501

        # Raise exception if 200 response is not returned
        if response.status_code != 200:
            response_json = response.json()
            message = str(response_json["message"])
            self.logger.error(message)
            raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=message)
        # Encode data as b64
        self.logger.debug("*" * 10)
        self.logger.debug(response)
        rpz = base64.b64encode(response.text.encode("ascii"))
        self.logger.debug("*" * 10)
        self.logger.debug(rpz)
        return {"rpz": rpz.decode("utf-8")}

        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        event_id = params.get(Input.EVENT_ID)
        from_date = params.get(Input.FROM)
        tags = params.get(Input.TAGS)
        to_date = params.get(Input.TO)
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.RPZ: None,
        }

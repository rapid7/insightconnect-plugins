import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import ExportHashesInput, ExportHashesOutput

# Custom imports below
import requests
import base64


class ExportHashes(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="export_hashes",
            description="Export hashes from HIDS database",
            input=ExportHashesInput(),
            output=ExportHashesOutput(),
        )

    def run(self, params={}):
        key = self.connection.key
        ssl = self.connection.ssl
        format_ = params.get("format")
        tags = params.get("tags")
        from_ = params.get("from")
        to_ = params.get("to")
        last = params.get("last")

        path = f"/events/hids/{format_}/download"
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
        if from_:
            path = f"{path}/{from_}"
        else:
            path = f"{path}/null"
        if to_:
            path = f"{path}/{to_}"
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
        hashes = base64.b64encode(response.text.encode("ascii"))

        return {"hashes": hashes.decode("utf-8")}

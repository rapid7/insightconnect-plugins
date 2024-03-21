import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import DownloadAttachmentInput, DownloadAttachmentOutput

# Custom imports below
import requests
import base64


class DownloadAttachment(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="download_attachment",
            description="Download attachment",
            input=DownloadAttachmentInput(),
            output=DownloadAttachmentOutput(),
        )

    def run(self, params={}):
        key = self.connection.key
        ssl = self.connection.ssl
        attribute_id = params.get("attribute_id")

        headers = {"content-type": "application/json", "Authorization": key}

        path = f"/attributes/downloadAttachment/download/{attribute_id}"
        url = self.connection.url + path

        try:
            # Generate request
            response = requests.get(url, headers=headers, verify=ssl)  # noqa: B501
            str(response.json()["message"])
            response.raise_for_status()
        except ValueError:
            self.logger.error("Attribute ID did not contain an attachment")
            raise PluginException(preset=PluginException.Preset.NOT_FOUND)
        except requests.exceptions.HTTPError as error:
            self.logger.error(error)
            raise PluginException(preset=PluginException.Preset.UNKNOWN)

        # Encode data as b64
        attachment = base64.b64encode(response.content).decode("utf-8")

        return {"attachment": attachment}

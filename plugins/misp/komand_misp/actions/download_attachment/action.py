import insightconnect_plugin_runtime
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
        attribute_id = params.get("attribute_id")

        headers = {"content-type": "application/json", "Authorization": key}

        path = f"/attributes/downloadAttachment/download/{attribute_id}"
        url = self.connection.url + path

        try:
            # Generate request
            response = requests.get(url, headers=headers, verify=False)  # noqa: B501
            str(response.json()["message"])
            response.raise_for_status()
        except ValueError:
            self.logger.error("Attribute ID did not contain an attachment")
            raise Exception("No attachment found for ID")
        except requests.exceptions.HTTPError as e:
            self.logger.error(e)
            raise

        # Encode data as b64
        attachment = base64.b64encode(response.content).decode("utf-8")

        return {"attachment": attachment}

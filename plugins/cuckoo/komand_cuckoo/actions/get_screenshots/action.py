import insightconnect_plugin_runtime
from .schema import GetScreenshotsInput, GetScreenshotsOutput, Input, Output

# Custom imports below
import requests
import base64


class GetScreenshots(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_screenshots",
            description="Returns one (jpeg) or all (zip) screenshots associated with the specified task ID",
            input=GetScreenshotsInput(),
            output=GetScreenshotsOutput(),
        )

    def run(self, params={}):
        server = self.connection.server
        task_id = params.get(Input.TASK_ID, "")
        screenshot_id = params.get(Input.SCREENSHOT_ID, "")

        if screenshot_id:
            endpoint = f"{server}/tasks/screenshots/{task_id}/{screenshot_id}"
        else:
            endpoint = f"{server}/tasks/screenshots/{task_id}"

        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            content_type = response.get("Content-Type", "")
            if content_type == "image/jpeg" or content_type == "application/zip":
                content = response.content
                return {Output.SCREENSHOTS: base64.b64encode(content).decode("UTF-8")}

        except Exception as exception:
            self.logger.error(f"Error: {str(exception)}")

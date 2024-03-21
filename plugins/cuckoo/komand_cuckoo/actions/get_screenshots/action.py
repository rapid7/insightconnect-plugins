import insightconnect_plugin_runtime
from .schema import GetScreenshotsInput, GetScreenshotsOutput, Input, Output, Component

# Custom imports below
from ...util.util import Util


class GetScreenshots(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_screenshots",
            description=Component.DESCRIPTION,
            input=GetScreenshotsInput(),
            output=GetScreenshotsOutput(),
        )

    def run(self, params={}):
        task_id = params.get(Input.TASK_ID, "")
        screenshot_id = params.get(Input.SCREENSHOT_ID, "")
        if screenshot_id:
            endpoint = f"tasks/screenshots/{task_id}/{screenshot_id}"
        else:
            endpoint = f"tasks/screenshots/{task_id}"
        response = self.connection.api.send(endpoint, _json=False)
        content = response.content
        return {Output.SCREENSHOTS: Util.prepare_decoded_value(content)}

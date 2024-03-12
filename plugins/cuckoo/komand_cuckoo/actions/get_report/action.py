import insightconnect_plugin_runtime
from .schema import GetReportInput, GetReportOutput, Input, Output

# Custom imports below
import requests
import base64


class GetReport(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_report",
            description="Returns the report associated with the specified task ID",
            input=GetReportInput(),
            output=GetReportOutput(),
        )

    def run(self, params={}):
        server = self.connection.server
        task_id = params.get(Input.TASK_ID, "")
        desired_format = params.get(Input.FORMAT, "")

        if desired_format:
            endpoint = f"{server}/tasks/report/{task_id}/{desired_format}"
        else:
            endpoint = server + f"/tasks/report/{task_id}"

        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            ctype = response.headers.get("Content-Type", "")
            if (
                ctype.startswith("application/x-tar")
                or ctype.startswith("application/octet-stream")
                or ctype.startswith("application/json")
                or ctype.startswith("text/html")
            ):
                content = response.content
                return {Output.REPORT: base64.b64encode(content).decode("UTF-8")}

        except Exception as exception:
            self.logger.error(f"Error: {str(exception)}")

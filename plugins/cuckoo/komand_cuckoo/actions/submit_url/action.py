import insightconnect_plugin_runtime
from .schema import SubmitUrlInput, SubmitUrlOutput, Input, Component


class SubmitUrl(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit_url",
            description=Component.DESCRIPTION,
            input=SubmitUrlInput(),
            output=SubmitUrlOutput(),
        )

    def run(self, params={}):
        endpoint = "/tasks/create/url"
        url = params.get(Input.URL, "")
        data = {"url": url}
        response = self.connection.api.send(endpoint, method="POST", data=data)
        return response

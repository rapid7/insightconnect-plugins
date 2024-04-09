import insightconnect_plugin_runtime
from .schema import CheckInput, CheckOutput, Component, Input


class Check(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="check",
            description=Component.DESCRIPTION,
            input=CheckInput(),
            output=CheckOutput(),
        )

    def run(self, params={}):

        url = params.get(Input.URL, "")
        url = url.strip()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url

        response = self.connection.phishtank_api.check(url)
        self.logger.info(f"result: {response}")
        return response

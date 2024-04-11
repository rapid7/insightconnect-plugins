import insightconnect_plugin_runtime

from .schema import CheckInput, CheckOutput, Component, Input, Output


class Check(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="check",
            description=Component.DESCRIPTION,
            input=CheckInput(),
            output=CheckOutput(),
        )

    def run(self, params={}):

        url = params.get(Input.URL, "").strip()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = f"https://{url}"

        response = self.connection.phishtank_api.check(url)
        response = response.get("results")

        in_database = response.get("in_database")
        if not in_database:
            return {
                Output.URL: response.get("url"),
                Output.IN_DATABASE: response.get("in_database"),
            }
        else:
            return {
                Output.IN_DATABASE: in_database,
                Output.PHISH_DETAIL_PAGE: response.get("phish_detail_page", ""),
                Output.PHISH_ID: response.get("phish_id"),
                Output.URL: response.get("url"),
                Output.VALID: response.get("valid"),
                Output.VERIFIED: response.get("verified"),
                Output.VERIFIED_AT: str(response.get("verified_at")),
            }

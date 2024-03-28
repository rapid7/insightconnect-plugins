import insightconnect_plugin_runtime
from .schema import CheckInput, CheckOutput, Component, Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException


# Custom imports below
import requests


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
        data = {"url": url}
        # response = self.connection.api.check(data)mak
        # self.logger.info("result: %s", response)
        try:
            response = self.connection.api.check(data)
            self.logger.info("result: %s", response)
        except Exception as e:                              # change this to an insightplugin exception
            self.logger.exception(e)
            return {
                "url": url,
                "in_database": False,
                "verified": False,
            }
        return response

    # def run(self, params={}):
    #     url = params.get("url")
    #     if not url:
    #         raise ValueError("url is required")
    #
    #     url = url.strip()
    #     if not url.startswith("http://") and not url.startswith("https://"):
    #         url = "http://" + url
    #
    #     try:
    #         result = self.connection.check(url)
    #         self.logger.debug("result: %s", result)
    #     except Exception as e:
    #         self.logger.exception(e)
    #         return {
    #             "url": url,
    #             "in_database": False,
    #             "verified": False,
    #         }
    #
    #     if "verified_at" in result:
    #         if result["verified_at"] is None:
    #             result["verified_at"] = str(result["verified_at"])
    #
    #     return result

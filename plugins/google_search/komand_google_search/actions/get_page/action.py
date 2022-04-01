import insightconnect_plugin_runtime
from .schema import GetPageInput, GetPageOutput

# Custom imports below
import googlesearch


class GetPage(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_page",
            description="Request the given URL and return the response page, using the cookie jar",
            input=GetPageInput(),
            output=GetPageOutput(),
        )

    def run(self, params={}):
        url = params.get("url")

        if "://" in url:
            response = googlesearch.get_page(url)
            return {"web_page": response.decode("utf-8")}
        else:
            self.logger.info("A valid URL was not passed, be sure to include the prefix e.g. http://")
            raise ("A valid URL was not passed")

    def test(self):
        return {"web_page": "blah"}

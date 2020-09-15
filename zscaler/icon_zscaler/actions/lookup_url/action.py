import insightconnect_plugin_runtime
from .schema import LookupUrlInput, LookupUrlOutput, Input, Output, Component
# Custom imports below


class LookupUrl(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='lookup_url',
                description=Component.DESCRIPTION,
                input=LookupUrlInput(),
                output=LookupUrlOutput())

    def run(self, params={}):
        lookup_urls = params.get(Input.URLS)

        if len(lookup_urls) > 100:
            self.logger.info("API accepts a maximum of one hundred URLs to lookup."
                             "The results will be presented for the first hundred URLs.")

        return {
            Output.URL_CATEGORIZATION: self.connection.client.url_lookup(lookup_urls[:100])
        }

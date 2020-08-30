import insightconnect_plugin_runtime
from .schema import UnshortenInput, UnshortenOutput, Input, Output, Component
# Custom imports below
import requests
from insightconnect_plugin_runtime.exceptions import PluginException


class Unshorten(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='unshorten',
            description=Component.DESCRIPTION,
            input=UnshortenInput(),
            output=UnshortenOutput())

    def run(self, params={}):
        short_url = params.get(Input.URL)
        try:
            r = requests.get('https://unshorten.me/json/' + short_url)
            r.raise_for_status()
            out = r.json()
        except Exception as e:
            self.logger.error(e)
            raise PluginException(cause='Internal server error',
                                  assistance='Unshorten.me is unable to resolve the URL',
                                  data=e)

        try:
            if out[Output.ERROR]:
                if out[Output.ERROR] == "Connection Error":
                    out[Output.ERROR] = "Unshorten.me is unable to resolve the URL"
                self.logger.error(out.get(Output.ERROR))
        except KeyError:
            # All good, no error key is present
            self.logger.info('No errors')

        return out

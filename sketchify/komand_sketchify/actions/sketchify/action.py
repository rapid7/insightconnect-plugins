# Custom imports below
import requests

import komand
from komand.exceptions import PluginException
from .schema import SketchifyInput, SketchifyOutput, Input, Output, Component


class Sketchify(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='sketchify',
            description=Component.DESCRIPTION,
            input=SketchifyInput(),
            output=SketchifyOutput())

    def run(self, params={}):
        url = params.get(Input.URL)
        try:
            r = requests.post('https://verylegit.link/sketchify', data={'long_url': url})
            r.raise_for_status()
            sketchy_url = r.content
        except Exception as e:
            self.logger.error(e)
            raise PluginException

        return {Output.URL: sketchy_url.decode()}

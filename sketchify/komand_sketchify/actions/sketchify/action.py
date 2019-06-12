import komand
from .schema import SketchifyInput, SketchifyOutput
# Custom imports below
import requests


class Sketchify(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='sketchify',
                description='Turn a URL into a suspicious looking one',
                input=SketchifyInput(),
                output=SketchifyOutput())

    def run(self, params={}):
        url = params.get('url')
        try:
            r = requests.post('https://verylegit.link/sketchify', data = {'long_url': url})
            r.raise_for_status()
            sketchy_url = r.content
        except Exception as e:
            self.logger.error(e)
            raise

        return { 'url': sketchy_url.decode() }

    def test(self):
        try:
            r = requests.post('https://verylegit.link/sketchify', data = {'long_url': 'test'})
            r.raise_for_status()
            sketchy_url = r.content
        except Exception as e:
            self.logger.error(e)
            raise

        return { 'url': sketchy_url.decode() }

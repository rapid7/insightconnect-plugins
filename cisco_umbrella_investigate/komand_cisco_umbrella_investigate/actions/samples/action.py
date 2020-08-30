import komand
from .schema import SamplesInput, SamplesOutput, Input
# Custom imports below
from komand.exceptions import PluginException


class Samples(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='samples',
                description='Return all samples associated with the domain',
                input=SamplesInput(),
                output=SamplesOutput())

    def run(self, params={}):
        URL = params.get(Input.URL)
        limit = params.get('limit', None)
        offset = params.get('offset', None)
        sortby = params.get('sortby', None)
        
        if not limit or limit == 0:
            limit = 10
        
        if not sortby or sortby == "":
            sortby = "score"
        
        if not offset:
            offset = 0

        try:
            samples = self.connection.investigate.samples(URL, limit=limit, offset=offset, sortby=sortby)
        except Exception as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)
        return samples

    def test(self):
        return {"limit": 1, "moreDataAvailable": False, "offset": 0, "query": "*", "samples": [], "totalResults": 0}

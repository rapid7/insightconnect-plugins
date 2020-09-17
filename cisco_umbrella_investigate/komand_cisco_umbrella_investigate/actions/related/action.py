import komand
from .schema import RelatedInput, RelatedOutput
# Custom imports below
from komand.exceptions import PluginException


class Related(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='related',
                description='Returns a list of domain names that have been frequently seen',
                input=RelatedInput(),
                output=RelatedOutput())

    def run(self, params={}):
        domain = params.get('domain')
        try:
            related = self.connection.investigate.related(domain)
        except Exception as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)
        founded = related.get('found')
        if founded:
            return {"related": related.get('tb1')}

        self.logger.info("No results found")
        return {"related": []}

    def test(self):
        return {"related": []}

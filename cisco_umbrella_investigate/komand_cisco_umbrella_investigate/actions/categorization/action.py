import komand
from .schema import CategorizationInput, CategorizationOutput
# Custom imports below
from komand.exceptions import PluginException


class Categorization(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='categorization',
                description='Return if domain has been flagged as malicious by the Cisco Security Labs team',
                input=CategorizationInput(),
                output=CategorizationOutput())

    def run(self, params={}):

        domains = params.get('domains')
        if (len(domains) == 1):
            domains = str(domains[0])
        
        try:
            remoteCategories = self.connection.investigate.categorization(domains, labels=True)
        except Exception as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)

        categories = []
        for key, value in remoteCategories.items():
            categories.append({"name": key, "status": value.get('status'), "security_categories": value.get('security_categories'), "content_categories": value.get('content_categories')})

        return {"categories": categories}

    def test(self):
        return {"categories": []}

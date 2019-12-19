import komand
from .schema import LookupHashInput, LookupHashOutput


# Custom imports below


class LookupHash(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='lookup_hash',
            description='Lookup By Hash',
            input=LookupHashInput(),
            output=LookupHashOutput())

    def normalize(self, result):
        formatted = {'found': False, 'threatscore': 0, 'reports': []}
        if result['response_code']:
            return formatted

        if result and len(result['response']) > 0:
            formatted['found'] = True
            formatted['reports'] = result['response']
            formatted['threatscore'] = result['response'][0]['threatscore']

        return formatted

    def lookup(self, hash=''):
        r = self.connection.get(hash)
        if r.status_code == 200:
            results = r.json()
            self.logger.debug("Got results %s", results)
            return self.normalize(results)
        return {'found': False, 'threatscore': 0, 'reports': []}

    def run(self, params={}):
        """Run action"""
        return self.lookup(params['hash'])

    def test(self):
        """Test action"""
        result = self.lookup('040c0111aef474d8b7bfa9a7caa0e06b4f1049c7ae8c66611a53fc2599f0b90f')
        self.logger.info("Got test result: %s", result)
        return result

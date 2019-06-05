import komand
from .schema import StatsInput, StatsOutput


class Stats(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='stats',
                description='Return current block stats',
                input=StatsInput(),
                output=StatsOutput())

    def run(self, params={}):
        client = self.connection.client
        r = client.stats()
        return { 
            'current': r['current'], 
            'expected': r['expected'], 
            'block_pending': r['block_pending'], 
            'unblock_pending': r['unblock_pending']
        }

    def test(self):
        """TODO: Test action"""
        return {}

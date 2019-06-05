import komand
from .schema import BlockInput, BlockOutput


class Block(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='block',
                description='Send a block request',
                input=BlockInput(),
                output=BlockOutput())

    def run(self, params={}):
        cidr           = params.get('cidr')
        autoscale      = params.get('autoscale', True)
        duration       = params.get('duration', '300')
        skip_whitelist = params.get('skip_whitelist', False)
        source         = params.get('source')
        why            = params.get('why')
        client         = self.connection.client
        result         = client.block(
            cidr,
            source,
            why,
            duration=duration,
            autoscale=autoscale,
            skip_whitelist=skip_whitelist
        )
        return { 'result': result }

    def test(self):
        """TODO: Test action"""
        return {}

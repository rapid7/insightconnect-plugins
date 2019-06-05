import komand
from .schema import UnblockInput, UnblockOutput


class Unblock(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='unblock',
                description='Send a unblock request',
                input=UnblockInput(),
                output=UnblockOutput())

    def run(self, params={}):
        cidr       = params.get('cidr')
        why        = params.get('why')
        client     = self.connection.client
        result     = client.unblock_now(
            cidr,
            why
        )
        return { 'status': result['status'] }

    def test(self):
        """TODO: Test action"""
        return {}

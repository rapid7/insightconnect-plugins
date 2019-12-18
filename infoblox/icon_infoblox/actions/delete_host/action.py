import komand
from .schema import DeleteHostInput, DeleteHostOutput
# Custom imports below


class DeleteHost(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_host',
                description='Delete a host',
                input=DeleteHostInput(),
                output=DeleteHostOutput())

    def run(self, params={}):
        ref = params.get('_ref')
        ref = self.connection.infoblox_connection.delete_host(ref)
        return {'_ref': ref}

    def test(self):
        return {
            '_ref': (
                'record:host/ZG5zLmhvc3QkLl9kZWZhdWx0LmNvbS5pbmZvLnRlc3Q1'
                ':test5.info.com/default'
            )
        }

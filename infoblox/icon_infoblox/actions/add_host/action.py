import komand
from .schema import AddHostInput, AddHostOutput
# Custom imports below


class AddHost(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_host',
                description='Add a new host record',
                input=AddHostInput(),
                output=AddHostOutput())

    def run(self, params={}):
        host = komand.helper.clean_dict(params.get('host'))
        ref = self.connection.infoblox_connection.add_host(host)
        return {'_ref': ref}

    def test(self):
        return {
            '_ref': 'record:host/ZG5zLmhvc3QkLl9kZWZhdWx0LmNvbS5pbmZvLmFieA'
            ':abx.info.com/default'
        }

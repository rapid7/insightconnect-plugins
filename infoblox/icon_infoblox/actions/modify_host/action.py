import komand
from .schema import ModifyHostInput, ModifyHostOutput
# Custom imports below


class ModifyHost(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='modify_host',
                description='Update host data',
                input=ModifyHostInput(),
                output=ModifyHostOutput())

    def run(self, params={}):
        ref = params.get('_ref')
        updated_host = komand.helper.clean_dict(params.get('updated_host'))
        ref = self.connection.infoblox_connection.modify_host(
            ref, updated_host
        )
        return {'_ref': ref}

    def test(self):
        return {
            '_ref': 'record:host/ZG5zLmhvc3QkLl9kZWZhdWx0LmNvbS5pbmZvLmFieA'
            ':abx.info.com/default'
        }

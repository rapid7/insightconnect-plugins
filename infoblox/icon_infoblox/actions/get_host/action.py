import komand
from .schema import GetHostInput, GetHostOutput
# Custom imports below


class GetHost(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_host',
                description='Obtain host details',
                input=GetHostInput(),
                output=GetHostOutput())

    def run(self, params={}):
        ref = params.get('_ref')
        host = self.connection.infoblox_connection.get_host(ref)
        return {'host': host}

    def test(self):
        return {
            'host': {
                'aliases': ['testing'],
                'extattrs': {'Site': {'value': 'East'}},
                '_ref': (
                    'record:host/ZG5zLmhvc3QkLm5vbl9ETlNfaG9zdF9yb290LjAuMTUzM'
                    'jY4OTgzMDkxMC5jb20uZXhhbXBsZS5hZG1pbg:admin.example.com'
                ),
                'ipv4addrs': [{
                    '_ref': (
                        'record:host_ipv4addr/ZG5zLmhvc3RfYWRkcmVzcyQubm9uX0RO'
                        'U19ob3N0X3Jvb3QuMC4xNTMyNjg5ODMwOTEwLmNvbS5leGFtcGxlL'
                        'mFkbWluLjEwLjEwLjEwLjAu:10.10.10.0/admin.example.com'
                    ),
                    'configure_for_dhcp': False,
                    'host': 'admin.example.com',
                    'ipv4addr': '10.10.10.0'
                }],
                'name': 'admin.example.com',
                'view': ' '
            }
        }

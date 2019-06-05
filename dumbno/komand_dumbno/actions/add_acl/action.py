import komand
from .schema import AddAclInput, AddAclOutput


class AddAcl(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_acl',
                description='Add ACL to Arista Switch',
                input=AddAclInput(),
                output=AddAclOutput())

    def run(self, params={}):
        dumbno = self.connection.dumbno
        result = dumbno.add_acl(
            src=params.get('srcip'),
            dst=params.get('dstip'),
            sport=params.get('sport'),
            dport=params.get('dport'),
            proto=params.get('proto')
        )
        if result == 'ok':
          return { 'success': True }
        return { 'success': False }

    def test(self):
        """TODO: Test action"""
        return {}

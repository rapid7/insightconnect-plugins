import komand
from .schema import AddIpsToBlacklistInput, AddIpsToBlacklistOutput
# Custom imports below


class AddIpsToBlacklist(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_ips_to_blacklist',
                description='Add IP addresses to the existing blacklist within the blocked IP address configuration',
                input=AddIpsToBlacklistInput(),
                output=AddIpsToBlacklistOutput())

    def run(self, params={}):
        app_id = params.get('app_id')
        ips = params.get('ips')
        id_ = self.connection.api.add_ips_to_blacklist(app_id, ips)
        return id_

    def test(self):
        return {}

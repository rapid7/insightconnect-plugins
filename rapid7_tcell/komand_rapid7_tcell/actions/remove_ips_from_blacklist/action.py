import komand
from .schema import RemoveIpsFromBlacklistInput, RemoveIpsFromBlacklistOutput
# Custom imports below


class RemoveIpsFromBlacklist(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='remove_ips_from_blacklist',
                description='Remove IP addresses from the existing blacklist within the blocked IP address configuration',
                input=RemoveIpsFromBlacklistInput(),
                output=RemoveIpsFromBlacklistOutput())

    def run(self, params={}):
        app_id = params.get('app_id')
        ips = params.get('ips')
        id_ = self.connection.api.remove_ips_from_blacklist(app_id, ips)
        return id_

    def test(self):
        return {}

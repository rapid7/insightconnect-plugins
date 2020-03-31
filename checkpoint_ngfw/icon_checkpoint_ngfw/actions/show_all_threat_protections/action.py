import komand
from .schema import ShowAllThreatProtectionsInput, ShowAllThreatProtectionsOutput, Input, Output, Component
# Custom imports below


class ShowAllThreatProtections(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='show_all_threat_protections',
                description=Component.DESCRIPTION,
                input=ShowAllThreatProtectionsInput(),
                output=ShowAllThreatProtectionsOutput())

    def run(self, params={}):
        threat_protection_list = self.connection.get_all_threat_protections()
        self.connection.logout()
        return {Output.THREAT_PROTECTION_LIST: threat_protection_list}

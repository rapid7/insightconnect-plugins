import komand
from .schema import DefineScanSettingsInput, DefineScanSettingsOutput, Component
# Custom imports below


class DefineScanSettings(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='define_scan_settings',
                description=Component.DESCRIPTION,
                input=DefineScanSettingsInput(),
                output=DefineScanSettingsOutput())

    def run(self, params={}):
        return self.connection.client.define_scan_settings(params)

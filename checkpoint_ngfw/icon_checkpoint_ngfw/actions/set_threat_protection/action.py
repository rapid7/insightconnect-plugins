import komand
from .schema import SetThreatProtectionInput, SetThreatProtectionOutput, Input, Output, Component
# Custom imports below


class SetThreatProtection(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='set_threat_protection',
                description=Component.DESCRIPTION,
                input=SetThreatProtectionInput(),
                output=SetThreatProtectionOutput())

    def run(self, params={}):
        url = f"{self.connection.server_and_port}/web_api/set-threat-protection"
        payload = {
            "name": params[Input.NAME],
            "overrides": {
                "profile": params[Input.PROFILE],
                "action": params[Input.ACTION]
            }
        }
        headers = self.connection.get_headers()
        discard_other_changes = params.get(Input.DISCARD_OTHER_SESSIONS)

        self.connection.post_and_publish(headers, discard_other_changes, payload, url)

        # If no exception is thrown, we can assume this succeeded.
        return {Output.SUCCESS: True}

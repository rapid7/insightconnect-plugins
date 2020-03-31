import komand
from .schema import SetThreatProtectionByCveInput, SetThreatProtectionByCveOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
import requests


class SetThreatProtectionByCve(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='set_threat_protection_by_cve',
                description=Component.DESCRIPTION,
                input=SetThreatProtectionByCveInput(),
                output=SetThreatProtectionByCveOutput())

    def run(self, params={}):
        # This is overly complicated, R80.40 add filter support to get
        # just the threat prevention we're looking for.
        # However, R80.40 isn't the official mainline build yet
        # This needs to be re-evaluated 3rd or 4th quarter 2020

        cve = params[Input.CVE_NUMBER]
        discard_other_changes = params[Input.DISCARD_OTHER_SESSIONS]
        action = params[Input.ACTION]
        profile = params[Input.PROFILE]

        all_protections = self.connection.get_all_threat_protections()

        target_protection = None

        self.logger.info(f"Looking for CVE: {cve}")
        for protection in all_protections:
            cve_list = protection.get("industry-reference", [])  # This isn't available on all protections
            if cve in cve_list:
                target_protection = protection

        if not target_protection:
            raise PluginException(cause=f"Could not find a threat protection that contains {cve}",
                                  assistance=f"Verify {cve} is included in one of the threat protections on Check Point NGFW")


        target_uid = target_protection.get("uid")
        self.logger.info(f"CVE found: {target_protection.get('name')}")
        self.logger.info(f"UID: {target_uid}")

        # The above call(s) take too long I think, reset our connection and try
        # to update the threat protection
        self.logger.info(f"Logout and get new SID")
        self.connection.logout()
        self.connection.get_sid()

        url = f"{self.connection.server_and_port}/web_api/set-threat-protection"
        payload = {
            "uid": target_uid,
            "overrides": {
                "profile": profile,
                "action": action
            }
        }
        headers = self.connection.get_headers()

        self.logger.info(f"Setting action: {action}")
        success = True
        try:
            self.connection.post_and_publish(headers, discard_other_changes, payload, url)
        except PluginException as e:
            if e.data and "500" in str(e.data):
                self.logger.warning("API returned a 500 error, this usually indicates the "
                                   "protection is already set.")
                self.logger.warning(str(e))
                success = False
            else:
                raise e
        except Exception as e:
            raise e

        # If no exception is thrown, we can assume this succeeded.
        return {Output.SUCCESS: success}

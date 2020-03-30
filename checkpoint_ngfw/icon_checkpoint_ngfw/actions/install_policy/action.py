import komand
from .schema import InstallPolicyInput, InstallPolicyOutput, Input, Output, Component
# Custom imports below


class InstallPolicy(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='install_policy',
                description=Component.DESCRIPTION,
                input=InstallPolicyInput(),
                output=InstallPolicyOutput())

    def run(self, params={}):
        url = f"{self.connection.server_and_port}/web_api/install-policy"
        payload = {
            "policy-package": params.get(Input.POLICY_PACKAGE),
            "targets": params.get(Input.TARGETS),
            "install-on-all-cluster-members-or-fail": params.get(Input.INSTALL_ON_ALL_CLUSTER_MEMBERS_OR_FAIL)
        }

        headers = self.connection.get_headers()
        discard_other_changes = params.get(Input.DISCARD_OTHER_SESSIONS)

        self.connection.install_policy(headers, discard_other_changes, payload, url)

        return {"success": True}

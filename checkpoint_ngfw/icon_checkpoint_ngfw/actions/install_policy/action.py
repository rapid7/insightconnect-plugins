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
        if params.get(Input.DISCARD_OTHER_SESSIONS, False):
            self.connection.discard_all_sessions()

        url = f"{self.connection.server_and_port}/web_api/install-policy"
        payload = {
            "policy-package": params.get(Input.POLICY_PACKAGE),
            "targets": params.get(Input.TARGETS),
            "install-on-all-cluster-members-or-fail": params.get(Input.INSTALL_ON_ALL_CLUSTER_MEMBERS_OR_FAIL)
        }

        headers = self.connection.get_headers()

        self.connection.install_policy(headers, payload, url)

        return {"success": True}

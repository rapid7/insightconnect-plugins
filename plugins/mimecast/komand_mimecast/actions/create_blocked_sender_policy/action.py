import insightconnect_plugin_runtime
from .schema import CreateBlockedSenderPolicyInput, CreateBlockedSenderPolicyOutput, Input, Output, Component

# Custom imports below
from komand_mimecast.util.util import Utils
from komand_mimecast.util.constants import DATA_FIELD


class CreateBlockedSenderPolicy(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_blocked_sender_policy",
            description=Component.DESCRIPTION,
            input=CreateBlockedSenderPolicyInput(),
            output=CreateBlockedSenderPolicyOutput(),
        )

    def run(self, params={}):
        source_ips = params.get(Input.SOURCE_IPS)
        option = params.get(Input.OPTION)

        data = {"option": option}

        # Generate policy dictionary
        policy = {}
        for key, value in params.items():
            temp = Utils.normalize(key, value)
            policy.update(temp)

        # Remove source_ips and option from policy as they should not be directly in that dictionary
        if params.get(Input.SOURCE_IPS):
            del policy["sourceIps"]
        del policy["option"]

        # Transform source_ips from comma delimited string to list
        if params.get(Input.SOURCE_IPS):
            source_ips = source_ips.split(",")

        # Add conditions dic to policy
        if source_ips:
            policy["conditions"] = {"sourceIPs": source_ips}

        # Add policy to data
        data["policy"] = policy

        return {Output.SENDER_POLICY: self.connection.client.create_blocked_sender_policy(data).get(DATA_FIELD)}

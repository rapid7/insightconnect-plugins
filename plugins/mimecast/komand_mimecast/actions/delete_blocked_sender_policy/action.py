import insightconnect_plugin_runtime
from .schema import DeleteBlockedSenderPolicyInput, DeleteBlockedSenderPolicyOutput, Input, Output, Component

# Custom imports below


class DeleteBlockedSenderPolicy(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_blocked_sender_policy",
            description=Component.DESCRIPTION,
            input=DeleteBlockedSenderPolicyInput(),
            output=DeleteBlockedSenderPolicyOutput(),
        )

    def run(self, params={}):
        identifier = params.get(Input.ID)
        data = {"id": identifier}
        self.connection.client.delete_blocked_sender_policy(data)
        return {"success": True}

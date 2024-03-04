import insightconnect_plugin_runtime
from .schema import UnblockUserInput, UnblockUserOutput, Input, Output, Component

# Custom imports below
import requests


class UnblockUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="unblock_user",
            description=Component.DESCRIPTION,
            input=UnblockUserInput(),
            output=UnblockUserOutput(),
        )

    def run(self, params={}):
        user_id = params.get(Input.ID)
        self.connection.client.unblock_user(user_id=user_id)
        return {Output.STATUS: True}

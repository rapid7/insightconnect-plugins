import insightconnect_plugin_runtime
from .schema import ListSshInput, ListSshOutput, Input, Output, Component

# Custom imports below
import json
import requests


class ListSsh(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_ssh",
            description=Component.DESCRIPTION,
            input=ListSshInput(),
            output=ListSshOutput(),
        )

    def run(self, params={}):
        user_id = params.get(Input.ID)
        response = self.connection.client.list_ssh(user_id)

        ssh_keys = []
        for key in response:
            key_obj = {
                "created_at": key.get("created_at", ""),
                "id": key.get("id", ""),
                "key": key.get("key", ""),
                "title": key.get("title", ""),
            }
            ssh_keys.append(key_obj)

        return {Output.SSH_KEYS: ssh_keys}

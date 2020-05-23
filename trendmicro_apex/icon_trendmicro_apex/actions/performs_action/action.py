import komand
from .schema import PerformsActionInput, PerformsActionOutput, Input, Component
# Custom imports below
from komand.exceptions import PluginException


class PerformsAction(komand.Action):
    ACTIONS_DICT = {
        "Isolate": "cmd_isolate_agent",
        "Restore": "cmd_restore_isolated_agent",
        "Relocate": "cmd_relocate_agent",
        "Uninstall": "cmd_uninstall_agent"
    }

    def __init__(self):
        super(self.__class__, self).__init__(
            name='performs_action',
            description=Component.DESCRIPTION,
            input=PerformsActionInput(),
            output=PerformsActionOutput())

    def run(self, params={}):
        return self.connection.api.execute(
            "post",
            "/WebApp/API/AgentResource/ProductAgents",
            self._get_payload(params)
        )

    def _get_payload(self, params):
        action_id = params.get(Input.ACTION)
        payload = {
            "act": self.ACTIONS_DICT.get(action_id),
            "allow_multiple_match": params.get(Input.ALLOW_MULTIPLE_MATCH, False)
        }

        if params.get(Input.ENTITY_ID):
            payload["entity_id"] = params.get(Input.ENTITY_ID)
            self._validate_allow_action(action_id, params, Input.ENTITY_ID)
        if params.get(Input.HOST_NAME):
            payload["host_name"] = params.get(Input.HOST_NAME)
            self._validate_allow_action(action_id, params, Input.HOST_NAME)
        if params.get(Input.IP_ADDRESS):
            payload["ip_address"] = params.get(Input.IP_ADDRESS)
            self._validate_allow_action(action_id, params, Input.IP_ADDRESS)
        if params.get(Input.MAC_ADDRESS):
            payload["mac_address"] = params.get(Input.MAC_ADDRESS)
            self._validate_allow_action(action_id, params, Input.MAC_ADDRESS)
        if params.get(Input.PRODUCT):
            payload["product"] = params.get(Input.PRODUCT)
        if params.get(Input.RELOCATE_TO_FOLDER_PATH):
            payload["relocate_to_folder_path"] = params.get(Input.RELOCATE_TO_FOLDER_PATH)
        if params.get(Input.RELOCATE_TO_SERVER_ID):
            payload["relocate_to_server_id"] = params.get(Input.RELOCATE_TO_SERVER_ID)

        return payload

    @staticmethod
    def _validate_allow_action(action_id, params, id_name):
        entity_id = params.get(id_name)
        deny_ids = params.get(Input.SKIP_IDS)
        if deny_ids and action_id in ["Isolate", "Uninstall"] and entity_id in deny_ids:
            raise PluginException(cause="Something unexpected occurred.",
                                  assistance=f"Can't {action_id.lower()} for admin endpoint")

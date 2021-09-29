import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import DeleteRegistryKeyInput, DeleteRegistryKeyOutput, Input, Output, Component

# Custom imports below
from icon_cybereason.util.api import CybereasonAPI


class DeleteRegistryKey(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_registry_key",
            description=Component.DESCRIPTION,
            input=DeleteRegistryKeyInput(),
            output=DeleteRegistryKeyOutput(),
        )

    def run(self, params={}):
        machine_guid = self.connection.api.get_sensor_details(params.get(Input.SENSOR)).get("guid")
        malop_id = params.get(Input.MALOP_ID)
        malop_features = self.connection.api.get_malop_feature_details(malop_id, "registryKeysToRemediate")

        if malop_features:
            targets = CybereasonAPI.get_machine_targets(malop_features, machine_guid)
        else:
            raise PluginException(
                cause="Empty response for Malop features lookup.",
                assistance=f"Ensure that the Malop: {malop_id} contains a registry key to delete for that sensor and try again.",
            )

        actions_by_machine = {machine_guid: []}
        for i in targets:
            actions_by_machine[machine_guid].append({"targetId": i, "actionType": "DELETE_REGISTRY_KEY"})

        return {
            Output.RESPONSE: self.connection.api.remediate(
                params.get(Input.INITIATOR_USER_NAME), actions_by_machine, malop_id
            )
        }

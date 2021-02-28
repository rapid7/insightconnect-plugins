import insightconnect_plugin_runtime
from .schema import IsolateMachineInput, IsolateMachineOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class IsolateMachine(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="isolate_machine",
            description=Component.DESCRIPTION,
            input=IsolateMachineInput(),
            output=IsolateMachineOutput(),
        )

    def run(self, params={}):
        malop_id = params.get(Input.MALOP_ID)
        if malop_id:
            pylum_ids = params.get(Input.PYLUM_IDS)
            if not pylum_ids:
                raise PluginException(
                    cause="Pylum IDs shouldn't be empty", assistance="Please check this input"
                )
            return {Output.RESPONSE: self.connection.api.isolate_machines(malop_id, pylum_ids)}

        initiator_user_name = params.get(Input.INITIATOR_USER_NAME)
        actions_by_machine = params.get(Input.ACTIONS_BY_MACHINE)
        if not initiator_user_name or not actions_by_machine:
            raise PluginException(
                cause="Initiator user name and actions by machine shouldn't be empty",
                assistance="Please check this input",
            )

        return {
            Output.RESPONSE: self.connection.api.remediate(initiator_user_name, actions_by_machine)
        }

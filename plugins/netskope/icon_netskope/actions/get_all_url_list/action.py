import insightconnect_plugin_runtime

from .schema import Component, GetAllUrlListInput, GetAllUrlListOutput, Input, Output


class GetAllUrlList(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_all_url_list",
            description=Component.DESCRIPTION,
            input=GetAllUrlListInput(),
            output=GetAllUrlListOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        status = params.get(Input.STATUS)
        # END INPUT BINDING - DO NOT REMOVE

        response = self.connection.client.get_all_url_list(
            {"pending": self._check_pending(status)} if status != "any" else None
        )
        return {Output.URLLISTS: response if response else []}

    @staticmethod
    def _check_pending(pending_value: str) -> int:
        return 1 if pending_value == "pending" else 0

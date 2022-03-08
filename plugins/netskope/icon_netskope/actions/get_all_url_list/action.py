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
        request_params = (
            {"pending": self._check_pending(params.get(Input.STATUS))} if params.get(Input.STATUS) else None
        )
        response = self.connection.client.get_all_url_list(request_params)
        if response:
            return {Output.URLLISTS: response}
        return {Output.URLLISTS: []}

    def _check_pending(self, pending_value: str) -> int:
        return 1 if pending_value == "pending" else 0

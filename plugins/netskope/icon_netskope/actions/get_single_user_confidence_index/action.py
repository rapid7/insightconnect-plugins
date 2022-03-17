import insightconnect_plugin_runtime

from .schema import Component, GetSingleUserConfidenceIndexInput, GetSingleUserConfidenceIndexOutput, Input


class GetSingleUserConfidenceIndex(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_single_user_confidence_index",
            description=Component.DESCRIPTION,
            input=GetSingleUserConfidenceIndexInput(),
            output=GetSingleUserConfidenceIndexOutput(),
        )

    def run(self, params={}):
        data = {"user": params.get(Input.USERNAME), Input.FROMTIME: params.get(Input.FROMTIME)}
        return self.connection.client.get_single_user_confidence_index(data)

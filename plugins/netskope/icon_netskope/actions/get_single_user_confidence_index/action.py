import insightconnect_plugin_runtime

from .schema import Component, GetSingleUserConfidenceIndexInput, GetSingleUserConfidenceIndexOutput, Input, Output


class GetSingleUserConfidenceIndex(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_single_user_confidence_index",
            description=Component.DESCRIPTION,
            input=GetSingleUserConfidenceIndexInput(),
            output=GetSingleUserConfidenceIndexOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        username = params.get(Input.USERNAME)
        from_time = params.get(Input.FROMTIME)
        # END INPUT BINDING - DO NOT REMOVE

        response = self.connection.client.get_single_user_confidence_index({"user": username, "fromTime": from_time})
        return {Output.USERID: response.get("userId"), Output.CONFIDENCES: response.get("confidences")}

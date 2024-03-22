import insightconnect_plugin_runtime

from .schema import GetOffensesInput, GetOffensesOutput, Component, Input, Output

from icon_ibm_qradar.util.api import IBMQRadarAPI


class GetOffenses(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super().__init__(
            name="get_offenses",
            description=Component.DESCRIPTION,
            input=GetOffensesInput(),
            output=GetOffensesOutput(),
        )

    def run(self, params={}):
        """
        Run Method to execute action.

        :param params: Input Param config required for the Action
        :return: None
        """
        api = IBMQRadarAPI(connection=self.connection, logger=self.logger)
        response = api.get_offenses_request(params=params, fields=[Input.RANGE, Input.FILTER, Input.FIELDS, Input.SORT])
        return {Output.DATA: response}

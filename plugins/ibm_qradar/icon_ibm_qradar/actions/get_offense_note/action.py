import insightconnect_plugin_runtime

from .schema import GetOffenseNoteInput, GetOffenseNoteOutput, Component, Input, Output

from icon_ibm_qradar.util.api import IBMQRadarAPI


class GetOffenseNote(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super().__init__(
            name="get_offense_note",
            description=Component.DESCRIPTION,
            input=GetOffenseNoteInput(),
            output=GetOffenseNoteOutput(),
        )

    def run(self, params={}):
        """Run Method to execute action.

        :param params: Input Param config required for the Action
        :return: None
        """
        offense_id = params.get(Input.OFFENSE_ID, "")
        self.logger.info(f"Offense ID provided: {offense_id}")

        api = IBMQRadarAPI(connection=self.connection, logger=self.logger)
        response = api.get_offense_note_request(
            offense_id=offense_id, params=params, fields=[Input.FILTER, Input.FIELDS, Input.RANGE]
        )
        return {Output.DATA: response}

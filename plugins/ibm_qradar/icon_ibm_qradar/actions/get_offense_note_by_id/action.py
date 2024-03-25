import insightconnect_plugin_runtime

from .schema import (
    GetOffenseNoteByIdOutput,
    GetOffenseNoteByIdInput,
    Component,
    Input,
    Output,
)

from icon_ibm_qradar.util.api import IBMQRadarAPI


class GetOffenseNoteById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super().__init__(
            name="get_offense_note_by_id",
            description=Component.DESCRIPTION,
            input=GetOffenseNoteByIdInput(),
            output=GetOffenseNoteByIdOutput(),
        )

    def run(self, params={}):
        """Run Method to execute action.

        :param params: Input Param config required for the Action
        :return: None
        """
        offense_id = params.get(Input.OFFENSE_ID, "")
        self.logger.info(f"Offense ID provided: {offense_id}")

        note_id = params.get(Input.NOTE_ID, "")
        self.logger.info(f"Note ID provided: {offense_id}")

        api = IBMQRadarAPI(connection=self.connection, logger=self.logger)
        response = api.get_offense_note_by_id_request(
            offense_id=offense_id, note_id=note_id, params=params, fields=[Input.FIELDS]
        )
        return {Output.DATA: response}

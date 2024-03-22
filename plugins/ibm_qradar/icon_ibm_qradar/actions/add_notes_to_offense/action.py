import insightconnect_plugin_runtime

from .schema import (
    AddNotesToOffenseInput,
    AddNotesToOffenseOutput,
    Component,
    Input,
    Output,
)


from icon_ibm_qradar.util.api import IBMQRadarAPI


class AddNotesToOffense(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super().__init__(
            name="add_notes_to_offense",
            description=Component.DESCRIPTION,
            input=AddNotesToOffenseInput(),
            output=AddNotesToOffenseOutput(),
        )

    def run(self, params={}):
        """Run Method to execute action.

        :param params: Input Param config required for the Action
        :return: None
        """
        offense_id = params.get(Input.OFFENSE_ID, "")
        self.logger.info(f"Offense ID provided: {offense_id}")

        note_text = params.get(Input.NOTE_TEXT, "")
        self.logger.info(f"Note Text provided: {note_text}")

        query_params = {"note_text": note_text}

        api = IBMQRadarAPI(connection=self.connection, logger=self.logger)
        response = api.add_notes_to_offense_request(
            offense_id=offense_id, params=params, query_params=query_params, fields=[Input.FIELDS]
        )
        return {Output.DATA: response}

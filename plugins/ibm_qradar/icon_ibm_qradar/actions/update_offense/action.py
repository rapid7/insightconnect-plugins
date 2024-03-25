import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import UpdateOffenseInput, UpdateOffenseOutput, Component, Input, Output

from icon_ibm_qradar.util.constants.messages import (
    CLOSING_REASON_ID_NOT_PROVIDED,
    CLOSING_REASON_ID_PROVIDED_FOR_OTHER_STATUS,
    CLOSING_REASON_ID_PROVIDED_IS_NOT_INTEGER,
)
from icon_ibm_qradar.util.api import IBMQRadarAPI


def parse_params(params: dict, logger) -> dict:
    """To parse the input params."""

    query_params = {}
    assigned_to = params.get(Input.ASSIGNED_TO, "")
    logger.info(f"Provided Assigned to: {assigned_to}")

    closing_reason_id = params.get(Input.CLOSING_REASON_ID, "")
    logger.info(f"Provided closing reason ID: {assigned_to}")

    if closing_reason_id != "" and not closing_reason_id.isdigit():
        raise PluginException(cause=CLOSING_REASON_ID_PROVIDED_IS_NOT_INTEGER)

    follow_up = params.get(Input.FOLLOW_UP, False)
    logger.info(f"follow_up provided: {follow_up}")

    protected = params.get(Input.PROTECTED, False)
    logger.info(f"protected provided: {protected}")

    status = params.get(Input.STATUS, "")
    status = status.upper()
    logger.info(f"status provided: {status}")

    if assigned_to != "":
        query_params["assigned_to"] = assigned_to

    if closing_reason_id != "":
        query_params["closing_reason_id"] = closing_reason_id

    query_params["follow_up"] = "true" if follow_up else "false"
    query_params["protected"] = "true" if protected else "false"

    if status != "":
        query_params["status"] = status

    return query_params


def validate(query_params: dict):
    if Input.CLOSING_REASON_ID in query_params:
        if Input.STATUS not in query_params or query_params[Input.STATUS] != "CLOSED":
            raise PluginException(cause=CLOSING_REASON_ID_PROVIDED_FOR_OTHER_STATUS)

    if Input.STATUS in query_params and query_params["status"] == "CLOSED":
        if Input.CLOSING_REASON_ID not in query_params or query_params[Input.CLOSING_REASON_ID] == "":
            raise PluginException(cause=CLOSING_REASON_ID_NOT_PROVIDED)


class UpdateOffense(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super().__init__(
            name="update_offense",
            description=Component.DESCRIPTION,
            input=UpdateOffenseInput(),
            output=UpdateOffenseOutput(),
        )

    def run(self, params={}):
        """Run Method to execute action.

        :param params: Input Param config required for the Action
        :return:
        """
        offense_id = params.get(Input.OFFENSE_ID, "")
        self.logger.info(f"Provided Offense ID: {offense_id}")

        query_params = parse_params(params, self.logger)
        validate(query_params)

        api = IBMQRadarAPI(connection=self.connection, logger=self.logger)
        response = api.update_offense_request(
            offense_id=offense_id, params=params, query_params=query_params, fields=[Input.FIELDS]
        )
        return {Output.DATA: response}

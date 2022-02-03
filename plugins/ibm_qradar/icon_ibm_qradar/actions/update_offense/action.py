import insightconnect_plugin_runtime
import requests
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import UpdateOffenseInput, UpdateOffenseOutput, Component, Input, Output

from icon_ibm_qradar.util.constants.endpoints import UPDATE_OFFENSES_ENDPOINT
from icon_ibm_qradar.util.constants.messages import (
    CLOSING_REASON_ID_NOT_PROVIDED,
    CLOSING_REASON_ID_PROVIDED_FOR_OTHER_STATUS,
    CLOSING_REASON_ID_PROVIDED_IS_NOT_INTEGER,
)
from icon_ibm_qradar.util.url import URL
from icon_ibm_qradar.util.utils import prepare_request_params, handle_response


def parse_params(params: dict, logger) -> dict:
    """To parse the input params."""

    query_params = {}
    assigned_to = params.get(Input.ASSIGNED_TO, "")
    logger.info("Provided Assigned to: %s", assigned_to)

    closing_reason_id = params.get(Input.CLOSING_REASON_ID, "")
    logger.info("Provided closing reason ID: %s", closing_reason_id)

    if closing_reason_id != "" and not closing_reason_id.isdigit():
        raise PluginException(cause=CLOSING_REASON_ID_PROVIDED_IS_NOT_INTEGER)

    follow_up = params.get(Input.FOLLOW_UP, False)
    logger.info("follow_up provided: %s", follow_up)

    protected = params.get(Input.PROTECTED, False)
    logger.info("protected provided: %s", protected)

    status = params.get(Input.STATUS, "")
    status = status.upper()
    logger.info("status provided: %s", status)

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
        self.endpoint = UPDATE_OFFENSES_ENDPOINT

    def run(self, params={}):
        """Run Method to execute action.

        :param params: Input Param config required for the Action
        :return:
        """
        offense_id = params.get(Input.OFFENSE_ID, "")
        self.logger.info("Provided Offense ID: %s", offense_id)

        query_params = parse_params(params, self.logger)
        validate(query_params)

        url_obj = URL(self.connection.host_url, self.endpoint)
        basic_url = url_obj.get_basic_url()
        if offense_id:
            basic_url = basic_url.format(offense_id=offense_id)

        url_obj.set_basic_url(basic_url)

        basic_url, headers = prepare_request_params(params, self.logger, url_obj, [Input.FIELDS], query_params)

        auth = (self.connection.username, self.connection.password)
        try:
            self.logger.debug(f"Final URL: {basic_url}")
            response = requests.post(
                url=basic_url, headers=headers, data={}, auth=auth, verify=self.connection.verify_ssl
            )
        except requests.exceptions.ConnectionError:
            raise PluginException(preset=PluginException.Preset.SERVICE_UNAVAILABLE)

        return {Output.DATA: handle_response(response)}

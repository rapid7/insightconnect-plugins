import insightconnect_plugin_runtime
import requests
from insightconnect_plugin_runtime.exceptions import ClientException, PluginException

from .schema import UpdateOffenseInput, UpdateOffenseOutput, Component, Input, Output

from icon_ibm_qradar.util.constants.endpoints import UPDATE_OFFENSES_ENDPOINT
from icon_ibm_qradar.util.constants.messages import (
    EMPTY_OFFENSE_ID_FOUND,
    CLOSING_REASON_ID_NOT_PROVIDED,
    CLOSING_REASON_ID_PROVIDED_FOR_OTHER_STATUS,
    CLOSING_REASON_ID_PROVIDED_IS_NOT_INTEGER,
)
from icon_ibm_qradar.util.url import URL
from icon_ibm_qradar.util.utils import prepare_request_params, handle_response


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
        self.logger.info("Offense ID provided: %s", offense_id)

        assigned_to = params.get(Input.ASSIGNED_TO, "")
        self.logger.info("assigned_to provided: %s", assigned_to)

        closing_reason_id = params.get(Input.CLOSING_REASON_ID, "")
        self.logger.info("closing_reason_id provided: %s", closing_reason_id)

        if closing_reason_id != "" and not closing_reason_id.isdigit():
            raise ClientException(Exception(CLOSING_REASON_ID_PROVIDED_IS_NOT_INTEGER))

        follow_up = params.get(Input.FOLLOW_UP, False)
        self.logger.info("follow_up provided: %s", follow_up)

        protected = params.get(Input.PROTECTED, False)
        self.logger.info("protected provided: %s", protected)

        status = params.get(Input.STATUS, "")
        self.logger.info("status provided: %s", status)

        query_params = {}

        if assigned_to != "":
            query_params["assigned_to"] = assigned_to

        if closing_reason_id != "":
            if status != "CLOSED":
                self.logger.info("Terminating: Closing Reason Id is provided to open / hide offense.")
                raise ClientException(Exception(CLOSING_REASON_ID_PROVIDED_FOR_OTHER_STATUS))

            query_params["closing_reason_id"] = closing_reason_id

        query_params["follow_up"] = "true" if follow_up else "false"
        query_params["protected"] = "true" if protected else "false"

        if status != "":
            query_params["status"] = status
            if status == "CLOSED":
                if closing_reason_id == "":
                    self.logger.info("Terminating: Closing Reason Id is not provided.")
                    raise ClientException(Exception(CLOSING_REASON_ID_NOT_PROVIDED))

        url_obj = URL(self.connection.hostname, self.endpoint)
        basic_url = url_obj.get_basic_url()
        if offense_id:
            basic_url = basic_url.format(offense_id=offense_id)

        url_obj.set_basic_url(basic_url)

        basic_url, headers = prepare_request_params(params, self.logger, url_obj, [Input.FIELDS], query_params)

        auth = (self.connection.username, self.connection.password)
        try:
            self.logger.debug(f"Final Url: {basic_url}")
            response = requests.post(url=basic_url, headers=headers, data={}, auth=auth)
        except requests.exceptions.ConnectionError:
            raise PluginException(preset=PluginException.Preset.SERVICE_UNAVAILABLE)

        return {Output.DATA: handle_response(response)}

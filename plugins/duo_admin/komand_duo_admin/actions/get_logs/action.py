import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import convert_dict_to_camel_case
from .schema import GetLogsInput, GetLogsOutput, Input, Output, Component

# Custom imports below
import time
from typing import Optional
from komand_duo_admin.util.helpers import clean, convert_fields_to_string
from komand_duo_admin.util.constants import Cause, Assistance, PossibleInputs


class GetLogs(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_logs", description=Component.DESCRIPTION, input=GetLogsInput(), output=GetLogsOutput()
        )

    def run(self, params={}):
        max_time = params.get(Input.MAXTIME)
        parameters = clean(
            {
                "mintime": str(params.get(Input.MINTIME, 1000000000000)),
                "maxtime": str(max_time) if max_time else str(int(round(time.time() * 1000))),
                "applications": params.get(Input.APPLICATIONS),
                "users": params.get(Input.USERS),
                "event_types": self.input_validation(params.get(Input.EVENTTYPES), PossibleInputs.possible_event_types),
                "factors": self.input_validation(params.get(Input.FACTORS), PossibleInputs.possible_factors),
                "groups": params.get(Input.GROUPS),
                "phone_numbers": params.get(Input.PHONENUMBERS),
                "reasons": self.input_validation(params.get(Input.REASONS), PossibleInputs.possible_reasons),
                "results": self.input_validation(params.get(Input.RESULTS), PossibleInputs.possible_results),
                "tokens": params.get(Input.TOKENS),
                "limit": str(1000),
            }
        )
        auth_logs = self.connection.admin_api.get_all_auth_logs(parameters)
        return {Output.AUTHLOGS: convert_fields_to_string(convert_dict_to_camel_case(clean(auth_logs)))}

    @staticmethod
    def input_validation(given_inputs: Optional[list], possible_inputs: list) -> Optional[list]:
        if not given_inputs:
            return None

        new_inputs = []
        for given_input in given_inputs:
            lower_input = given_input.lower().strip().replace(" ", "_")
            if lower_input in possible_inputs:
                new_inputs.append(lower_input)
            else:
                raise PluginException(
                    cause=Cause.INVALID_INPUT,
                    assistance=Assistance.INVALID_INPUT.format(
                        given_input=given_input, possible_inputs=possible_inputs
                    ),
                )
        return new_inputs

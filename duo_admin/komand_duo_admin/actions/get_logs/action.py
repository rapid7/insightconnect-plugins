import komand
from komand.exceptions import PluginException
from .schema import GetLogsInput, GetLogsOutput, Input, Output, Component

# Custom imports below
import time
from komand_duo_admin.util.util import PossibleInputs
from typing import Optional


class GetLogs(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_logs", description=Component.DESCRIPTION, input=GetLogsInput(), output=GetLogsOutput()
        )

        self.METADATA, self.NEXT_OFFSET, self.AUTH_LOGS, self.TOTAL_OBJECTS = (
            "metadata",
            "next_offset",
            "authlogs",
            "total_objects",
        )
        self.PAGE_SIZE = 1000

    def run(self, params={}):
        min_time = params.get(Input.MINTIME, 1000000000000)
        applications = params.get(Input.APPLICATIONS)
        users = params.get(Input.USERS)
        groups = params.get(Input.GROUPS)
        phone_numbers = params.get(Input.PHONE_NUMBERS)
        registration_id = params.get(Input.REGISTRATION_ID)
        token_id = params.get(Input.TOKEN_ID)
        webauthnkey = params.get(Input.WEBAUTHNKEY)

        if params.get(Input.MAXTIME):
            max_time = params.get(Input.MAXTIME)
        else:
            max_time = int(round(time.time() * 1000))

        event_types = self.input_validation(params.get(Input.EVENT_TYPES), PossibleInputs.possible_event_types)
        factors = self.input_validation(params.get(Input.FACTORS), PossibleInputs.possible_factors)
        reasons = self.input_validation(params.get(Input.REASONS), PossibleInputs.possible_reasons)
        results = self.input_validation(params.get(Input.RESULTS), PossibleInputs.possible_results)

        auth_logs = []
        try:
            results = self.connection.admin_api.get_authentication_log(
                api_version=2,
                mintime=min_time,
                maxtime=max_time,
                applications=applications,
                users=users,
                event_types=event_types,
                factors=factors,
                groups=groups,
                phone_numbers=phone_numbers,
                reasons=reasons,
                results=results,
                registration_id=registration_id,
                token_id=token_id,
                webauthnkey=webauthnkey,
                limit=str(self.PAGE_SIZE),
            )
            auth_logs.extend(results[self.AUTH_LOGS])

            total_objects_left = results[self.METADATA][self.TOTAL_OBJECTS] - self.PAGE_SIZE

            next_offset = results[self.METADATA][self.NEXT_OFFSET]
            while total_objects_left > 0:
                results = self.connection.admin_api.get_authentication_log(
                    api_version=2,
                    mintime=min_time,
                    maxtime=max_time,
                    applications=applications,
                    users=users,
                    event_types=event_types,
                    factors=factors,
                    groups=groups,
                    phone_numbers=phone_numbers,
                    reasons=reasons,
                    results=results,
                    registration_id=registration_id,
                    token_id=token_id,
                    webauthnkey=webauthnkey,
                    limit=str(self.PAGE_SIZE),
                    next_offset=next_offset,
                )

                next_offset = results[self.METADATA][self.NEXT_OFFSET]
                total_objects_left -= self.PAGE_SIZE
                auth_logs.extend(results[self.AUTH_LOGS])

            return {Output.AUTHLOGS: komand.helper.clean(auth_logs)}
        except KeyError as e:
            raise PluginException(
                preset=PluginException.Preset.SERVER_ERROR,
                data=f"Error: API response was missing required fields necessary for proper functioning. {str(e)}",
            )

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
                    cause="Incorrect input.",
                    assistance=f"Please check that your input is correct and try again.\n"
                    f"Incorrect input: '{given_input}'.\n"
                    f"Possible inputs: '{possible_inputs}'.",
                )
        return new_inputs

import komand
from .schema import GetDetailsForSpecificEventInput, GetDetailsForSpecificEventOutput, Input, Output
from komand_carbon_black_defense.connection import *

# Custom imports below
import requests


class GetDetailsForSpecificEvent(komand.Action):

    # URI for Get Details
    _URI = "/integrationServices/v3/event/"

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_details_for_specific_event",
            description="Retrieve details for an individual event given the event ID",
            input=GetDetailsForSpecificEventInput(),
            output=GetDetailsForSpecificEventOutput(),
        )

    def run(self, params={}):

        event_id = params.get(Input.EVENT_ID)
        id_ = self.connection.get_job_id_for_detail_search(event_id=event_id)

        if id_ is None:
            return {Output.SUCCESS: False,
                    Output.EVENTINFO: {}
                    }
        detail_search_status = self.connection.check_status_of_detail_search(id_)

        # check if status of
        # detail search is complete by checking if the completed property
        # in results is not equal to the contacted property

        if not detail_search_status:
            self.connection.check_status_of_detail_search(id_)
        else:
            self.connection.retrieve_results_for_detail_search()

        try:
            success = self.connection.retrieve_results_for_detail_search()
            data = komand.helper.clean(success.json())
            message = "message_placeholder"
            return {
                Output.SUCCESS: success,
                Output.MESSAGE: komand.helper.clean(message)
                Output.EVENTINFO: data["eventInfo"]
            }

        except ValueError:
            self.logger.error(success.text)
            raise Exception(
                f"Error: Received an unexpected response"
                f" (non-JSON or no response was received). Raw response in logs."
            )
        if result.status_code == 200:
            return {
                Output.SUCCESS: data["success"],
                Output.MESSAGE: data["message"],
                Output.EVENTINFO: data["eventInfo"],
            }
        if result.status_code in range(400, 499):
            raise Exception(
                f"Carbon Black returned a {result.status_code} code."
                f" Verify the token and host configuration in the connection. Response was: {result.text}"
            )
        if result.status_code in range(500, 599):
            raise Exception(
                f"Carbon Black returned a {result.status_code} code."
                f" If the problem persists please contact support for help. Response was: {result.text}"
            )
        self.logger.error(result.text)
        raise Exception(
            f"An unknown error occurred."
            f" Carbon Black returned a {result.status_code} code. Contact support for help. Raw response in logs."
        )

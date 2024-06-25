import insightconnect_plugin_runtime
import time
from datetime import datetime
from .schema import PollOatListInput, PollOatListOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import json
import pytmv1


class PollOatList(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="poll_oat_list",
            description=Component.DESCRIPTION,
            input=PollOatListInput(),
            output=PollOatListOutput(),
        )

    def run(self, params={}):
        """Run the trigger"""
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        detected_start_date_time = params.get(Input.DETECTED_START_DATE_TIME)
        detected_end_date_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")  # Current time in UTC
        ingested_start_date_time = params.get(Input.INGESTED_START_DATE_TIME)
        ingested_end_date_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")  # Current time in UTC
        fields = params.get(Input.FIELDS)
        query_op = params.get(Input.QUERY_OP)
        # Choose enum
        if "or" in query_op:
            query_op = pytmv1.QueryOp.OR
        elif "and" in query_op:
            query_op = pytmv1.QueryOp.AND

        while True:
            # Make sure response contains < 5K entries
            self.logger.info("Checking Response Size...")
            count = client.oat.list(
                detected_start_date_time=detected_start_date_time,
                detected_end_date_time=detected_end_date_time,
                ingested_start_date_time=ingested_start_date_time,
                ingested_end_date_time=ingested_end_date_time,
                top=1,
                op=query_op,
                **fields,
            )
            if "error" in count.result_code.lower():
                raise PluginException(
                    cause="An error occurred while getting OAT count.",
                    assistance="Please check your inputs and try again.",
                    data=count.error,
                )
            total_count = count.response.total_count
            if total_count > 50:
                raise PluginException(
                    cause="Attempted query is over-sized (more than 50 results).",
                    assistance="Please refine your inputs to reduce search size and try again.",
                )
            new_oats = []
            # Get OATs List
            self.logger.info("Getting OATs List...")
            response = client.oat.consume(
                lambda oat: new_oats.append(json.loads(oat.model_dump_json())),
                detected_start_date_time=detected_start_date_time,
                detected_end_date_time=detected_end_date_time,
                ingested_start_date_time=ingested_start_date_time,
                ingested_end_date_time=ingested_end_date_time,
                top=50,
                op=query_op,
                **fields,
            )
            if "error" in response.result_code.lower():
                raise PluginException(
                    cause="An error occurred while polling OATs.",
                    assistance="Please check your inputs and try again.",
                    data=response.error,
                )
            # Return results
            self.logger.info("Returning Results...")
            self.send({Output.TOTAL_COUNT: len(new_oats), Output.OATS: new_oats})
            # Sleep before next run
            time.sleep(params.get(Input.INTERVAL, 1800))
            # Update start_date_time and end_date_time for the next iteration
            detected_start_date_time = detected_end_date_time
            detected_end_date_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")  # Current time in UTC
            ingested_start_date_time = ingested_end_date_time
            ingested_end_date_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")  # Current time in UTC

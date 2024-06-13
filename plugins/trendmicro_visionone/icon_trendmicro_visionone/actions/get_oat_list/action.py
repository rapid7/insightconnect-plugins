import insightconnect_plugin_runtime
from .schema import GetOatListInput, GetOatListOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import json
import pytmv1


class GetOatList(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_oat_list",
            description=Component.DESCRIPTION,
            input=GetOatListInput(),
            output=GetOatListOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        detected_start_date_time = params.get(Input.DETECTED_START_DATE_TIME)
        detected_end_date_time = params.get(Input.DETECTED_END_DATE_TIME)
        ingested_start_date_time = params.get(Input.INGESTED_START_DATE_TIME)
        ingested_end_date_time = params.get(Input.INGESTED_END_DATE_TIME)
        fields = params.get(Input.FIELDS)
        query_op = params.get(Input.QUERY_OP)
        # Choose enum
        if "or" in query_op:
            query_op = pytmv1.QueryOp.OR
        elif "and" in query_op:
            query_op = pytmv1.QueryOp.AND

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
        # Make Action API Call
        self.logger.info("Creating OATs list...")
        try:
            client.oat.consume(
                lambda oat: new_oats.append(json.loads(oat.model_dump_json())),
                detected_start_date_time=detected_start_date_time,
                detected_end_date_time=detected_end_date_time,
                ingested_start_date_time=ingested_start_date_time,
                ingested_end_date_time=ingested_end_date_time,
                top=50,
                op=query_op,
                **fields,
            )
        except Exception as error:
            raise PluginException(
                cause="An error occurred while trying to get the OATs list.",
                assistance="Please check the provided parameters and try again.",
                data=error,
            )
        # Return results
        self.logger.info("Returning Results...")
        return {Output.TOTAL_COUNT: len(new_oats), Output.OATS: new_oats}

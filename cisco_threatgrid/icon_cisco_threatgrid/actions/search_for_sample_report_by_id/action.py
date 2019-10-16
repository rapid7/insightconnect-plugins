import komand
from komand.exceptions import PluginException
from komand.exceptions import ConnectionTestException
from .schema import SearchForSampleReportByIdInput, SearchForSampleReportByIdOutput, Input, Output, Component
# Custom imports below
import json


class SearchForSampleReportById(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_for_sample_report_by_id',
                description=Component.DESCRIPTION,
                input=SearchForSampleReportByIdInput(),
                output=SearchForSampleReportByIdOutput())

    def run(self, params={}):
        sample_id = params.get(Input.SAMPLE_ID)

        result = self.connection.api.search_id(q=sample_id)

        # The way ThreatGrid works is kind of odd, they don't have an enpoint to just get an ID.
        # I'm searching for the ID using the terms, however, every once in a while it'll return more than one hit
        # this will make sure we got what the user wanted.
        try:
            items = result.get("data").get("items")
        except json.JSONDecodeError as e:
            raise PluginException(
                preset=ConnectionTestException.Preset.INVALID_JSON,
                data=f"{result.text}\n Exception: {e}"
            )

        for item in items:
            current_sample = item.get("item").get("sample")
            self.logger.info(f"Comparing {current_sample} with {sample_id}")
            if sample_id == item.get("item").get("sample"):
                self.logger.info("Sample found.")
                return {Output.SAMPLE_REPORT: komand.helper.clean(item.get("item"))}

        raise PluginException(cause="Sample ID not found.",
                              assistance="Please check your sample ID and trying again.")

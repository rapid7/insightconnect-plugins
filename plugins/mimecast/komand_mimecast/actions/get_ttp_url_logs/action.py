import insightconnect_plugin_runtime
from .schema import GetTtpUrlLogsInput, GetTtpUrlLogsOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
import re
from komand_mimecast.util.constants import DATA_FIELD, META_FIELD, PAGINATION_FIELD, URL_FIELD


class GetTtpUrlLogs(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_ttp_url_logs",
            description=Component.DESCRIPTION,
            input=GetTtpUrlLogsInput(),
            output=GetTtpUrlLogsOutput(),
        )

    def run(self, params={}):
        from_ = params.get(Input.FROM)
        to_ = params.get(Input.TO)
        url_to_filter = params.get(Input.URL_TO_FILTER)
        max_pages = params.get(Input.MAX_PAGES, 1)

        data = {
            "route": params.get(Input.ROUTE),
            "scanResult": params.get(Input.SCAN_RESULT),
            "oldestFirst": params.get(Input.OLDEST_FIRST, False),
        }

        if to_:
            data["to"] = to_
        if from_:
            data["from"] = from_

        meta = {PAGINATION_FIELD: {"pageSize": params.get(Input.PAGE_SIZE, 10)}}

        responses = []

        for _ in range(max_pages):
            response = self.connection.client.get_ttp_url_logs(data, meta)
            responses.append(response)

            if (
                "meta" not in response
                or PAGINATION_FIELD not in response[META_FIELD]
                or "pageToken" not in response[META_FIELD][PAGINATION_FIELD]
            ):
                break
            meta[PAGINATION_FIELD]["pageToken"] = response[META_FIELD][PAGINATION_FIELD]["next"]

        try:
            output = []
            if url_to_filter:
                for response in responses:
                    for log in response[DATA_FIELD][0]["clickLogs"]:
                        if re.search(f"{url_to_filter}", log.get(URL_FIELD)):
                            output.append(log)
            else:
                for response in responses:
                    output.extend(response.get(DATA_FIELD)[0]["clickLogs"])
        except (KeyError, IndexError):
            self.logger.error(responses)
            raise PluginException(
                cause="Unexpected output format.",
                assistance="The output from Mimecast was not in the expected format. Please contact support for help.",
                data=responses,
            )

        return {Output.CLICK_LOGS: output}

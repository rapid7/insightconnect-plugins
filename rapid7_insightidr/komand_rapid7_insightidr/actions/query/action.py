import komand
from .schema import QueryInput, QueryOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
from komand_rapid7_insightidr.util.endpoints import QueryLogs
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
import json
import time


class Query(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='query',
            description=Component.DESCRIPTION,
            input=QueryInput(),
            output=QueryOutput())

    def run(self, params={}):
        time_now = int(time.time())
        request = ResourceHelper(self.connection.session, self.logger)
        request_params = {
            "from": (time_now - 7776000) * 1000,
            "to": time_now * 1000
        }
        response = request.resource_request(
            QueryLogs.get_query_logs(self.connection.url, params.get(Input.ID)),
            'get',
            params=request_params
        )

        try:
            result = json.loads(response['resource'])
            if response["status"] == 202:
                response = request.resource_request(result["links"][0]["href"], 'get', params=request_params)
                result = json.loads(response['resource'])
        except json.decoder.JSONDecodeError:
            self.logger.error(f'InsightIDR response: {response}')
            raise PluginException(cause='The response from InsightIDR was not in the correct format.',
                                  assistance='Contact support for help. See log for more details')

        try:
            result_response = []
            events = result.get("events", [])
            if events:
                for event in events:
                    event["message"] = event["message"].replace('\n', '\\n')
                    result_response.append(event)

            return {
                Output.EVENTS: result_response
            }
        except KeyError:
            self.logger.error(result)
            raise PluginException(cause='The response from InsightIDR was not in the correct format.',
                                  assistance='Contact support for help. See log for more details')

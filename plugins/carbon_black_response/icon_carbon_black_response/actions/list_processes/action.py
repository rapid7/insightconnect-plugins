import insightconnect_plugin_runtime
from .schema import ListProcessesInput, ListProcessesOutput

# Custom imports below


class ListProcesses(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_processes",
            description="List Carbon Black processes with given parameters",
            input=ListProcessesInput(),
            output=ListProcessesOutput(),
        )

    def run(self, params={}):
        query_params = [
            ("q", params.get("query", "")),
            ("rows", params.get("rows", 10)),
            ("start", params.get("start", 0)),
        ]

        try:
            # TODO: Verify this is returning useful data
            results = self.connection.carbon_black.get_object("/api/v1/process", query_parameters=query_params)[
                "results"
            ]
        except Exception as ex:
            self.logger.error("Failed to list process: %s", ex)
            raise ex

        results = insightconnect_plugin_runtime.helper.clean(results)

        return {"processes": results}

    def test(self):
        if self.connection.test():
            return {}

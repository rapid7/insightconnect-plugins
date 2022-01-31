import insightconnect_plugin_runtime
from .schema import ListSensorsInput, ListSensorsOutput

# Custom imports below


class ListSensors(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_sensors",
            description="List all sensors",
            input=ListSensorsInput(),
            output=ListSensorsOutput(),
        )

    def run(self, params={}):
        query_params = [
            ("hostname", params.get("hostname", "")),
            ("ip", params.get("ip", "")),
            ("groupid", params.get("groupid", "")),
        ]
        id = params.get("id", "")
        try:
            if not id:
                results = self.connection.carbon_black.get_object("/api/v1/sensor", query_parameters=query_params)
            else:
                # Returns single sensor if ID is supplied
                results = []
                results.append(
                    self.connection.carbon_black.get_object("/api/v1/sensor/%s" % id, query_parameters=query_params)
                )
            updated_results = []
            for result in results:
                result["found"] = True
                updated_results.append(result)
            results = updated_results
        except Exception as ex:
            results = []
            results.append({"computer_name": params.get("hostname"), "found": False})

        results = insightconnect_plugin_runtime.helper.clean(results)

        return {"sensors": results}

    def test(self):
        if self.connection.test():
            return {}

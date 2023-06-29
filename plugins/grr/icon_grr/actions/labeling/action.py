import insightconnect_plugin_runtime
from .schema import LabelingInput, LabelingOutput, Input, Output


# Custom imports below


class Labeling(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="labeling",
            description="Looks for exposed secrets in the git commit history and branches",
            input=LabelingInput(),
            output=LabelingOutput(),
        )
        self.grrapi = None

    def run(self, params={}):
        self.grrapi = self.connection.grrapi
        query = params.get(Input.QUERY, "")
        label = params.get(Input.LABEL, [])
        label = [str(x) for x in label]
        search_results = self.grrapi.SearchClients(query)
        try:
            for client in search_results:
                type_client = type(client)
                if isinstance(client, type_client):
                    return {Output.RESULTS: "No clients found with the given query"}
                client.AddLabels(label)
        except Exception as error:
            self.logger.error(error)
        return {Output.RESULTS: "All clients have been labeled"}

    def test(self):
        self.grrapi = self.connection.grrapi
        if self.grrapi:
            return {Output.RESULTS: "Ready to label"}
        if not self.grrapi:
            return {Output.RESULTS: "Not ready. Please check your connection with the GRR Client"}

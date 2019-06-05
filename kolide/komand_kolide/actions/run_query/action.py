import komand
from .schema import RunQueryInput, RunQueryOutput, Input, Output
# Custom imports below


class RunQuery(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='run_query',
                description='Run selected query on fleet',
                input=RunQueryInput(),
                output=RunQueryOutput())

    def run(self, params={}):
        query = params.get(Input.QUERY)
        hosts = params.get(Input.HOSTS)
        labels = params.get(Input.LABELS)

        payload = {
            "query": query,
            "selected": {
                "hosts": hosts,
                "labels": labels
            }
        }

        response = self.connection.api.run_query(payload=payload)

        return {Output.RESULTS: response}

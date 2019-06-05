import komand
from .schema import CreateQueryInput, CreateQueryOutput, Input, Output
# Custom imports below


class CreateQuery(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_query',
                description='Create a new query in Kolide',
                input=CreateQueryInput(),
                output=CreateQueryOutput())

    def run(self, params={}):
        name = params.get(Input.NAME)
        description = params.get(Input.DESCRIPTION)
        query = params.get(Input.QUERY)

        payload = {
            "name": name,
            "description": description,
            "query": query
        }

        response = self.connection.api.create_query(payload=payload)

        return {Output.RESULTS: response}

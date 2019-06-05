import komand
from .schema import GetQueryInput, GetQueryOutput, Input, Output
# Custom imports below


class GetQuery(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="get_query",
                description="Gets query details on past queries by specified query ID",
                input=GetQueryInput(),
                output=GetQueryOutput())

    def run(self, params={}):
        queryid = params.get(Input.QUERYID)

        response = self.connection.api.get_query(queryID=queryid)
        return {Output.RESULTS: response}

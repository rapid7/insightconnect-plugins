import komand
from .schema import GetSolutionInput, GetSolutionOutput, Input, Output, Component
# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_helper import ResourceHelper


class GetSolution(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_solution',
                description=Component.DESCRIPTION,
                input=GetSolutionInput(),
                output=GetSolutionOutput())

    def run(self, params={}):
        resource_helper = ResourceHelper(self.connection.session, self.logger)
        id = params.get('id')
        endpoint = endpoints.Vulnerability.solution(self.connection.console_url, id)
        self.logger.info(f"Using {endpoint}...")
        response = resource_helper.resource_request(endpoint=endpoint)

        return {"solution": response}

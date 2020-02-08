import komand
from .schema import GetFactorsInput, GetFactorsOutput, Input, Output, Component
# Custom imports below


class GetFactors(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_factors',
                description=Component.DESCRIPTION,
                input=GetFactorsInput(),
                output=GetFactorsOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}

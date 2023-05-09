import insightconnect_plugin_runtime
from .schema import ResetFactorsInput, ResetFactorsOutput, Input, Output, Component

# Custom imports below


class ResetFactors(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="reset_factors",
            description=Component.DESCRIPTION,
            input=ResetFactorsInput(),
            output=ResetFactorsOutput(),
        )

    def run(self, params={}):
        login = params.get(Input.LOGIN)
        user_id = self.connection.api_client.get_user_id(login)
        return {
            Output.SUCCESS: self.connection.api_client.reset_factors(user_id),
            Output.USERID: user_id,
            Output.LOGIN: login,
        }

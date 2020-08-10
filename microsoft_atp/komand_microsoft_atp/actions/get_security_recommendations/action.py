import insightconnect_plugin_runtime
from .schema import GetSecurityRecommendationsInput, GetSecurityRecommendationsOutput, Input, Output, Component


class GetSecurityRecommendations(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_security_recommendations',
            description=Component.DESCRIPTION,
            input=GetSecurityRecommendationsInput(),
            output=GetSecurityRecommendationsOutput())

    def run(self, params={}):
        machine_id = self.connection.client.find_first_machine(params.get(Input.MACHINE)).get("id")
        self.logger.info(f"Attempting to get security recommendations for machine ID: {machine_id}.")

        return {
            Output.RECOMMENDATIONS: insightconnect_plugin_runtime.helper.clean(
                self.connection.client.get_security_recommendations(machine_id).get("value")
            )
        }

import insightconnect_plugin_runtime
from .schema import ListCountriesInput, ListCountriesOutput, Input, Output, Component
# Custom imports below


class ListCountries(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="list_countries",
                description=Component.DESCRIPTION,
                input=ListCountriesInput(),
                output=ListCountriesOutput())

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        # END INPUT BINDING - DO NOT REMOVE

        self.logger.info('Running server_lia_countries')
        countries = self.connection.api.server_lia_countries()

        return {"countries": countries}

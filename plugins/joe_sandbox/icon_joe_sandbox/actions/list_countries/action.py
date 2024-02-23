import insightconnect_plugin_runtime
from .schema import ListCountriesInput, ListCountriesOutput, Output

# Custom imports below


class ListCountries(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_countries",
            description="Retrieve a list of localized internet anonymization countries",
            input=ListCountriesInput(),
            output=ListCountriesOutput(),
        )

    def run(
        self,
    ):
        countries = self.connection.api.server_lia_countries()
        return {Output.COUNTRIES: countries}

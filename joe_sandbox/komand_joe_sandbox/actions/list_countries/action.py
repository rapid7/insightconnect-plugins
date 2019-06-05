import komand
from .schema import ListCountriesInput, ListCountriesOutput, Input, Output
# Custom imports below


class ListCountries(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_countries',
                description='Retrieve a list of localized internet anonymization countries',
                input=ListCountriesInput(),
                output=ListCountriesOutput())

    def run(self, params={}):
        countries = self.connection.api.server_lia_countries()
        return {'countries': countries}

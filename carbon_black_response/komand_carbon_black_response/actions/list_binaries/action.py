import komand
from .schema import ListBinariesInput, ListBinariesOutput
# Custom imports below


class ListBinaries(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_binaries',
                description='List Carbon Black binaries with given parameters',
                input=ListBinariesInput(),
                output=ListBinariesOutput())

    def run(self, params={}):
        try:
            query_params = [
                ("q", params.get("query", "")),
                ("rows", params.get("rows", 10)),
                ("start", params.get("start", 0))
            ]

            results = self.connection.carbon_black.get_object("/api/v1/binary", query_parameters=query_params)
        except Exception as ex:
            self.logger.error('Failed to get binaries: %s', ex)
            raise ex

        results = komand.helper.clean(results["results"])

        return {'binaries': results}

    def test(self):
        if self.connection.test():
            return {}

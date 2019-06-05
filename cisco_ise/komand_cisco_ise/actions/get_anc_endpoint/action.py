import komand
from .schema import GetAncEndpointInput, GetAncEndpointOutput, Input, Output
# Custom imports below


class GetAncEndpoint(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_anc_endpoint',
                description='Returns ANC information based on the ID supplied',
                input=GetAncEndpointInput(),
                output=GetAncEndpointOutput())

    def run(self, params={}):
        endpoint_mac = params.get(Input.MAC)

        all_endpoints = self.connection.ers.get_anc_endpoint_all()
        try:
            for endpoint in all_endpoints["SearchResult"]["resources"]:
                results = self.connection.ers.get_anc_endpoint(endpoint["id"])
                ersanc_endpoint = results["ErsAncEndpoint"]
                if "macAddress" in ersanc_endpoint and ersanc_endpoint["macAddress"] == endpoint_mac:
                    return {Output.RESULTS: ersanc_endpoint}
        except Exception as e:
            raise Exception(f"Error has occurred, response: {e}")
        self.logger.info(f"MAC {endpoint_mac} was not found!")

        return {Output.RESULTS: {}}

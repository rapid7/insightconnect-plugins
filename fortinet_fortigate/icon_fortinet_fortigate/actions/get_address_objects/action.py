import komand
from .schema import GetAddressObjectsInput, GetAddressObjectsOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException

class GetAddressObjects(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_address_objects',
                description=Component.DESCRIPTION,
                input=GetAddressObjectsInput(),
                output=GetAddressObjectsOutput())

    def run(self, params={}):
        endpoint = f"https://{self.connection.host}/api/v2/cmdb/firewall/address"
        filter = params.get(Input.NAME_FILTER, "")

        params=None
        if filter:
            params = {
                "filter": f"name=@{filter}"
            }

        result = self.connection.session.get(endpoint, verify=self.connection.ssl_verify, params=params)

        try:
            result.raise_for_status()
        except Exception as e:
            raise PluginException(cause=f"Get address objects failed for {endpoint}",
                                  assistance=result.text,
                                  data=e)

        results = result.json().get("results")
        return {Output.ADDRESS_OBJECTS: komand.helper.clean(results)}

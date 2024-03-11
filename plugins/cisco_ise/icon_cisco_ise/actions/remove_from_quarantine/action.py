import insightconnect_plugin_runtime

from .schema import Component, Input, Output, RemoveFromQuarantineInput, RemoveFromQuarantineOutput

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class RemoveFromQuarantine(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="remove_from_quarantine",
            description=Component.DESCRIPTION,
            input=RemoveFromQuarantineInput(),
            output=RemoveFromQuarantineOutput(),
        )

    def run(self, params={}):
        mac_address = params.get(Input.MAC_ADDRESS)

        self.connection.ers.clean_anc_end_point(mac_address=mac_address)
        results = self.connection.ers.get_anc_endpoint()

        try:
            if results["SearchResult"]["total"] == 0:
                return {Output.SUCCESS: True}
            results = results["SearchResult"]["resources"]
        except KeyError:
            self.logger.error(f"Raw results from ANC endpoint query: {results}")
            raise PluginException(cause="Results contained improperly formatted data. See log for more details")
        except Exception as error:
            self.logger.error(error)
            self.logger.error(f"Raw results from ANC endpoint query: {results}")
            raise PluginException(cause="Unexpected error. See log for more details")

        try:
            for element in results:
                find = self.connection.ers.get_anc_endpoint(element["id"])
                if find["ErsAncEndpoint"]["macAddress"] == mac_address:
                    self.logger.error(results)
                    raise PluginException(cause=f"{mac_address} was not removed. See log for more details")
            return {Output.SUCCESS: True}
        except KeyError:
            self.logger.error(f"Raw results from ANC endpoint query: {results}")
            self.logger.error(f"Raw results from ANC endpoint query on IDs: {element}")
            raise
        except Exception as error:
            self.logger.error(error)
            self.logger.error(f"Raw results from ANC endpoint query: {results}")
            self.logger.error(f"Raw results from ANC endpoint query on IDs: {element}")
            raise

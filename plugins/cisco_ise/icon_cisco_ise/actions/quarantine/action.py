import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import Component, Input, Output, QuarantineInput, QuarantineOutput

# Custom imports below


class Quarantine(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="quarantine",
            description=Component.DESCRIPTION,
            input=QuarantineInput(),
            output=QuarantineOutput(),
        )

    def run(self, params={}):
        mac_address = params.get(Input.MAC_ADDRESS)
        policy = params.get(Input.POLICY)

        self.connection.ers.apply_anc_endpoint_mac(mac_address, policy)
        results = self.connection.ers.get_anc_endpoint()

        try:
            results = results["SearchResult"]["resources"]
        except KeyError:
            self.logger.error(f"Raw results from ANC endpoint query: {results}")
            raise
        except Exception as error:
            self.logger.error(error)
            self.logger.error(f"Raw results from ANC endpoint query: {results}")
            raise

        try:
            for element in results:
                find = self.connection.ers.get_anc_endpoint(element["id"])
                if find["ErsAncEndpoint"]["macAddress"] == mac_address:
                    return {Output.ERS_ANC_ENDPOINT: find["ErsAncEndpoint"]}
        except KeyError:
            self.logger.error(f"Raw results from ANC endpoint query: {results}")
            self.logger.error(f"Raw results from ANC endpoint query on IDs: {element}")
            raise
        except Exception as error:
            self.logger.error(error)
            self.logger.error(f"Raw results from ANC endpoint query: {results}")
            self.logger.error(f"Raw results from ANC endpoint query on IDs: {element}")
            raise

        self.logger.error(f"MAC address, {mac_address}")
        self.logger.error(f"Policy, {policy}")
        self.logger.error(f"Raw results from ANC endpoint query, {results}")
        raise PluginException(
            cause="Cisco ISE did not return a result",
            assistance="Check your configuration settings and confirm your policy exists and "
            "MAC address are correct",
        )

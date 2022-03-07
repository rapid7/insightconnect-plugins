from .scan_results import ScanResults
from insightconnect_plugin_runtime.exceptions import PluginException
import validators


# Return the first element of an array, otherwise None.
def first(array):
    return next(iter(array or []), None)


def generate_payload(results, operation, max_page_size):
    scan_results = ScanResults(max_page_size)

    for result in results:
        ip_address = result.get("host", {}).get("ip_address", "")
        if ip_address:
            if validators.ipv4(ip_address) or validators.ipv6(ip_address):
                scan_results.add_scan_result(ip_address, result, operation)
            else:
                raise PluginException(
                    cause=f"The provided IP address {ip_address} is invalid.",
                    assistance="Please provide a valid IP address for the host and try again.",
                )
        else:
            raise PluginException(
                cause="No IP address provided.", assistance="Please provide an IP address for the host and try again."
            )

    return scan_results.commands

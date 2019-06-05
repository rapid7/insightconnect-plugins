from .scan_results import ScanResults


# Return the first element of an array, otherwise None.
def first(array):
    return next(iter(array or []), None)


# Generates correct payload that can be sent to Firepower
def generate_payload(results, operation, max_page_size):
    scan_results = ScanResults(max_page_size)

    for result in results:
        host = result.get('host', {})
        ip_address = host.get('ip_address', '')
        if not ip_address:
            raise Exception("No IP address provided.")
        scan_results.add_scan_result(ip_address, result, operation)

    return scan_results.commands

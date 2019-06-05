import komand
from .schema import ScanInput, ScanOutput
# Custom imports below
from nmap import PortScanner, PortScannerError
import komand.helper


class Scan(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='scan',
                description='Run nmap scan',
                input=ScanInput(),
                output=ScanOutput())

    def run(self, params={}):
        hosts_to_scan = params.get("hosts")
        ports_to_scan = params.get("ports")
        nmap_args = params.get("arguments")
        sudo = params.get("sudo")  # defaulted to False

        if not len(ports_to_scan):
            ports_to_scan = None

        if not len(nmap_args):
            nmap_args = None

        scanner = PortScanner()

        try:
            scanner.scan(hosts=hosts_to_scan,
                         ports=ports_to_scan,
                         arguments=nmap_args,
                         sudo=sudo)
        except PortScannerError as e:
            self.logger.error("An error occurred: %s" % e)
        else:
            scanned_hosts = scanner.all_hosts()  # grab hosts that were scanned
            results = list(map(lambda host: scanner[host], scanned_hosts))  # create list of scan results

            results = komand.helper.clean(results)

            return {"result": results}

    def test(self):
        scanner = PortScanner()
        scanner.scan(hosts="localhost", arguments="-T 4 --max-retries 0 --max-rtt-timeout 100ms")
        return {"result": []}

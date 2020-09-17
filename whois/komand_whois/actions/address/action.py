import insightconnect_plugin_runtime
from .schema import AddressInput, AddressOutput, Input
import re


class Address(insightconnect_plugin_runtime.Action):
    ARIN, LACNIC, APNIC, RIPE = "arin", "lacnic", "apnic", "ripe"

    NORMALIZATION_MAP = {
        RIPE: {
            "netname": "netname",
            "nettype": "status",
            "netrange": "inetnum",
            "organization": "organisation",
            "orgname": "descr",
            "regdate": "created",
            "updated": "last-modified",
            "address": "address",
            "country": "country",
            "org_abuse_email": "abuse-mailbox"
        },
        ARIN: {
            "netname": "NetName",
            "nettype": "NetType",
            "netrange": "NetRange",
            "cidr": "CIDR",
            "organization": "Organization",
            "orgname": "OrgName",
            "regdate": "RegDate",
            "update": "Updated",
            "address": "Address",
            "city": "City",
            "postal": "PostalCode",
            "state": "StateProv",
            "country": "Country",
            "org_abuse_email": "OrgAbuseEmail",
            "org_abuse_phone": "OrgAbusePhone",
            "org_tech_email": "OrgTechEmail",
            "org_tech_phone": "OrgTechPhone",
        },
        LACNIC: {
            "netname": "ownerid",
            "nettype": "status",
            "netrange": "inetnum",
            "cidr": "inetnum",
            "organization": "organisation",
            "orgname": "owner",
            "regdate": "created",
            "update": "changed",
            "address": "address",
            "country": "country",
            "org_abuse_email": "e-mail",
            "org_abuse_phone": "phone",
        },
        APNIC: {
            "netname": "netname",
            "nettype": "status",
            "netrange": "inetnum",
            "cidr": "inetnum",
            "organization": "organisation",
            "orgname": "descr",
            "update": "last-modified",
            "address": "address",
            "country": "country",
            "org_abuse_email": "e-mail",
            "org_abuse_phone": "phone",
        }
    }

    def __init__(self):
        super(self.__class__, self).__init__(
                name="address",
                description="Whois IP Lookup",
                input=AddressInput(),
                output=AddressOutput())

    def run(self, params={}):
        binary = "/usr/bin/whois"
        cmd = "%s %s" % (binary, params.get("address"))
        stdout = insightconnect_plugin_runtime.helper.exec_command(cmd)["stdout"]
        stdout = stdout.decode('utf-8')
        results = self.parse_stdout(params.get(Input.REGISTRAR), stdout=stdout)
        results = insightconnect_plugin_runtime.helper.clean_dict(results)

        if not results:
            self.logger.error("Error: Request did not return any data")
        return results

    def _get_stdout_pairs(self, stdout):
        """
        Run a regex against the stdout string to extract pairings
        :param stdout: Stdout from the whois query
        :return: Pairs
        """
        regex = r"\S*:\s*.*"
        r = re.compile(pattern=regex, flags=re.IGNORECASE | re.MULTILINE)
        results = r.findall(string=stdout)

        pairs = dict()
        for result in results:
            pair = list(map(str.strip, result.split(":")))
            pairs[pair[0]] = pair[1]

        return pairs

    def _get_registry(self, stdout):
        lines = stdout.splitlines()[:4]
        if list(filter(lambda l: self.ARIN in l.lower(), lines)):
            registry = self.ARIN
        elif list(filter(lambda l: self.LACNIC in l.lower(), lines)):
            registry = self.LACNIC
        elif list(filter(lambda l: self.APNIC in l.lower(), lines)):
            registry = self.APNIC
        elif list(filter(lambda l: self.RIPE in l.lower(), lines)):
            registry = self.RIPE
        else:
            self.logger.info("Warning: No WHOIS registry detected from stdout, defaulting to ARIN...")
            registry = self.ARIN

        return registry

    def _load_normalization_map(self, refer):
        if refer not in self.NORMALIZATION_MAP.keys():
            self.logger.info("Warning: No normalization map found for: %s\n"
                             "Please contact support with the IP address used as input to this action." % refer)
        return self.NORMALIZATION_MAP[refer]

    def parse_stdout(self, registrar, stdout):
        pairs = self._get_stdout_pairs(stdout)
        if not registrar or registrar == "Autodetect":
            registry = self._get_registry(stdout=stdout)
        else:
            registry = registrar.lower()

        self.logger.info("Info: Using registry: %s" % registry)

        loaded_map = self._load_normalization_map(refer=registry)

        output = dict()
        for p_key, p_value in pairs.items():
            for n_key, n_value in loaded_map.items():
                if p_key == n_value:
                    output[n_key] = p_value

        return output

    def test(self):
        # TODO: Implement test function
        return {}

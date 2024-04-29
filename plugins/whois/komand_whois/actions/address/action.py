import insightconnect_plugin_runtime
from .schema import AddressInput, AddressOutput, Input, Output
import re
import validators
from insightconnect_plugin_runtime.exceptions import PluginException


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
            "org_abuse_email": "abuse-mailbox",
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
        },
    }

    def __init__(self):
        super(self.__class__, self).__init__(
            name="address",
            description="Whois IP Lookup",
            input=AddressInput(),
            output=AddressOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        address = params.get(Input.ADDRESS, "")
        registrar = params.get(Input.REGISTRAR, "")
        # END INPUT BINDING - DO NOT REMOVE

        # Validate user input
        if not any(validator(address, cidr=False) for validator in (validators.ipv4, validators.ipv6)):
            raise PluginException(
                cause="Invalid IPv4 or IPv6 address specified for a field 'Address'.",
                assistance="Please enter a valid IPv4 or IPv6 address and try again.",
            )

        command = f"/usr/bin/whois {address}"
        stdout = insightconnect_plugin_runtime.helper.exec_command(command)["stdout"]
        try:
            stdout = stdout.decode("utf-8")
        except UnicodeDecodeError:
            stdout = stdout.decode("iso-8859-1")
        results = self.parse_stdout(registrar, stdout=stdout)
        results = insightconnect_plugin_runtime.helper.clean_dict(results)

        if not results:
            raise PluginException(
                cause="Error: Request did not return any data.",
                assistance="Please check provided address and try again.",
            )
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

        pairs = {}
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
        if refer not in self.NORMALIZATION_MAP:
            self.logger.info(
                f"Warning: No normalization map found for: {refer}\n"
                "Please contact support with the IP address used as input to this action."
            )
        return self.NORMALIZATION_MAP[refer]

    def parse_stdout(self, registrar, stdout):
        pairs = self._get_stdout_pairs(stdout)
        if not registrar or registrar == "Autodetect":
            registry = self._get_registry(stdout=stdout)
        else:
            registry = registrar.lower()

        self.logger.info(f"Info: Using registry: {registry}")
        loaded_map = self._load_normalization_map(refer=registry)

        output = {}
        for p_key, p_value in pairs.items():
            for n_key, n_value in loaded_map.items():
                if p_key == n_value:
                    output[n_key] = p_value

        return output

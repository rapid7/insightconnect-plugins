import json
import os


class Util:
    @staticmethod
    def read_file_to_string(filename):
        with open(filename) as my_file:
            return my_file.read()

    @staticmethod
    def load_parameters(filename):
        return json.loads(
            Util.read_file_to_string(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{filename}.json.resp")
            )
        )

    @staticmethod
    def mocked_run(*args, **kwargs):
        class MockRun:
            def __init__(self, filename, error):
                if error:
                    self.stdout = b""
                    self.stderr = error
                else:
                    self.stdout = self.load_data(filename)
                    self.stderr = error

            @staticmethod
            def load_data(filename):
                return Util.read_file_to_string(
                    os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{filename}.json.resp")
                ).encode()

        if args[0] == ["dnstwist", "-r", "-s", "-m", "-f", "json", "rapid7.com"]:
            return MockRun("check_for_squatters_ssdeep_and_mxcheck", b"")
        if args[0] == ["dnstwist", "--registered", "--whois", "-f", "json", "rapid7.com"]:
            return MockRun("check_for_squatters_whois_flag", b"")
        if args[0] == ["dnstwist", "-r", "-g", "-f", "json", "rapid7.com"]:
            return MockRun("check_for_squatters_geoip_flag", b"")
        if args[0] == ["dnstwist", "--registered", "-f", "json", "rapid7.com"]:
            return MockRun("check_for_squatters_with_flag", b"")
        if args[0] == ["dnstwist", "-f", "json", "rapid7.com"]:
            return MockRun("check_for_squatters_without_flag", b"")
        if args[0] == ["dnstwist", "-f", "json", "rapid7"]:
            return MockRun("check_for_squatters_with_invalid_domain", b"")
        if args[0] == ["dnstwist", "--invalid_flag", "-f", "json", "rapid7.com"]:
            return MockRun(
                "check_for_squatters_invalid_flag",
                b"usage: /usr/local/bin/dnstwist [OPTION]... DOMAIN\ndnstwist: error: unrecognized arguments: --invalid_flag\n",
            )
        raise Exception("Unimplemented test")

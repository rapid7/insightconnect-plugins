import komand
from .schema import ScanFileInput, ScanFileOutput
# Custom imports below
import yara
import base64


class ScanFile(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='scan_file',
                description='Scans file using Yara',
                input=ScanFileInput(),
                output=ScanFileOutput())

    def run(self, params={}):
        yara_results = []
        input_rules = params["rules"]
        input_file = params["file"]

        # Decode and builds rules
        def build_rules(encoded_rules):
            try:
                encoded_rules = base64.b64decode(encoded_rules)
                # Build Yara rules - loads one file of rules
                yara_rules = yara.compile(source=encoded_rules.decode())
                return yara_rules
            except Exception as e:
                self.logger.error("An error has occurred while building rules", e)
                raise

        # Decode file
        def build_file(encoded_file):
            try:
                data = base64.b64decode(encoded_file)
                return data
            except Exception as e:
                self.logger.error("An error has occurred while building file", e)
                raise

        # Generates matches based off rules and the files to scan
        def matches(built_rules, built_files):
            try:
                rules = built_rules
                files = built_files
                findings = rules.match(data=files)
                return findings
            except Exception as e:
                self.logger.error("An error has occurred while checking for matches", e)
                raise

        # Results from the matches
        try:
            results = matches(build_rules(input_rules), build_file(input_file))
        except Exception as e:
            self.logger.error("An error has occurred while running matches", e)
            raise

            # Appending each output of the results
        for result in results:
            # Sanitize tuple in stings for dict
            san_strings = []
            for tup in result.strings:
                for tup_string in tup:
                    if isinstance(tup_string, bytes):
                        san_strings.append(tup_string.decode())
                    else:
                        san_strings.append(str(tup_string))

            yara_results.append(
                {
                    "meta":result.meta,
                    "namespace": result.namespace,
                    "rule": result.rule,
                    "string": san_strings,
                    "tags": result.tags
                }
            )

        # Returning a array of objects
        return {"results": yara_results}

    def test(self):
        # Checks to make sure Yara loads
        try:
            version = yara.YARA_VERSION
        except ImportError:
            raise ImportError("Error occurred trying to import Yara")
        return {"results": [{"success": True}]}

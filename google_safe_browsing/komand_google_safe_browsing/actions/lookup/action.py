import komand
from .schema import LookupInput, LookupOutput
# Custom imports below
import json
import requests
import jsonpickle
from komand_google_safe_browsing.util.objects import *


class Lookup(komand.Action):

    __URL = "https://safebrowsing.googleapis.com/v4/threatMatches:find"

    def __init__(self):
        super(self.__class__, self).__init__(
                name='lookup',
                description='Lookup URL in Safe Browsing service',
                input=LookupInput(),
                output=LookupOutput())

    def run(self, params={}):
        client_id = params.get("client_id")
        urls = params.get("urls")

        # Create individual payload arrays for use in whole payload
        threat_types = self.get_threat_types(params)
        platform_types = self.get_platforms(params)
        threat_entries = self.make_threat_entries(urls=urls)
        threat_entry_types = self.get_threat_entry_types(params)

        # Create object hierarchy and payload to send to Google
        client = Client(client_id=client_id)
        threat_info = ThreatInfo(threatTypes=threat_types, platformTypes=platform_types,
                                 threatEntryTypes=threat_entry_types, threatEntries=threat_entries)
        request_payload = Request(client=client, threatInfo=threat_info)  # Create request payload

        # Marshall & serialize object hierarchy into JSON
        payload = jsonpickle.encode(request_payload, unpicklable=False)
        self.logger.info("Run: Created payload: {payload}".format(payload=payload))

        # Send request to Google
        response = requests.post(self.__URL,
                                 data=payload,
                                 params={"key": self.connection.API_KEY})

        # Check if status code is good. If not, raise an exception and halt.
        if not self.status_code_ok(status_code=response.status_code):
            raise Exception("Run: Non-200 status code received, halting. (Got {status_code})"
                            .format(status_code=response.status_code))

        # Get matches from the response. If they don't exist, then early call sys.exit.
        matches = response.json().get("matches")
        if not matches:
            self.logger.info("Run: No matches found!")
            matches = [{'threat':{'url':''}, 'threat_type':'','cache_duration':'','threat_entry_type':'','platform_type':''}]
            results = 0
        else:
            results = len(matches)
        return {"matches": matches, 'results': results}

    @staticmethod
    def status_code_ok(status_code):
        """Checks status code against list at https://developers.google.com/safe-browsing/v4/status-codes
        and determines if execution can continue"""

        if status_code is 200:
            return True
        if status_code is 400:
            self.logger.info("Bad Request: Invalid argument (invalid request payload).")
            return False
        if status_code is 403:
            self.logger.info("Forbidden: Permission denied (invalid API key/quota exceeded).")
            return False
        if status_code is 500:
            self.logger.info("Internal Server Error")
            return False
        if status_code is 503:
            self.logger.info("Service Unavailable: Unavailable.")
            return False
        if status_code is 504:
            self.logger.info("Gateway Timeout: Deadline exceeded (retry your request).")
            return False
        else:  # We received an undocumented status code, so return False
            assert "Undocumented status code received: {status_code}".format(status_code=status_code)
            return False

    @staticmethod
    def make_threat_entries(urls):
        """Takes a list of urls and creates ThreatEntry objects from them."""
        threat_entries = list()

        for url in urls:
            threat_entries.append(ThreatEntry(url=url))

        return threat_entries

    @staticmethod
    def get_threat_types(params):
        """Takes input parameters from user and creates a list of appropriate threat types."""
        threat_types = list()

        if params.get("threat_type_malware"):
            threat_types.append("MALWARE")

        if params.get("threat_type_potential"):
            threat_types.append("POTENTIALLY_HARMFUL_APPLICATION")

        if params.get("threat_type_social"):
            threat_types.append("SOCIAL_ENGINEERING")

        if params.get("threat_type_unspecified"):
            threat_types.append("THREAT_TYPE_UNSPECIFIED")

        if params.get("threat_type_unwanted"):
            threat_types.append("UNWANTED_SOFTWARE")

        return threat_types

    @staticmethod
    def get_platforms(params):
        """Takes input parameters from user and creates a list of appropriate platforms."""
        platforms = list()

        if params.get("platform_type_unspecified"):
            platforms.append("PLATFORM_TYPE_UNSPECIFIED")

        if params.get("platform_type_windows"):
            platforms.append("WINDOWS")

        if params.get("platform_type_linux"):
            platforms.append("LINUX")

        if params.get("platform_type_android"):
            platforms.append("ANDROID")

        if params.get("platform_type_mac"):
            platforms.append("OSX")

        if params.get("platform_type_ios"):
            platforms.append("IOS")

        if params.get("platform_type_any"):
            platforms.append("ANY_PLATFORM")

        if params.get("platform_type_all"):
            platforms.append("ALL_PLATFORMS")

        if params.get("platform_type_chrome"):
            platforms.append("CHROME")

        return platforms

    @staticmethod
    def get_threat_entry_types(params):
        """Takes input parameters from user and creates a list of appropriate threat entry types."""
        types = list()

        if params.get("threat_entry_type_unspecified"):
            types.append("THREAT_ENTRY_TYPE_UNSPECIFIED")

        if params.get("threat_entry_type_url"):
            types.append("URL")

        if params.get("threat_entry_type_executable"):
            types.append("EXECUTABLE")

        if params.get("threat_entry_type_ip"):
            types.append("IP_RANGE")

        return types

    def test(self):
        return {}



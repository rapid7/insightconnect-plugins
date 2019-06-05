import komand
from .schema import NsWhoisInput, NsWhoisOutput
# Custom imports below


class NsWhois(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='ns_whois',
                description='Allows you to search a nameserver to find all domains registered by that nameserver',
                input=NsWhoisInput(),
                output=NsWhoisOutput())

    def run(self, params={}):
        nameserver = params.get('nameserver')
        try:
           ns_whois = self.connection.investigate.ns_whois([nameserver], limit=1000)
        except Exception as e:
            self.logger.error("NsWhois: Run: Problem with request")
            raise e
        one_ns_whois = ns_whois.get(nameserver)
        if not one_ns_whois:
            self.logger.error("NsWhois: Run: Wrong object")
            raise Exception("NsWhois: Run: Wrong object")
        return {"domain": [{"more_data_available": one_ns_whois.get("moreDataAvailable"), "limit": one_ns_whois.get("limit"), "domains": one_ns_whois.get("domains"), "total_results": one_ns_whois.get("totalResults")}]}

    def test(self):
        return {"domain": [{"total_results": 500, "limit": 500, "more_data_available": True, "domains": [{"current": True, "domain": "0x255.com"}, {"current": True, "domain": "265.com"}]}]}

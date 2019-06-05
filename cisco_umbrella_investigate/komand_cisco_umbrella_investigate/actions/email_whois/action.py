import komand
from .schema import EmailWhoisInput, EmailWhoisOutput
# Custom imports below
from validate_email import validate_email


class EmailWhois(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='email_whois',
                description='Returns the WHOIS information for the specified email address(es), nameserver(s) and domains',
                input=EmailWhoisInput(),
                output=EmailWhoisOutput())

    def run(self, params={}):
        email = params.get('email')
        is_valid = validate_email(email)
        if not is_valid:
            self.logger.error("EmailWhois: Run: Wrong email")
            raise Exception("EmailWhois: run: Wrong email")

        try:
            email_whois = self.connection.investigate.email_whois(email)
        except Exception as e:
            self.logger.error("LatestDomains: Run: Problem with request")
            raise e

        one_email_whois = email_whois.get(email)
        if not one_email_whois:
            self.logger.error("EmailWhois: Run: Wrong object")
            raise Exception("EmailWhois: run: Wrong object")

        return {"email_whois": [{"more_data_available": one_email_whois.get("moreDataAvailable"), "limit": one_email_whois.get("limit"), "domains": one_email_whois.get("domains"), "total_results": one_email_whois.get("totalResults")}]}

    def test(self):
        return {"email_whois": []}

import insightconnect_plugin_runtime
from .schema import DomainInput, DomainOutput, Input

# Custom imports below
import whois
import datetime
from insightconnect_plugin_runtime.exceptions import PluginException

class Domain(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='domain',
                description='Whois Domain Lookup',
                input=DomainInput(),
                output=DomainOutput())

    def run(self, params={}):
        domain = str(params.get(Input.DOMAIN))  # Comes in as unicode - whois library has assert for type on str
        self.logger.info("Getting whois information for %s" % domain)

        if not self.is_valid_domain(domain=domain):
            raise PluginException(cause="Invalid domain as input.",
                                  assistance="Ensure the domain is not prefixed with a protocol.")

        try:
            lookup_results = whois.query(domain, ignore_returncode=1)  # ignore_return code required for plugin
        except Exception as e:
            self.logger.error("Error occurred: %s" % e)
            raise PluginException(cause="The whois command failed.",
                                  assistance=f"{e}")

        result_dict = insightconnect_plugin_runtime.helper.clean_dict(lookup_results.__dict__)

        # Type conversions for the new version of whois.

        # convert datetimes to string
        for key in result_dict.keys():
            value = result_dict.get(key)
            if isinstance(value, datetime.datetime):
                result_dict[key] = str(value)

        # convert set to list
        for key in result_dict.keys():
            value = result_dict.get(key)
            if isinstance(value, set):
                result_dict[key] = list(value)

        return result_dict

    def is_valid_domain(self, domain):
        if "://" in domain:
            return False
        return True

    def test(self):
        # TODO: Implement test function
        return {}

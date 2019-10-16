import json
import re
import requests
from urllib.parse import urlparse
from urllib.parse import urljoin
import urllib
import datetime, time
import logging

class Investigate(object):
    BASE_URL = 'https://investigate.api.opendns.com/'
    SUPPORTED_DNS_TYPES = [
        "A",
        "NS",
        "MX",
        "TXT",
        "CNAME",
    ]

    DEFAULT_LIMIT = None
    DEFAULT_OFFSET = None
    DEFAULT_SORT = None
    IP_PATTERN = re.compile(r'(\d{1,3}\.){3}\d{1,3}')

    DOMAIN_ERR = "Domains must be a string or a list of strings"
    IP_ERR = "Invalid IP address"
    UNSUPPORTED_DNS_QUERY = "Supported query types are: {}".format(SUPPORTED_DNS_TYPES)
    SEARCH_ERR = "Start argument must be a datetime or a timedelta"

    def __init__(self, api_key, proxies={}):
        self.api_key = api_key
        self.proxies = proxies
        self._uris = {
            "categorization":       "domains/categorization/",
            "cooccurrences":        "recommendations/name/{}.json",
            "domain_rr_history":    "dnsdb/name/{}/{}.json",
            "ip_rr_history":        "dnsdb/ip/{}/{}.json",
            "latest_domains":       "ips/{}/latest_domains",
            "related":              "links/name/{}.json",
            "security":             "security/name/{}.json",
            "tags":                 "domains/{}/latest_tags",
            "whois_email":          "whois/emails/{}",
            "whois_ns":             "whois/nameservers/{}",
            "whois_domain":         "whois/{}",
            "whois_domain_history": "whois/{}/history",
            "search":               "search/{}",
            "samples":              "samples/{}",
            "sample":               "sample/{}",
            "sample_artifacts":     "sample/{}/artifacts",
            "sample_connections":   "sample/{}/connections",
            "sample_samples":       "sample/{}/samples",
            "as_for_ip":            "bgp_routes/ip/{}/as_for_ip.json",
            "prefixes_for_asn":     "bgp_routes/asn/{}/prefixes_for_asn.json"
        }
        self._auth_header = {"Authorization": "Bearer " + self.api_key}

    def get(self, uri, params={}):
        '''A generic method to make GET requests to the OpenDNS Investigate API
        on the given URI.
        '''
        return requests.get(urljoin(Investigate.BASE_URL, uri),
            params=params, headers=self._auth_header, proxies=self.proxies
        )

    def post(self, uri, params={}, data={}):
        '''A generic method to make POST requests to the OpenDNS Investigate API
        on the given URI.
        '''
        return requests.post(
            urljoin(Investigate.BASE_URL, uri),
            params=params, data=data, headers=self._auth_header,
            proxies=self.proxies
        )

    def _request_parse(self, method, *args):
        r = method(*args)
        r.raise_for_status()
        return r.json()

    def get_parse(self, uri, params={}):
        '''Convenience method to call get() on an arbitrary URI and parse the response
        into a JSON object. Raises an error on non-200 response status.
        '''
        return self._request_parse(self.get, uri, params)

    def post_parse(self, uri, params={}, data={}):
        '''Convenience method to call post() on an arbitrary URI and parse the response
        into a JSON object. Raises an error on non-200 response status.
        '''
        return self._request_parse(self.post, uri, params, data)

    def _get_categorization(self, domain, labels):
        uri = urljoin(self._uris['categorization'], domain)
        params = {'showLabels': True} if labels else {}
        return self.get_parse(uri, params)

    def _post_categorization(self, domains, labels):
        params = {'showLabels': True} if labels else {}
        return self.post_parse(self._uris['categorization'], params,
            json.dumps(domains)
        )

    def categorization(self, domains, labels=False):
        '''Get the domain status and categorization of a domain or list of domains.
        'domains' can be either a single domain, or a list of domains.
        Setting 'labels' to True will give back categorizations in human-readable
        form.
        For more detail, see https://sgraph.opendns.com/docs/api#categorization
        '''
        if type(domains) is str:
            return self._get_categorization(domains, labels)
        elif type(domains) is list:
            return self._post_categorization(domains, labels)
        else:
            raise PluginException(cause='Unable to retrieve domain information.', assistance=Investigate.DOMAIN_ERR)

    def cooccurrences(self, domain):
        '''Get the cooccurrences of the given domain.
        For details, see https://sgraph.opendns.com/docs/api#co-occurrences
        '''
        uri = self._uris["cooccurrences"].format(domain)
        return self.get_parse(uri)

    def related(self, domain):
        '''Get the related domains of the given domain.
        For details, see https://sgraph.opendns.com/docs/api#relatedDomains
        '''
        uri = self._uris["related"].format(domain)
        return self.get_parse(uri)

    def security(self, domain):
        '''Get the Security Information for the given domain.
        For details, see https://sgraph.opendns.com/docs/api#securityInfo
        '''
        uri = self._uris["security"].format(domain)
        return self.get_parse(uri)

    def domain_tags(self, domain):
        '''Get the domain tagging dates for the given domain.
        For details, see https://sgraph.opendns.com/docs/api#latest_tags
        '''
        uri = self._uris["tags"].format(domain)
        return self.get_parse(uri)

    def _domain_rr_history(self, domain, query_type):
        uri = self._uris["domain_rr_history"].format(query_type, domain)
        return self.get_parse(uri)

    def _ip_rr_history(self, ip, query_type):
        uri = self._uris["ip_rr_history"].format(query_type, ip)
        return self.get_parse(uri)

    def rr_history(self, query, query_type="A"):
        '''Get the RR (Resource Record) History of the given domain or IP.
        The default query type is for 'A' records, but the following query types
        are supported:
        A, NS, MX, TXT, CNAME
        For details, see https://sgraph.opendns.com/docs/api#dnsrr_domain
        '''
        if query_type not in Investigate.SUPPORTED_DNS_TYPES:
            raise PluginException(cause='Unable to retrieve resource record.', assistance=Investigate.UNSUPPORTED_DNS_QUERY)

        # if this is an IP address, query the IP
        if Investigate.IP_PATTERN.match(query):
            return self._ip_rr_history(query, query_type)

        # otherwise, query the domain
        return self._domain_rr_history(query, query_type)

    def latest_domains(self, ip):
        '''Gets the latest known malicious domains associated with the given
        IP address, if any. Returns the list of malicious domains.
        '''
        if not Investigate.IP_PATTERN.match(ip):
            raise PluginException(cause='Unable to retrieve domains for IP address.', assistance='Please try submitting another address.')

        uri = self._uris["latest_domains"].format(ip)
        resp_json = self.get_parse(uri)

        # parse out the domain names
        return [ val for d in resp_json for key, val in d.iteritems() if key == 'name' ]

    def domain_whois(self, domain):
        '''Gets whois information for a domain'''
        uri = self._uris["whois_domain"].format(domain)
        resp_json = self.get_parse(uri)
        return resp_json

    def domain_whois_history(self, domain, limit=None):
        '''Gets whois history for a domain'''

        params = dict()
        if limit is not None:
            params['limit'] = limit

        uri = self._uris["whois_domain_history"].format(domain)
        resp_json = self.get_parse(uri, params)
        return resp_json

    def ns_whois(self, nameservers, limit=DEFAULT_LIMIT, offset=DEFAULT_OFFSET, sort_field=DEFAULT_SORT):
        '''Gets the domains that have been registered with a nameserver or
        nameservers'''
        if not isinstance(nameservers, list):
            uri = self._uris["whois_ns"].format(nameservers)
            params = {'limit': limit, 'offset': offset, 'sortField': sort_field}
        else:
            uri = self._uris["whois_ns"].format('')
            params = {'nameServerList' : ','.join(nameservers), 'limit': limit, 'offset': offset, 'sortField': sort_field}

        resp_json = self.get_parse(uri, params=params)
        return resp_json

    def email_whois(self, emails, limit=DEFAULT_LIMIT, offset=DEFAULT_OFFSET, sort_field=DEFAULT_SORT):
        '''Gets the domains that have been registered with a given email
        address
        '''
        if not isinstance(emails, list):
            uri = self._uris["whois_email"].format(emails)
            params = {'limit': limit, 'offset': offset, 'sortField': sort_field}
        else:
            uri = self._uris["whois_email"].format('')
            params = {'emailList' : ','.join(emails), 'limit': limit, 'offset': offset, 'sortField': sort_field}

        resp_json = self.get_parse(uri, params=params)
        return resp_json

    def search(self, pattern, start=None, limit=None, include_category=None):
        '''Searches for domains that match a given pattern'''
        
        params = dict()

        if start is None:
            start = datetime.timedelta(days=30)

        if isinstance(start, datetime.timedelta):
            params['start'] = int(time.mktime((datetime.datetime.utcnow() - start).timetuple()) * 1000)
        elif isinstance(start, datetime.datetime):
            params['start'] = int(time.mktime(start.timetuple()) * 1000)
        else:
            raise PluginException(cause='Unable to retrieve domains for search.', assistance=Investigate.SEARCH_ERR)
        
        if limit is not None and isinstance(limit, int):
            params['limit'] = limit
        if include_category is not None and isinstance(include_category, bool):
            params['includeCategory'] = str(include_category).lower()

        uri = self._uris['search'].format(urllib.parse.quote_plus(pattern))

        return self.get_parse(uri, params)

    def samples(self, anystring, limit=None, offset=None, sortby=None):
        '''Return an object representing the samples identified by the input domain, IP, or URL'''

        uri = self._uris['samples'].format(anystring)
        params = {'limit': limit, 'offset': offset, 'sortby': sortby}

        return self.get_parse(uri, params)

    def sample(self, hash, limit=None, offset=None):
        '''Return an object representing the sample identified by the input hash, or an empty object if that sample is not found'''

        uri = self._uris['sample'].format(hash)
        params = {'limit': limit, 'offset': offset}

        return self.get_parse(uri, params)

    def sample_artifacts(self, hash, limit=None, offset=None):
        '''
            Return an object representing artifacts associated with an input hash
            NOTE: Only available to Threat Grid customers
        '''

        uri = self._uris['sample_artifacts'].format(hash)
        params = {'limit': limit, 'offset': offset}

        return self.get_parse(uri, params)

    def sample_connections(self, hash, limit=None, offset=None):
        '''Return an object representing network connections associated with an input hash'''

        uri = self._uris['sample_connections'].format(hash)
        params = {'limit': limit, 'offset': offset}

        return self.get_parse(uri, params)

    def sample_samples(self, hash, limit=None, offset=None):
        '''Return an object representing samples associated with an input hash'''

        uri = self._uris['sample_samples'].format(hash)
        params = {'limit': limit, 'offset': offset}

        return self.get_parse(uri, params)

    def as_for_ip(self, ip):
        '''Gets the AS information for a given IP address.'''
        if not Investigate.IP_PATTERN.match(ip):
            raise PluginException(cause='Unable to retrieve AS for IP address.', assistance='Please try submitting another address.')

        uri = self._uris["as_for_ip"].format(ip)
        resp_json = self.get_parse(uri)

        return resp_json

    def prefixes_for_asn(self, asn):
        '''Gets the AS information for a given ASN. Return the CIDR and geolocation associated with the AS.'''

        uri = self._uris["prefixes_for_asn"].format(asn)
        resp_json = self.get_parse(uri)

        return resp_json

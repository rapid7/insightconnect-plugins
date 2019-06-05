import komand
import time
import json
import certstream
import re
import Levenshtein
from komand_typo_squatter.util import utils
from .schema import SearchCertstreamInput, SearchCertstreamOutput


class SearchCertstream(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_certstream',
                description='Searches certstream for new certs matching query',
                input=SearchCertstreamInput(),
                output=SearchCertstreamOutput())

    def callback(self, message, context):
        """Callback handler for certstream events."""
        if message['message_type'] == "heartbeat":
            return

        if message['message_type'] == "certificate_update":
            all_domains = message['data']['leaf_cert']['all_domains']

            for domain in all_domains:
                score = utils.score_domain(domain.lower())

                # If issued from a free CA = more suspicious
                if "Let's Encrypt" in message['data']['chain'][0]['subject']['aggregated']:
                    score += 10
                if self.query:
                    if not re.search(self.query,domain):
                        continue
                else:
                     if (Levenshtein.distance(str(self.domain), str(domain)) >  self.levenshtein) :
                         continue
                self.send({'domain':domain,'score':score})

    def run(self, params={}):
        """Run the trigger"""
        self.query = params.get('query')
        self.levenshtein = params.get('levenshtein')
        self.domain = params.get('domain')
        certstream.listen_for_events(self.callback)

    def test(self,params={}):
        self.query = params.get('query')
        self.levenshtein = params.get('levenshtein')
        self.domain = params.get('domain')
        if self.query and self.domain:
            self.logger.error("Can't use both levenshtein and query")
            return 0
        return {'domain':'komand.com','score':'0'}

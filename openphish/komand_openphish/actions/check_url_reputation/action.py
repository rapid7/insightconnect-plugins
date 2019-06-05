import komand
from .schema import CheckUrlReputationInput, CheckUrlReputationOutput, Input, Output
# Custom imports below
import json


class CheckUrlReputation(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='check_url_reputation',
            description='Check URL Reputation',
            input=CheckUrlReputationInput(),
            output=CheckUrlReputationOutput())

    def run(self, params={}):
        searched_url = params.get(Input.URL)
        with komand.helper.open_cachefile('/var/cache/feed.txt') as f:
            split_urls = f.read().splitlines()
        counter = self.count_found_urls(searched_url, split_urls)
        decoded_stats = self.normalize_decoded_stats(searched_url, self.get_decoded_stats())

        decoded_stats["found"] = counter > 0
        decoded_stats["matches"][searched_url] = decoded_stats["matches"][searched_url] + counter
        decoded_stats["total_matches"] = decoded_stats["total_matches"] + counter

        with komand.helper.open_cachefile('/var/cache/stats.txt') as f:
            f.write(json.dumps(decoded_stats))

        return {
            Output.URLREPUTATION: decoded_stats
        }

    @staticmethod
    def count_found_urls(searched_url, split_urls):
        counter = 0
        if split_urls:
            for url in split_urls:
                if url.find(searched_url) > -1:
                    counter = counter + 1

        return counter

    @staticmethod
    def get_decoded_stats():
        with komand.helper.open_cachefile('/var/cache/stats.txt') as f:
            stats_file = f.read()
        decoded_stats = {}
        if stats_file:
            decoded_stats = json.loads(stats_file)

        return decoded_stats

    @staticmethod
    def normalize_decoded_stats(searched_url, decoded_stats):
        if "matches" not in decoded_stats:
            decoded_stats["matches"] = {
                searched_url: 0
            }

        if searched_url not in decoded_stats["matches"]:
            decoded_stats["matches"][searched_url] = 0

        if "total_matches" not in decoded_stats:
            decoded_stats["total_matches"] = 0

        return decoded_stats

import komand
from .schema import AsnInput, AsnOutput
# Custom imports below
import json
import feedparser
import urllib.request


class Asn(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='asn',
                description='Lookup ZeuS hosts in specific autonomous system',
                input=AsnInput(),
                output=AsnOutput())

    def run(self, params={}):
        server = self.connection.server
        url = server + '/monitor.php?asnrss=' + params.get('as')
        response = urllib.request.urlopen(url)
        raw_data = feedparser.parse(response.read())
        results = []

        limit = min(params.get('limit'), len(raw_data['entries']))

        for idx in range(limit):
            raw_entry = raw_data['entries'][idx]

            asn = raw_entry['description'].split(', ')[-2].split(' ')[-1]
            country = raw_entry['description'].split(', ')[-1].split(' ')[-1]
            date = raw_entry['title'].split(' ')[1][1:-1]
            guid = raw_entry['guid'][-32:]
            host = raw_entry['description'].split(', ')[0].split(' ')[1]
            ip = raw_entry['description'].split(', ')[1].split(' ')[2]
            level = int(raw_entry['description'].split(', ')[4].split(' ')[1])
            link = raw_entry['link']
            malware = raw_entry['description'].split(', ')[5].split(' ')[1]
            sbl = raw_entry['description'].split(', ')[2].split(' ')[1]
            status = raw_entry['description'].split(', ')[3].split(' ')[1]

            output_entry = {
                    'as': asn,
                    'country': country,
                    'date': date,
                    'guid': guid,
                    'host': host,
                    'ip': ip,
                    'level': level,
                    'link': link,
                    'malware': malware,
                    'sbl': sbl,
                    'status': status
                    }
            results.append(output_entry)
        return { 'results': results }

    def test(self):
        # TODO: Implement test function
        return {}

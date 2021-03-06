import komand
from .schema import BinariesInput, BinariesOutput
# Custom imports below
import json
import feedparser
import urllib.request


class Binaries(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='binaries',
                description='Get information on ZeuS binary URLs',
                input=BinariesInput(),
                output=BinariesOutput())

    def run(self, params={}):
        server = self.connection.server
        url = server + '/monitor.php?urlfeed=binaries'
        response = urllib.request.urlopen(url)
        raw_data = feedparser.parse(response.read())
        results = []

        limit = min(params.get('limit'), len(raw_data['entries']))

        for idx in range(limit):
            raw_entry = raw_data['entries'][idx]

            date = raw_entry['title'].split(' ')[1][1:-1]
            download_url = raw_entry['title'].split(' ')[0]
            guid = raw_entry['guid'][-32:]
            link = raw_entry['link']
            try:
                md5 = raw_entry['description'].split(', ')[-1].split(' ')[-1]
            except:
                md5 = ""
            status = raw_entry['description'].split(', ')[1].split(' ')[1]
            version = 'N/A'

            output_entry = {
                    'date': date,
                    'download_url': download_url,
                    'guid': guid,
                    'link': link,
                    'md5': md5,
                    'status': status,
                    'version': version
                    }
            results.append(output_entry)
        return { 'results': results }

    def test(self):
        # TODO: Implement test function
        return {}

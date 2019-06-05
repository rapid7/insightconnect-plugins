import komand
from .schema import IpAddressInput, IpAddressOutput
# Custom imports below
import json
import urllib.request
import lxml.html


class IpAddress(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='ip_address',
                description='Lookup ZeuS hosts by IP address',
                input=IpAddressInput(),
                output=IpAddressOutput())

    def run(self, params={}):
        output = {}
        server = self.connection.server
        url = server + '/monitor.php?ipaddress=' + params.get('ip')
        response = urllib.request.urlopen(url)
        tree = lxml.html.fromstring(response.read())
        tables = tree.xpath('//table')

        if not tables:
            return { 'found': False }

        output['found'] = True
        trs = tables[0].xpath('tr')
        ip = trs[0].xpath('td')[-1].text
        output['ip'] = ip
        host = trs[1].xpath('td')[-1].text
        output['host'] = host
        num_hosts = int(trs[2].xpath('td')[-1].xpath('strong')[-1].text)
        output['num_hosts'] = num_hosts
        active_files = int(trs[3].xpath('td')[-1].xpath('strong')[-1].text)
        output['active_files'] = active_files
        sbl = trs[4].xpath('td')[-1].xpath('a')[-1].text
        output['sbl'] = sbl
        asn_num = trs[5].xpath('td')[-1].xpath('a')[-1].text
        output['asn_num'] = asn_num
        asn_name = trs[6].xpath('td')[-1].text
        output['asn_name'] = asn_name
        country = trs[7].xpath('td')[-1].xpath('a')[-1].text
        output['country'] = country

        zeus_hosts = []
        trs = tables[1].xpath('tr')[1:]
        for tr in trs:
            date, dummy, dummy, host, status, num_files, registrar, ns = tr.xpath('td')
            row = {
                'date': date.text,
                'host': host.xpath('a')[-1].text,
                'status': status.text,
                'num_files': int(num_files.text),
                'registrar': registrar.text,
                'nameserver': ns.text
                }
            zeus_hosts.append(row)
        output['zeus_hosts'] = zeus_hosts

        return output

    def test(self):
        return { 'found': True }

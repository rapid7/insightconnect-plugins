import komand
from .schema import HostInput, HostOutput
# Custom imports below
import json
import base64
import urllib.request
import lxml.html


class Host(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='host',
                description='Lookup ZeuS hosts by hostname',
                input=HostInput(),
                output=HostOutput())

    def run(self, params={}):
        output = {}
        server = self.connection.server
        url = server + '/monitor.php?host=' + params.get('host')
        response = urllib.request.urlopen(url)
        tree = lxml.html.fromstring(response.read())
        tables = tree.xpath('//table')

        if not tables:
            return { 'found': False }

        output['found'] = True
        trs = tables[0].xpath('tr')
        malware = trs[1].xpath('td')[-1].text
        output['malware'] = malware
        ip = trs[2].xpath('td')[-1].xpath('a')[-1].text
        output['ip'] = ip
        status = trs[3].xpath('td')[-1].text
        output['status'] = status
        uptime = trs[4].xpath('td')[-1].text
        output['uptime'] = uptime
        host = trs[5].xpath('td')[-1].text
        output['host'] = host
        sbl = trs[6].xpath('td')[-1].text
        output['sbl'] = sbl
        as_num = trs[7].xpath('td')[-1].xpath('a')[-1].text
        output['as_num'] = as_num
        as_name = trs[8].xpath('td')[-1].text
        output['as_name'] = as_name
        country = trs[9].xpath('td')[-1].xpath('a')[-1].text
        output['country'] = country
        level = int(trs[10].xpath('td')[-1].text.split(' ')[0])
        output['level'] = level
        registrar = trs[11].xpath('td')[-1].text
        output['registrar'] = registrar
        link_list = trs[12].xpath('td')[-1].xpath('a')
        nameservers = []
        for link in link_list:
            nameservers.append(link.text)
        output['nameservers'] = nameservers
        date_added = trs[13].xpath('td')[-1].text
        output['date_added'] = date_added
        last_checked = trs[14].xpath('td')[-1].text
        output['last_checked'] = last_checked
        last_updated = trs[15].xpath('td')[-1].text
        output['last_updated'] = last_updated

        trs = tables[1].xpath('tr')[1:]
        config_urls = []
        for tr in trs:
            date, config_url, status, version, builder, filesize, md5, http_status, file_url = tr.xpath('td')
            dl_link = server + file_url.xpath('a/@href')[-1]
            response = urllib.request.urlopen(dl_link)
            file_dl = str(base64.b64encode(response.read()))
            row = {
                'date': date.text,
                'url': config_url.text,
                'status': status.text,
                'version': version.text,
                'builder': builder.text,
                'filesize': filesize.text,
                'md5': md5.xpath('a')[-1].text,
                'http_status': http_status.text,
                'file': file_dl
            }
            config_urls.append(row)
        output['config_urls'] = config_urls

        trs = tables[2].xpath('tr')[1:]
        binary_urls = []
        for tr in trs:
            date, binary_url, status, filesize, md5, anubis, virustotal, http_status, file_url = tr.xpath('td')
            dl_link = server + file_url.xpath('a/@href')[-1]
            response = urllib.request.urlopen(dl_link)
            file_dl = str(base64.b64encode(response.read()))
            row = {
                'date': date.text,
                'url': binary_url.text,
                'status': status.text,
                'filesize': filesize.text,
                'md5': md5.xpath('a')[-1].text,
                'anubis': anubis.text,
                'virustotal': virustotal.text,
                'http_status': http_status.text,
                'file': file_dl
            }
            binary_urls.append(row)
        output['binary_urls'] = binary_urls

        trs = tables[3].xpath('tr')[1:]
        drop_urls = []
        for tr in trs:
            date, drop_url, status, http_status = tr.xpath('td')
            row = {
                'date': date.text,
                'url': drop_url.text,
                'status': status.text,
                'http_status': http_status.text
            }
            drop_urls.append(row)
        output['drop_urls'] = drop_urls

        trs = tables[4].xpath('tr')[1:]
        fake_urls = []
        for tr in trs:
            md5, url, protocol = tr.xpath('td')
            row = {
                'md5': md5.xpath('a')[-1].text,
                'url': url.text,
                'protocol': protocol.text
            }
            fake_urls.append(row)
        output['fake_urls'] = fake_urls

        trs = tables[5].xpath('tr')[1:]
        domain_history = []
        for tr in trs:
            date, host, ip, as_num, as_name, country = tr.xpath('td')
            try:
                country = country.xpath('center')[-1].xpath('img/@title')[-1]
            except:
                country = ""
            row = {
                'changedate': date.text,
                'host': host.text,
                'ip': str(ip.text),
                'as_num': as_num.text,
                'as_name': str(as_name.text),
                'country': country
            }
            domain_history.append(row)
        output['domain_history'] = domain_history
        return output

    def test(self):
        # TODO: Implement test function
        return {}

import json
import os
import sys
import logging
import datetime
import re

import insightconnect_plugin_runtime
from komand_whois.connection.connection import Connection


sys.path.append(os.path.abspath("../"))


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action, params: dict = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_dict(filename: str, encodingenabled: bool = False) -> dict:
        with open(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), filename), "r", encoding="utf-8"
        ) as file_reader:
            data = json.load(file_reader)
            if encodingenabled:
                encodeddata = {}
                for key, value in data.items():
                    encodeddata[key] = value.encode("utf-8")
                return encodeddata
            else:
                return data

    @staticmethod
    def mock_whois(*args, **kwargs):

        class MockWhois:
            def __init__(self, data):
                try:
                    self.name = data['domain_name'][0].strip().lower()
                    self.registrar = data['registrar'][0].strip()
                    self.registrant_cc = data['registrant_cc'][0].strip().lower()
                    self.creation_date = str_to_date(data['creation_date'][0])
                    self.expiration_date = str_to_date(data['expiration_date'][0])
                    self.last_updated = str_to_date(data['updated_date'][0])

                    tmp = []
                    for x in data['name_servers']:
                        if isinstance(x, str):
                            tmp.append(x)
                        else:
                            for y in x: tmp.append(y)

                    self.name_servers = []
                    for x in tmp:
                        x = x.strip(' .')
                        if x:
                            if ' ' in x:
                                x, _ = x.split(' ', 1)
                                x = x.strip(' .')

                            self.name_servers.append(x.lower())

                    # Komand additions
                    self.registry_domain_id = data['registry_domain_id'][0].strip().lower()
                    self.registrar_whois_server = data['registrar_whois_server'][0].strip().lower()
                    self.registrar_url = data['registrar_url'][0].strip().lower()
                    self.registrar_iana_id = data['registrar_iana_id'][0].strip().lower()
                    self.registrar_abuse_contact_email = data['registrar_abuse_contact_email'][0].strip().lower()
                    self.registrar_abuse_contact_phone = data['registrar_abuse_contact_phone'][0].strip().lower()
                    self.domain_status = list(map(lambda ds: ds.strip().lower(), data['domain_status']))
                    self.dnssec = data['dnssec'][0].strip().lower()

                except KeyError:
                    pass

            def get_json_serializable(self):
                properties = self.__dict__

                for key in properties:
                    if type(properties[key]) is datetime.datetime:
                        properties[key] = properties[key].isoformat()
                    if type(properties[key]) is set:
                        properties[key] = list(properties[key])

                return properties

        # http://docs.python.org/library/datetime.html#strftime-strptime-behavior
        DATE_FORMATS = [
            '%d-%b-%Y',  # 02-jan-2000
            '%d.%m.%Y',  # 02.02.2000
            '%d/%m/%Y',  # 01/06/2011
            '%Y-%m-%d',  # 2000-01-02
            '%Y.%m.%d',  # 2000.01.02
            '%Y/%m/%d',  # 2005/05/30
            'before %b-%Y',  # before aug-1996
            '%Y.%m.%d %H:%M:%S',  # 2002.09.19 13:00:00
            '%Y%m%d %H:%M:%S',  # 20110908 14:44:51
            '%Y-%m-%d %H:%M:%S',  # 2011-09-08 14:44:51
            '%Y-%m-%d %H:%M:%S CLST',  # 2011-09-08 14:44:51 CLST CL
            '%Y-%m-%d %H:%M:%S.%f',  # 2011-09-08 14:44:51 CLST CL
            '%d.%m.%Y  %H:%M:%S',  # 19.09.2002 13:00:00
            '%d-%b-%Y %H:%M:%S %Z',  # 24-Jul-2009 13:20:03 UTC
            '%Y/%m/%d %H:%M:%S (%z)',  # 2011/06/01 01:05:01 (+0900)
            '%Y/%m/%d %H:%M:%S',  # 2011/06/01 01:05:01
            '%a %b %d %H:%M:%S %Z %Y',  # Tue Jun 21 23:59:59 GMT 2011
            '%a %b %d %Y',  # Tue Dec 12 2000
            '%Y-%m-%dT%H:%M:%S',  # 2007-01-26T19:10:31
            '%Y-%m-%dT%H:%M:%SZ',  # 2007-01-26T19:10:31Z
            '%Y-%m-%dt%H:%M:%S.%fz',  # 2007-01-26t19:10:31.00z
            '%Y-%m-%dT%H:%M:%S%z',  # 2011-03-30T19:36:27+0200
            '%Y-%m-%dT%H:%M:%S.%f%z',  # 2011-09-08T14:44:51.622265+03:00
            '%Y-%m-%dt%H:%M:%S.%f',  # 2011-09-08t14:44:51.622265
            '%Y-%m-%dt%H:%M:%S',  # 2007-01-26T19:10:31
            '%Y-%m-%dt%H:%M:%SZ',  # 2007-01-26T19:10:31Z
            '%Y-%m-%dt%H:%M:%S.%fz',  # 2007-01-26t19:10:31.00z
            '%Y-%m-%dt%H:%M:%S%z',  # 2011-03-30T19:36:27+0200
            '%Y-%m-%dt%H:%M:%S %z',  # 2011-03-30T19:36:27+0200
            '%Y-%m-%dt%H:%M:%S.%f%z',  # 2011-09-08T14:44:51.622265+03:00
            '%Y%m%d',  # 20110908
            '%Y. %m. %d.',  # 2020. 01. 12.
            'before %b-%Y',  # before aug-1996
            '%a %d %b %Y',  # Tue 21 Jun 2011
            '%A %d %b %Y',  # Tuesday 21 Jun 2011
            '%a %d %B %Y',  # Tue 21 June 2011
            '%A %d %B %Y',  # Tuesday 21 June 2011
            '%Y-%m-%d %H:%M:%S (%Z+0:00)',  # 2007-12-24 10:24:32 (gmt+0:00)
            '%B %d %Y',  # January 01 2000
        ]

        def str_to_date(text):
            text = text.strip().lower()

            if not text or text == 'not defined':
                return

            text = text.replace('(jst)', '(+0900)')
            text = re.sub('(\+[0-9]{2}):([0-9]{2})', '\\1\\2', text)
            text = re.sub('(\ #.*)', '', text)
            # hack for 1st 2nd 3rd 4th etc
            # better here https://stackoverflow.com/questions/1258199/python-datetime-strptime-wildcard
            text = re.sub(r"(\d+)(st|nd|rd|th) ", r"\1 ", text)

            for format in DATE_FORMATS:
                try:
                    return datetime.datetime.strptime(text, format)
                except ValueError:
                    pass

            raise Exception("Unknown date format: '%s'" % text)

        query = args[0]
        if query == f"google.com":
            filename = "domain.json.resp"
            test_data = Util.read_file_to_dict(f"responses/{filename}", encodingenabled=False)
            return MockWhois(data=test_data)
        elif query == f"hello/world.com":
            filename = "domain_error.json.resp"
            test_data = Util.read_file_to_dict(f"responses/{filename}", encodingenabled=False)
            return MockWhois(data=test_data)
        elif query == f"/usr/bin/whois 198.51.100.100":
            filename = "address.json.resp"
            test_data = Util.read_file_to_dict(f"responses/{filename}", encodingenabled=False)
            print(f"{test_data =}")
            return test_data

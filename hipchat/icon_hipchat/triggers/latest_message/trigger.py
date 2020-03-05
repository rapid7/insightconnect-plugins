import komand
import time
import json
import urllib
import requests
from icon_hipchat.util import utils

from .schema import LatestMessageInput, LatestMessageOutput


# Custom imports below


class LatestMessage(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='latest_message',
            description='Trigger on chat latest message',
            input=LatestMessageInput(),
            output=LatestMessageOutput())

    def get_latest_message(self, base_url, url, token):
        '''Check for supported url prefix'''
        utils.validate_url(url)

        is_modified = True
        meta = utils.hash_url(base_url)
        cache_file = '/var/cache/' + meta['file']

        '''Attempt to retrieve headers from past request'''
        headers = {}
        if komand.helper.check_cachefile(meta['metafile']):
            headers = utils.check_url_meta_file(meta)

        '''Call request get latest message'''
        urlobj = komand.helper.open_url(
            url, If_None_Match=headers.get('etag', ''),
            If_Modified_Since=headers.get('last-modified', ''),
            Content_Type='application/json',
            Authorization='Bearer %s' % token)

        '''File modified'''
        if urlobj:
            contents = urlobj.read()
            '''Write etag and last modified to cache'''
            utils.create_url_meta_file(meta, urlobj)

            '''We can't guarantee server supports lastmodified/etag, compare contents'''
            if komand.helper.check_cachefile(cache_file):
                old = komand.helper.open_cachefile(cache_file)
                old_contents = old.read()
                old.close()
                if old_contents == contents:
                    is_modified = False
                    self.logger.info('HipChat: No new messages')

            '''Write new latest message contents to cache'''
            if is_modified:
                f = komand.helper.open_cachefile(cache_file)
                f.write(contents)
                f.close()

                '''Check URL status code and return latest message'''
                if urlobj.code >= 200 and urlobj.code <= 299:
                    if contents:
                        self.send(json.loads(contents))

    def run(self, params={}):
        server = self.connection.server
        token = self.connection.token
        data = {}

        room_id_or_name = params.get("room_id_or_name", "")
        # add query parameters
        max_results = params.get("max-results", "")
        timezone = params.get("timezone", "")
        not_before = params.get("not-before", "")
        include_deleted = params.get("include_deleted", "")

        if max_results:
            data["max-results"] = max_results

        if include_deleted:
            data["include_deleted"] = include_deleted

        if timezone:
            data["timezone"] = timezone

        if not_before:
            data["not_before"] = not_before

        base_url = server + '/room/' + room_id_or_name + '/history/latest?'
        url_values = urllib.urlencode(data)
        url = base_url + url_values

        while True:
            self.get_latest_message(base_url, url, token)
            time.sleep(float(params.get("interval")))

    def test(self):
        http_method = "GET"
        token = self.connection.token

        #  url test authentication
        url = 'http://api.hipchat.com'

        # call request test authentication
        response = requests.request(http_method, url,
                                    headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' % token})

        if response.status_code == 401:
            raise Exception('Unauthorized: %s (HTTP status: %s)' % (response.text, response.status_code))
        if response.status_code != 200:
            raise Exception('%s (HTTP status: %s)' % (response.text, response.status_code))

        return {'status_code': response.status_code}

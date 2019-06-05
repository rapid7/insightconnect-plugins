import komand
import time
from .schema import PollFileInput, PollFileOutput
# Custom imports below
from komand_get_url.util.utils import Utils


class PollFile(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='poll_file',
            description='Download modified file by URL',
            input=PollFileInput(),
            output=PollFileOutput())

    def run(self, params={}):
        utils = Utils(action=self)
        url = params.get('url')
        is_verify = params.get('is_verify', True)
        poll = params.get('poll', 60)

        while True:
            '''Check for supported url prefix'''
            utils.validate_url(url)

            is_modified = True
            meta = utils.hash_url(url)
            cache_file = '/var/cache/' + meta['file']

            '''Attempt to retrieve headers from past request'''
            headers = {}
            if komand.helper.check_cachefile(meta['metafile']):
                headers = utils.check_url_meta_file(meta)

            '''Download file'''
            urlobj = komand.helper.open_url(
                url, verify=is_verify,
                If_None_Match=headers.get('etag', ''),
                If_Modified_Since=headers.get('last-modified', ''))

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
                        self.logger.info('GetUrl: File not updated')

                '''Write new URL file contents to cache'''
                if is_modified:
                    f = komand.helper.open_cachefile(cache_file)
                    f.write(contents)
                    f.close()

                    '''Check URL status code and return file contents'''
                    if urlobj.code >= 200 or urlobj.code <= 299:
                        f = komand.helper.encode_string(contents)
                        if f:
                            output = {'file': f, 'status_code': urlobj.code or 200}
                            self.send(output)

            time.sleep(poll)

    def test(self, params={}):
        url = 'https://www.google.com'
        komand.helper.check_url(url)
        return {}

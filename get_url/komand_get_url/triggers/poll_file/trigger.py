import komand
import time
from .schema import PollFileInput, PollFileOutput, Input, Output, Component
# Custom imports below
from komand_get_url.util.utils import Utils


class PollFile(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='poll_file',
            description=Component.DESCRIPTION,
            input=PollFileInput(),
            output=PollFileOutput())

    def run(self, params={}):
        utils = Utils(action=self)
        url = params.get(Input.URL)
        is_verify = params.get(Input.IS_VERIFY, True)
        poll = params.get(Input.POLL, 60)

        while True:
            '''Check for supported url prefix'''
            utils.validate_url(url)

            is_modified = True
            meta = utils.hash_url(url)
            cache_file = "/var/cache/" + meta["file"]

            '''Attempt to retrieve headers from past request'''
            headers = {}
            if komand.helper.check_cachefile(meta["metafile"]):
                headers = utils.check_url_meta_file(meta)

            '''Download file'''
            url_object = komand.helper.open_url(
                url, verify=is_verify,
                If_None_Match=headers.get("etag", ""),
                If_Modified_Since=headers.get("last-modified", ""),
                User_Agent=params.get(Input.USER_AGENT, "Mozilla/5.0"))

            '''File modified'''
            if url_object:
                contents = url_object.read().decode('utf-8')

                '''Write etag and last modified to cache'''
                utils.create_url_meta_file(meta, url_object)

                '''We can't guarantee server supports lastmodified/etag, compare contents'''
                if komand.helper.check_cachefile(cache_file):
                    old = komand.helper.open_cachefile(cache_file)
                    old_contents = old.read()
                    old.close()
                    if old_contents == contents:
                        is_modified = False
                        self.logger.info("GetUrl: File not updated")

                '''Write new URL file contents to cache'''
                if is_modified:
                    f = komand.helper.open_cachefile(cache_file)
                    f.write(contents)
                    f.close()

                    '''Check URL status code and return file contents'''
                    if url_object.code >= 200 or url_object.code <= 299:
                        f = komand.helper.encode_string(contents)
                        if f:
                            output = {Output.BYTES: f.decode('utf-8'), Output.STATUS_CODE: url_object.code or 200}
                            self.send(output)

            time.sleep(poll)

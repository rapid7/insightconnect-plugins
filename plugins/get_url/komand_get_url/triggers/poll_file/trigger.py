import time

# Custom imports below
import komand
from komand_get_url.util.utils import Utils

from .schema import PollFileInput, PollFileOutput, Input, Output, Component


class PollFile(komand.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="poll_file",
            description=Component.DESCRIPTION,
            input=PollFileInput(),
            output=PollFileOutput(),
        )
        self.is_modified = True
        self.utils = Utils(action=self)

    def run(self, params={}):
        poll = params.get(Input.POLL, 60)

        while True:
            url = params.get(Input.URL)
            is_verify = params.get(Input.IS_VERIFY, True)
            user_agent = params.get(Input.USER_AGENT, "Mozilla/5.0")
            url_object, meta = self.utils.check_prefix_and_download(url, is_verify, user_agent)
            """File modified"""
            if url_object:
                self._save_to_cache_and_send(url_object, meta)
            time.sleep(poll)

    def _save_to_cache_and_send(self, url_object, meta):
        cache_file = "/var/cache/" + meta.get("file")
        contents = url_object.read().decode("utf-8", "replace")

        # Write etag and last modified to cache
        self.utils.create_url_meta_file(meta, url_object)

        """We can't guarantee server supports lastmodified/etag, compare contents"""
        if komand.helper.check_cachefile(cache_file):
            old_cache_file = komand.helper.open_cachefile(cache_file)
            old_contents = old_cache_file.read()
            old_cache_file.close()
            if old_contents == contents:
                self.is_modified = False
                self.logger.debug("GetUrl: File not updated")

        if self.is_modified:
            opened_cache_file = komand.helper.open_cachefile(cache_file)
            opened_cache_file.write(contents)
            opened_cache_file.close()

            # Check URL status code and return file contents
            if 200 <= url_object.code <= 299:
                self.send(
                    {
                        Output.BYTES: komand.helper.encode_string(contents).decode("utf-8"),
                        Output.STATUS_CODE: url_object.code or 200,
                    }
                )

import time
from http.client import HTTPResponse

import insightconnect_plugin_runtime

# Custom imports below
from komand_get_url.util import constants
from komand_get_url.util.utils import Utils
from .schema import PollFileInput, PollFileOutput, Input, Output, Component


class PollFile(insightconnect_plugin_runtime.Trigger):
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
        poll = params.get(Input.POLL, constants.DEFAULT_TIMEOUT)
        url = params.get(Input.URL)
        is_verify = params.get(Input.IS_VERIFY, True)
        user_agent = params.get(Input.USER_AGENT, constants.DEFAULT_USER_AGENT)
        while True:
            url_object, meta = self.utils.check_prefix_and_download(url, is_verify, user_agent)
            # File modified
            if url_object:
                self._save_to_cache_and_send(url_object, meta)
            time.sleep(poll)

    def _save_to_cache_and_send(self, url_object: HTTPResponse, meta: dict):
        """The function checks whether changes have been made to the file the user is monitoring using trigger.
        If the file under the given URL does not match the cache,
        the function refreshes the cache and returns the new file to the user.
        """
        cache_file = constants.DEFAULT_CACHE_FOLDER + meta.get("file")
        contents = url_object.read().decode(constants.DEFAULT_ENCODING, "replace")

        # Write etag and last modified to cache
        self.utils.create_url_meta_file(meta, url_object)

        # We can't guarantee server supports lastmodified/etag, compare contents
        if insightconnect_plugin_runtime.helper.check_cachefile(cache_file):
            old_contents = self.utils.read_contents_from_cache(cache_file)
            if old_contents == contents:
                self.is_modified = False
                self.logger.debug("GetUrl: File not updated")

        if self.is_modified:
            self.utils.write_contents_to_cache(cache_file, contents)

            # Check URL status code and return file contents
            if 200 <= url_object.code <= 299:
                self.send(
                    {
                        Output.BYTES: insightconnect_plugin_runtime.helper.encode_string(contents).decode(
                            constants.DEFAULT_ENCODING
                        ),
                        Output.STATUS_CODE: url_object.code or 200,
                    }
                )

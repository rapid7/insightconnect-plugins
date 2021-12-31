import komand
from komand.exceptions import PluginException
from komand_get_url.util.utils import Utils

from .schema import GetFileInput, GetFileOutput, Input, Output, Component


class GetFile(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_file",
            description=Component.DESCRIPTION,
            input=GetFileInput(),
            output=GetFileOutput(),
        )
        self.utils = Utils(action=self)

    def run(self, params={}):
        url = params.get(Input.URL)
        checksum = params.get(Input.CHECKSUM)
        timeout = params.get(Input.TIMEOUT, 60)
        is_verify = params.get(Input.IS_VERIFY, True)
        user_agent = params.get(Input.USER_AGENT, "Mozilla/5.0")
        url_object, meta = self.utils.check_prefix_and_download(url, is_verify, user_agent, timeout)
        cache_file = "/var/cache/" + meta.get("file")
        if url_object:
            contents = url_object.read().decode("utf-8", "replace")
            # Optional integrity check of file
            if checksum and not komand.helper.check_hashes(contents, checksum):
                self.logger.error("GetFile: File Checksum Failed")
                raise PluginException(cause="GetURL Failed", assistance="File Checksum Failed")

            # Write etag and last modified to cache
            self.utils.create_url_meta_file(meta, url_object)

            # Write URL file contents to cache
            old_cache_file = komand.helper.open_cachefile(cache_file)
            old_cache_file.write(contents)
            old_cache_file.close()

            # Check URL status code and return file contents
            if not url_object.code or 200 <= url_object.code <= 299:
                return {
                    Output.BYTES: komand.helper.encode_string(contents).decode("utf-8"),
                    Output.STATUS_CODE: url_object.code or 200,
                }

        # When the download fails or file is not modified
        else:
            # Attempt to return file from cache if available
            self.logger.info(f"GetURL: File not modified: {url}")
            if komand.helper.check_cachefile(cache_file):
                self.logger.info(f"GetURL: File returned from cache: {cache_file}")
                return {Output.BYTES: komand.helper.encode_file(cache_file).decode("utf-8"), Output.STATUS_CODE: 200}

        # If file hasn't been returned then we fail
        self.logger.info(f"GetURL: Download failed for {url}")
        raise PluginException(preset=PluginException.Preset.UNKNOWN, assistance=f"Download failed for {url}")

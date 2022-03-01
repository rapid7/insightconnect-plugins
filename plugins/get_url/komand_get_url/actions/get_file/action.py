import komand
from komand.exceptions import PluginException

from komand_get_url.util import constants
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
        timeout = params.get(Input.TIMEOUT, constants.DEFAULT_TIMEOUT)
        is_verify = params.get(Input.IS_VERIFY, True)
        user_agent = params.get(Input.USER_AGENT, constants.DEFAULT_USER_AGENT)
        url_object, meta = self.utils.check_prefix_and_download(url, is_verify, user_agent, timeout)
        cache_file = constants.DEFAULT_CACHE_FOLDER + meta.get("file")
        if url_object:
            contents = url_object.read().decode(constants.DEFAULT_ENCODING, "replace")
            # Optional integrity check of file
            if checksum and not komand.helper.check_hashes(contents, checksum):
                self.logger.error("GetFile: File Checksum Failed")
                raise PluginException(
                    cause="Checksums between the downloaded file and provided checksum did not match.",
                    assistance="Verify the file you meant to download and the checksum you provided are correct.",
                )

            # Write etag and last modified to cache
            self.utils.create_url_meta_file(meta, url_object)

            # Write URL file contents to cache
            self.utils.write_contents_to_cache(cache_file, contents)

            # Check URL status code and return file contents
            if not url_object.code or 200 <= url_object.code <= 299:
                return {
                    Output.BYTES: komand.helper.encode_string(contents).decode(constants.DEFAULT_ENCODING),
                    Output.STATUS_CODE: url_object.code or 200,
                }

        # When the download fails or file is not modified
        else:
            # Attempt to return file from cache if available
            self.logger.info(f"GetURL: File not modified: {url}")
            if komand.helper.check_cachefile(cache_file):
                self.logger.info(f"GetURL: File returned from cache: {cache_file}")
                return {
                    Output.BYTES: komand.helper.encode_file(cache_file).decode(constants.DEFAULT_ENCODING),
                    Output.STATUS_CODE: 200,
                }

        # If file hasn't been returned then we fail
        self.logger.info(f"GetURL: Download failed for {url}")
        raise PluginException(preset=PluginException.Preset.UNKNOWN, assistance=f"Download failed for {url}")

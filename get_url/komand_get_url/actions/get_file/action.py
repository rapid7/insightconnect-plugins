import komand
from .schema import GetFileInput, GetFileOutput, Input, Output, Component
# Custom imports below
from komand_get_url.util.utils import Utils
from komand.exceptions import PluginException
import http


class GetFile(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_file',
            description=Component.DESCRIPTION,
            input=GetFileInput(),
            output=GetFileOutput())

    def run(self, params={}):
        utils = Utils(action=self)
        url = params.get(Input.URL)
        checksum = params.get(Input.CHECKSUM)
        tout = params.get(Input.TIMEOUT, 60)
        is_verify = params.get(Input.IS_VERIFY, True)

        # Check for supported url prefix
        utils.validate_url(url)

        meta = utils.hash_url(url)
        cache_file = "/var/cache/" + meta["file"]

        # Attempt to retrieve headers from past request
        headers = {}
        if komand.helper.check_cachefile(meta["metafile"]):
            headers = utils.check_url_meta_file(meta)

        # Download file
        url_object = komand.helper.open_url(
            url, timeout=tout, verify=is_verify,
            If_None_Match=headers.get("etag", ""),
            If_Modified_Since=headers.get("last-modified", ""),
            User_Agent=params.get(Input.USER_AGENT, "Mozilla/5.0"))

        if url_object:
            contents = url_object.read(8388608).decode('utf-8')

            # Optional integrity check of file
            if checksum:
                if not komand.helper.check_hashes(contents, checksum):
                    self.logger.error("GetFile: File Checksum Failed")
                    raise PluginException(cause="GetURL Failed",
                                          assistance="File Checksum Failed")

            # Write etag and last modified to cache
            utils.create_url_meta_file(meta, url_object)

            # Write URL file contents to cache
            f = komand.helper.open_cachefile(cache_file)
            f.write(contents)
            f.close()

            # Check URL status code and return file contents
            if url_object.code is None or url_object.code >= 200 or url_object.code <= 299:
                f = komand.helper.encode_string(contents)
                if f:
                    return {Output.BYTES: f.decode('utf-8'), Output.STATUS_CODE: url_object.code or 200}

        # When the download fails or file is not modified
        if url_object is None:
            # Attempt to return file from cache if available
            self.logger.info(f"GetURL: File not modified: {url}")
            if komand.helper.check_cachefile(cache_file):
                f = komand.helper.encode_file(cache_file)
                self.logger.info(f"GetURL: File returned from cache: {cache_file}")
                return {Output.BYTES: f.decode('utf-8'), Output.STATUS_CODE: 200}

        # If file hasn't been returned then we fail
        self.logger.info(f"GetURL: Download failed for {url}")
        raise PluginException(preset=PluginException.Preset.UNKNOWN, assistance=f"Download failed for {url}")

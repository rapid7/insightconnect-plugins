import komand
from .schema import GetFileInput, GetFileOutput
# Custom imports below
from komand_get_url.util.utils import Utils


class GetFile(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_file',
            description='Download a file by URL',
            input=GetFileInput(),
            output=GetFileOutput())

    def run(self, params={}):
        utils = Utils(action=self)
        url = params.get('url')
        checksum = params.get('checksum')
        tout = params.get('timeout', 60)
        is_verify = params.get('is_verify', True)

        # Check for supported url prefix
        utils.validate_url(url)

        meta = utils.hash_url(url)
        cache_file = '/var/cache/' + meta['file']

        # Attempt to retrieve headers from past request
        headers = {}
        if komand.helper.check_cachefile(meta['metafile']):
            headers = utils.check_url_meta_file(meta)

        # Download file
        urlobj = komand.helper.open_url(
            url, timeout=tout, verify=is_verify,
            If_None_Match=headers.get('etag', ''),
            If_Modified_Since=headers.get('last-modified', ''))

        if urlobj:
            contents = urlobj.read()

            # Optional integrity check of file
            if checksum:
                if not komand.helper.check_hashes(contents, checksum):
                    self.logger.error('GetFile: File Checksum Failed')
                    raise Exception('GetURL Failed')

            # Write etag and last modified to cache
            utils.create_url_meta_file(meta, urlobj)

            # Write URL file contents to cache
            f = komand.helper.open_cachefile(cache_file)
            f.write(contents)
            f.close()

            # Check URL status code and return file contents
            if urlobj.code >= 200 or urlobj.code <= 299:
                f = komand.helper.encode_string(contents)
                if f:
                    return {'file': f, 'status_code': urlobj.code or 200}

        # When the download fails or file is not modified
        if urlobj is None:
            # Attempt to return file from cache if available
            self.logger.info('GetURL: File not modified: %s', url)
            if komand.helper.check_cachefile(cache_file):
                f = komand.helper.encode_file(cache_file)
                self.logger.info('GetURL: File returned from cache: %s', cache_file)
                return {'bytes': f, 'status_code': 200}

        # If file hasn't been returned then we fail
        self.logger.info('GetURL: Download failed for %s', url)
        raise Exception('GetURL Failed')

    def test(self, params={}):
        url = 'https://www.google.com'
        komand.helper.check_url(url)
        return {}

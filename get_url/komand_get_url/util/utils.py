import komand
import json
import hashlib
from komand.exceptions import PluginException


class Utils(object):

    def __init__(self, action):
        self.logger = action.logger

    def validate_url(self, url):
        """Check for supported URL prefixes from url string"""
        if url.startswith("http://") or url.startswith("https://") or url.startswith("ftp://"):
            return True
        self.logger.info(f"GetURL: Unsupported URL prefix: {url}")
        raise PluginException(preset=PluginException.Preset.UNKNOWN,
                              assistance=f"GetURL: Unsupported URL prefix: {url}")

    def get_headers(self, url_object):
        """Return cache related headers from urllib2 headers dictonary"""
        if "etag" or "last-modified" in url_object.headers.dict:
            etag = url_object.headers.get("etag")
            lm = url_object.headers.get("last-modified")
            return {"etag": etag, "last-modified": lm}

        self.logger.error("GetHeaders: Error occurred while obtaining etag and last-modified headers")

    def hash_url(self, url):
        """Creates a dictionary containing hashes from a url of type string"""
        try:
            self.logger.info(f"url: {url}")
            sha1 = hashlib.sha1(url.encode("utf-8")).hexdigest()
            contents = sha1 + ".file"
            meta_file = sha1 + ".meta"
            self.logger.info(f"HashUrl: Url hashed successfully: {sha1}")
            return {"file": contents, "url": url, "hash": sha1, "metafile": meta_file}
        except Exception as e:
            self.logger.error(f"HashUrl: Error hashing url {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)

    def create_url_meta_file(self, meta, url_object):
        """Create metadata file from meta info information"""
        headers = self.get_headers(url_object)
        data = {
            "url": meta.get("url"),
            "last-modified": headers.get("last-modified"),
            "etag": headers.get("etag"),
            "file": meta.get("file")
        }
        with komand.helper.open_cachefile(meta["metafile"]) as f:
            json.dump(data, f)
        self.logger.info(f"CreateUrlMetaFile: MetaFile created: {str(data)}")

    def check_url_meta_file(self, meta):
        """Check caching headers from meta info dictionary"""
        try:
            with komand.helper.open_cachefile(meta["metafile"]) as f:
                data = json.load(f)
            return data
        except Exception as e:
            self.logger.error(f"CheckUrlMetaFile: Error while retreving meta file, error {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  assistance="Error while retreving meta file",
                                  data=e)

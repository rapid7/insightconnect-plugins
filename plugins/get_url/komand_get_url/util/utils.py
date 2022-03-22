import hashlib
import json
from http.client import HTTPResponse

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from typing import AnyStr


class Utils(object):
    def __init__(self, action):
        self.logger = action.logger

    def validate_url(self, url: str) -> bool:
        """Check for supported URL prefixes from url string"""
        if url.startswith("http://") or url.startswith("https://") or url.startswith("ftp://"):
            return True
        self.logger.info(f"GetURL: Unsupported URL prefix: {url}")
        raise PluginException(
            preset=PluginException.Preset.UNKNOWN,
            assistance=f"GetURL: Unsupported URL prefix: {url}",
        )

    def __get_headers(self, url_object: HTTPResponse) -> dict:
        """Return cache related headers from urllib2 headers dictonary"""
        etag = url_object.headers.get("etag")
        lm = url_object.headers.get("last-modified")
        return {"etag": etag, "last-modified": lm}

    def hash_url(self, url: str) -> dict:
        """Creates a dictionary containing hashes from a url of type string"""
        try:
            self.logger.info(f"url: {url}")
            sha1 = hashlib.sha1(url.encode("utf-8")).hexdigest()  # noqa: B303
            contents = sha1 + ".file"
            meta_file = sha1 + ".meta"
            self.logger.info(f"HashUrl: Url hashed successfully: {sha1}")
            return {"file": contents, "url": url, "hash": sha1, "metafile": meta_file}
        except Exception as e:
            self.logger.error(f"HashUrl: Error hashing url {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)

    def create_url_meta_file(self, meta: dict, url_object: HTTPResponse):
        """Create metadata file from meta info information"""
        headers = self.__get_headers(url_object)
        data = {
            "url": meta.get("url"),
            "last-modified": headers.get("last-modified"),
            "etag": headers.get("etag"),
            "file": meta.get("file"),
        }
        with insightconnect_plugin_runtime.helper.open_cachefile(meta.get("metafile")) as loaded_file:
            json.dump(data, loaded_file)
        self.logger.info(f"CreateUrlMetaFile: MetaFile created: {str(data)}")

    def check_url_meta_file(self, meta: dict):
        """Check caching headers from meta info dictionary"""
        try:
            with insightconnect_plugin_runtime.helper.open_cachefile(meta.get("metafile")) as loaded_file:
                data = json.load(loaded_file)
            return data
        except Exception as e:
            self.logger.error(f"CheckUrlMetaFile: Error while retrieving meta file, error {e}")
            raise PluginException(
                preset=PluginException.Preset.UNKNOWN,
                assistance="Error while retrieving meta file",
                data=e,
            )

    def check_prefix_and_download(
        self, url: str, is_verify: bool, user_agent: str, timeout: int = None
    ) -> (HTTPResponse, dict):
        """Check for supported url prefix"""
        self.validate_url(url)
        meta = self.hash_url(url)

        # Attempt to retrieve headers from past request
        headers = {}
        if insightconnect_plugin_runtime.helper.check_cachefile(meta.get("metafile")):
            headers = self.check_url_meta_file(meta)

        # Download file
        url_object = insightconnect_plugin_runtime.helper.open_url(
            url,
            timeout=timeout,
            verify=is_verify,
            If_None_Match=headers.get("etag", ""),
            If_Modified_Since=headers.get("last-modified", ""),
            User_Agent=user_agent,
        )
        return url_object, meta

    def write_contents_to_cache(self, cache_file: str, contents: bytes):
        try:
            old_cache_file = insightconnect_plugin_runtime.helper.open_cachefile(cache_file)
            old_cache_file.write(contents)
            old_cache_file.close()
        except IOError as error:
            raise PluginException(
                cause="Error appear while saving data to cache file.",
                assistance="Please contact support for assistance.",
                data=error,
            )

    def read_contents_from_cache(self, cache_file: str) -> AnyStr:
        try:
            old_cache_file = insightconnect_plugin_runtime.helper.open_cachefile(cache_file)
            old_contents = old_cache_file.read()
            old_cache_file.close()
        except Exception as error:
            raise PluginException(
                cause="Error appear while reading contents from cache file.",
                assistance="Please contact support for assistance.",
                data=error,
            )
        return old_contents

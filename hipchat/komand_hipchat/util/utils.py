import komand
import json
import base64
import urllib2
import hashlib
import os
import socket
import ssl
import subprocess

class Utils(object):

    def __init__(self, logger):
        self.logger = logger

    def validate_url(self, url):
        '''Check for supported URL prefixes from url string'''
        if url.startswith('http://') or url.startswith('https://') or url.startswith('ftp://'):
            return True
        self.logger.info('GetURL: Unsupported URL prefix: %s', url)
        raise Exception('GetURL Failed')


    def get_headers(self, urlobj):
        '''Return cache related headers from urllib2 headers dictonary'''
        if 'etag' or 'last-modified' in urlobj.headers.dict.keys():
            etag = urlobj.headers.get('etag')
            lm   = urlobj.headers.get('last-modified')
            return {'etag': etag, 'last-modified': lm }
        self.logger.error('GetHeaders: Error occured while obtaining etag and last-modified headers')

    def hash_url(self, url):
        '''Creates a dictionary containting hashes from a url of type string'''
        try:
            sha1 = hashlib.sha1(url).hexdigest()
            contents = sha1 + '.file'
            metafile = sha1 + '.meta'
            self.logger.info('HashUrl: Url hashed successfully: ' + sha1)
            return {'file': contents, 'url': url, 'hash': sha1, 'metafile': metafile}
        except:
            self.logger.error('HashUrl: Error hashing url')
        raise Exception('Url hash Failed')


    def create_url_meta_file(self, meta, urlobj):
        '''Create metadata file from meta info information'''
        headers = self.get_headers(urlobj)
        data    = {
            'url': meta.get('url'),
            'last-modified': headers.get('last-modified'),
            'etag': headers.get('etag'),
            'file': meta.get('file')
        }
        with komand.helper.open_cachefile(meta['metafile']) as f:
            json.dump(data, f)
            self.logger.info('CreateUrlMetaFile: MetaFile created: ' + str(data))


    def check_url_meta_file(self, meta):
        '''Check caching headers from meta info dictionary'''
        try:
            with komand.helper.open_cachefile(meta['metafile']) as f:
                data = json.load(f)
                return data
        except:
            self.logger.error('CheckUrlMetaFile: Error while retreving meta file')

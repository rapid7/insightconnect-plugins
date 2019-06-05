import requests
from urllib.parse import quote
from requests.auth import HTTPBasicAuth


def test_auth(log, host, username=None, password=None):
    if not host.endswith('/'):
        host += '/'
    headers = {'Accept': 'application/json'}
    try:
        if not username:
            resp = requests.get(host, headers=headers)
        else:
            resp = requests.get(host, auth=HTTPBasicAuth(username, password), headers=headers)

        if resp.status_code >= 200 and resp.status_code <= 399:
            return resp.json()

    except requests.exceptions.HTTPError:
        log.error('Requests: HTTPError: status code %s for %s' % (str(resp.status_code), host))
    except requests.exceptions.Timeout:
        log.error('Requests: Timeout for %s' % host)
    except requests.exceptions.TooManyRedirects:
        log.error('Requests: TooManyRedirects for %s' % host)
    except requests.exceptions.ConnectionError:
        log.error('Requests: ConnectionError for %s' % host)
    raise Exception("Call failed: unknown error")


def put_index(log, host, index, type_, id_, document, username=None, password=None, params=None):
    if not host.endswith('/'):
        host += '/'
    url = host + index + '/' + type_ + '/' + id_ + '?'
    if params:
        d = [k + '=' + quote(v) for k, v in params.items()]
        url += '&'.join(d)
    headers = {'Content-Type': 'application/json'}
    try:
        if not username:
            resp = requests.put(url, json=document, headers=headers)
        else:
            resp = requests.put(url, json=document, auth=HTTPBasicAuth(username, password), headers=headers)

        if resp.status_code >= 200 and resp.status_code <= 399:
            return resp.json()

    except requests.exceptions.HTTPError:
        log.error('Requests: HTTPError: status code %s for %s' % (str(resp.status_code), url))
    except requests.exceptions.Timeout:
        log.error('Requests: Timeout for %s' % url)
    except requests.exceptions.TooManyRedirects:
        log.error('Requests: TooManyRedirects for %s' % url)
    except requests.exceptions.ConnectionError:
        log.error('Requests: ConnectionError for %s' % url)
    raise Exception("Call failed: unknown error")


def post_index(log, host, index, type_, document, username=None, password=None, params=None):
    if not host.endswith('/'):
        host += '/'
    url = host + index + '/' + type_ + '?'
    if params:
        d = [k + '=' + quote(v) for k, v in params.items()]
        url += '&'.join(d)
    headers = {'Content-Type': 'application/json'}
    try:
        if not username:
            resp = requests.post(url, json=document, headers=headers)
        else:
            resp = requests.post(url, json=document, auth=HTTPBasicAuth(username, password), headers=headers)

        if resp.status_code >= 200 and resp.status_code <= 399:
            return resp.json()

    except requests.exceptions.HTTPError:
        log.error('Requests: HTTPError: status code %s for %s' % (str(resp.status_code), url))
    except requests.exceptions.Timeout:
        log.error('Requests: Timeout for %s' % url)
    except requests.exceptions.TooManyRedirects:
        log.error('Requests: TooManyRedirects for %s' % url)
    except requests.exceptions.ConnectionError:
        log.error('Requests: ConnectionError for %s' % url)
    raise Exception("Call failed: unknown error")


def post_update(log, host, index, type_, id_, script, username=None, password=None, params=None):
    if not host.endswith('/'):
        host += '/'
    url = host + index + '/' + type_ + '/' + id_ + '/' + '_update' + '?'
    if params:
        d = [k + '=' + quote(v) for k, v in params.items()]
        url += '&'.join(d)
    headers = {'Content-Type': 'application/json'}
    try:
        if not username:
            resp = requests.post(url, json=script, headers=headers)
        else:
            resp = requests.post(url, json=script, auth=HTTPBasicAuth(username, password), headers=headers)

        if resp.status_code >= 200 and resp.status_code <= 399:
            return resp.json()

    except requests.exceptions.HTTPError:
        log.error('Requests: HTTPError: status code %s for %s' % (str(resp.status_code), url))
    except requests.exceptions.Timeout:
        log.error('Requests: Timeout for %s' % url)
    except requests.exceptions.TooManyRedirects:
        log.error('Requests: TooManyRedirects for %s' % url)
    except requests.exceptions.ConnectionError:
        log.error('Requests: ConnectionError for %s' % url)
    raise Exception("Call failed: unknown error")


def get_search(log, host, index, type_, query=None, username=None, password=None, params=None):
    if not host.endswith('/'):
        host += '/'
    url = host + index + '/' + type_ + '/' + '_search?'
    if params:
        d = [k + '=' + quote(v) for k, v in params.items()]
        url += '&'.join(d)
    headers = {'Content-Type': 'application/json'}

    if not query:
        query = {}

    query['version'] = True
    try:
        if not username:
            resp = requests.get(url, json=query, headers=headers)
        else:
            resp = requests.get(url, json=query, auth=HTTPBasicAuth(username, password), headers=headers)

        if resp.status_code >= 200 and resp.status_code <= 399:
            return resp.json()

    except requests.exceptions.HTTPError:
        log.error('Requests: HTTPError: status code %s for %s' % (str(resp.status_code), url))
    except requests.exceptions.Timeout:
        log.error('Requests: Timeout for %s' % url)
    except requests.exceptions.TooManyRedirects:
        log.error('Requests: TooManyRedirects for %s' % url)
    except requests.exceptions.ConnectionError:
        log.error('Requests: ConnectionError for %s' % url)
    raise Exception("Call failed: unknown error")


def get_health(log, host, username=None, password=None):
    if not host.endswith('/'):
        host += '/'
    url = host + '_cluster/health'
    headers = {'Content-Type': 'application/json'}
    try:
        if not username:
            resp = requests.get(url, headers=headers)
        else:
            resp = requests.get(url, auth=HTTPBasicAuth(username, password), headers=headers)

        if resp.status_code >= 200 and resp.status_code <= 399:
            return resp.json()

    except requests.exceptions.HTTPError:
        log.error('Requests: HTTPError: status code %s for %s' % (str(resp.status_code), url))
    except requests.exceptions.Timeout:
        log.error('Requests: Timeout for %s' % url)
    except requests.exceptions.TooManyRedirects:
        log.error('Requests: TooManyRedirects for %s' % url)
    except requests.exceptions.ConnectionError:
        log.error('Requests: ConnectionError for %s' % url)
    raise Exception("Call failed: unknown error")

import requests 
import re
import base64
 

def add_schema(url):
    '''Returns a URL with scheme supplied given a URL string'''
    if 'http://' in url or 'https://' in url: return url
    else: return 'http://' + url

def try_req(f):
    def wrapper(*args, **kwargs):
      try:
          resp = f(*args, **kwargs)
          if resp.status_code >= 200 and resp.status_code <= 399:
              return resp
      except requests.exceptions.HTTPError:
          self.logger.error('Requests: HTTPError: status code %s for %s' % (str(resp.status_code), ', '.join(args)))
      except requests.exceptions.Timeout:
          self.logger.error('Requests: Timeout for %s' % ', '.join(args))
      except requests.exceptions.TooManyRedirects:
          self.logger.error('Requests: TooManyRedirects for %s' % ', '.join(args))
      except requests.exceptions.ConnectionError:
          self.logger.error('Requests: ConnectionError for %s' % ', '.join(args))
      return None
    return wrapper

@try_req
def head_url(url):
    '''Returns a request HEAD object given a URL as a string'''
    return requests.head(add_schema(url))

@try_req
def post_url(url, data, headers):
    '''Returns a request POST object given a URL as a string, data, and a header dic'''
    return requests.post(add_schema(url), data=data, headers=headers)

@try_req
def get_url(url, headers=None):
    '''Returns a request GET object given a URL as a string and a header dic'''
    return requests.get(add_schema(url), headers=headers)

@try_req
def delete_url(url, headers=None):
    '''Returns a request DELETE object given a URL as a string and a header dic'''
    return requests.delete(add_schema(url), headers=headers)
  
def get_users(host, auth, search=None):
    '''Returns a List of Users in dictionary form given a host and an auth string'''
    url = host + 'wp/v2/users?context=edit&per_page=100'
    if search: url += '&search=' + search
    headers = {'Authorization': auth, 'Accept': 'application/json'}
    try:
        resp = requests.get(url, headers=headers) 
        if resp.status_code >= 200 and resp.status_code <= 399:
            return resp.json()
    except requests.exceptions.HTTPError:
        self.logger.error('Requests: HTTPError: status code %s for %s' % (str(resp.status_code), ', '.join(args)))
    except requests.exceptions.Timeout:
        self.logger.error('Requests: Timeout for %s' % ', '.join(args))
    except requests.exceptions.TooManyRedirects:
        self.logger.error('Requests: TooManyRedirects for %s' % ', '.join(args))
    except requests.exceptions.ConnectionError:
        self.logger.error('Requests: ConnectionError for %s' % ', '.join(args))
    return None

def test_auth(host, auth):
    url = host + 'wp/v2/users?context=edit'
    headers = {'Authorization': auth, 'Accept': 'application/json'}
    try:
        resp = requests.get(url, headers=headers) 
        if resp.status_code >= 200 and resp.status_code <= 399:
            return True
    except requests.exceptions.HTTPError:
        self.logger.error('Requests: HTTPError: status code %s for %s' % (str(resp.status_code), ', '.join(args)))
    except requests.exceptions.Timeout:
        self.logger.error('Requests: Timeout for %s' % ', '.join(args))
    except requests.exceptions.TooManyRedirects:
        self.logger.error('Requests: TooManyRedirects for %s' % ', '.join(args))
    except requests.exceptions.ConnectionError:
        self.logger.error('Requests: ConnectionError for %s' % ', '.join(args))
    return False

def delete_user(host, auth, user_id, assignee_id=None):
    '''Returns a request DELETE object given a host url, a b64 auth string, and a user_id'''
    url = host + 'wp/v2/users/' + user_id + '?force=true'
    if assignee_id: url += '&reassign=' + assignee_id
    headers = {'Authorization': auth, 'Accept': 'application/json'}
    return delete_url(url, headers)

def get_api_route(link):
    '''Returns the api root URL given a link header string'''
    links = [l.strip() for l in link.split(',')]
    if not links: return None
    
    for l in links:
        if 'rel="https://api.w.org/"' in l:
            m = re.match(r'<(.*?)>', l)
            if not m: continue
            else: return m.group(1)
    return None

def api_installed(url):
    '''Returns boolean given a URL'''
    resp = get_url(url)
    if not resp: return False
    r = resp.json()
    namespaces = r.get('namespaces')
    if type(namespaces) is not list: return None
    if 'wp/v2' in namespaces: return True
    else: return False
    return None

def encode_creds(username, password):
    '''Returns the content of an Authorization Header given a username and password'''
    creds = username + ':' + password
    return b'Basic ' + base64.b64encode(bytes(creds, 'utf-8'))

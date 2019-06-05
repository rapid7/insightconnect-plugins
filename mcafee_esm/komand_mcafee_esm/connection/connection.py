import komand
from .schema import ConnectionSchema
# Custom imports below
import base64
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

        self.esm_session = None
        self.url = None

    def connect(self, params):
        host, port, user, password = params.get("hostname"), params.get("port"),\
                base64.b64encode(params.get("credentials").get("username").encode()).decode(),\
            base64.b64encode(params.get("credentials").get("password").encode()).decode()

        self.url = 'https://{}:{}/rs/esm/'.format(host, port)
        payload = {"username": user,"password": password,"locale": "en_US"}
        url = self.url + "login"

        r = requests.session()
        r.headers['Content-Type'] = 'application/json'
        resp = r.post(url, json=payload, verify=False)
        # Move csrf headers to session
        r.headers['Cookie'] = resp.headers.get('Set-Cookie')
        r.headers['X-Xsrf-Token'] = resp.headers.get('Xsrf-Token')
        self.esm_session = r

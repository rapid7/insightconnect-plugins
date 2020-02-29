import requests

import komand
from .schema import LookupInput, LookupOutput, Output, Component


class Lookup(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='lookup',
            description=Component.DESCRIPTION,
            input=LookupInput(),
            output=LookupOutput())

    def run(self, params={}):
        url = 'https://api.ipify.org?format=json'
        r = requests.get(url)
        return {
            Output.ADDRESS: r.json().pop('ip')
        }

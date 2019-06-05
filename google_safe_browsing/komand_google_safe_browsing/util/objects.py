# File to hold all objects to ease construction of JSON payload.
# Non-PEP8 property declaration used as JSON serializing is 1:1, eg. "clientId = clientId", not "client_id = clientId"


class Client(object):
    clientId = ""
    clientVersion = "0.0.1"

    def __init__(self, client_id, client_version="0.0.1"):
        self.clientId = client_id
        self.clientVersion = client_version


class ThreatEntry(object):

    def __init__(self, url):
        self.url = url


class ThreatInfo(object):

    def __init__(self, threatTypes, platformTypes, threatEntryTypes, threatEntries):
        self.threatTypes = threatTypes
        self.platformTypes = platformTypes
        self.threatEntryTypes = threatEntryTypes
        self.threatEntries = threatEntries


class Request(object):

    def __init__(self, client, threatInfo):
        self.client = client
        self.threatInfo = threatInfo

import komand
from .schema import ListingInput, ListingOutput
# Custom imports below
from grr_api_client import api
import json
from google.protobuf.json_format import MessageToJson


class Listing(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='listing',
                description='Looks for exposed secrets in the git commit history and branches',
                input=ListingInput(),
                output=ListingOutput())
        self.grrapi = None
        self.query = None
        self.result = {}

    def run(self, params={}):
        self.grrapi = self.connection.grrapi
        if params.get('hunts'):
            self.hunts()
        if params.get('hunt_approvals'):
            self.hunt_approvals()
        if params.get('grr_binaries'):
            self.grr_binaries()
        if params.get('clients'):
            query = params.get('query').encode("utf-8", "ignore")
            self.clients(query)
        return {'result': self.result}

    def hunts(self):
        try:
            list_hunts = self.grrapi.ListHunts()
            result = {}
            count = 0
            for hunt in list_hunts:
                data = hunt.data
                data = MessageToJson(data)
                result["hunt%s" % count] = json.loads(data)
                count += 1
            self.result = komand.helper.clean(result)
        except Exception as e:
            self.logger.error(e)

    def hunt_approvals(self):
        # Still testing, need to create a hunt to see the hunt approval and how the data comes out
        try:
            hunt_approvals = self.grrapi.ListHuntApprovals()
            self.logger.info(hunt_approvals.data)
            count = 0
            result = {}
            for item in hunt_approvals:
                data = item.data
                data = MessageToJson(data)
                result["approval%s" % count] = json.loads(data)
                count += 1
            self.result = komand.helper.clean(result)
        except Exception as e:
            self.logger.error(e)

    def clients(self, query):
        try:
            search_results = self.grrapi.SearchClients(query)
            result = {}
            count = 0
            if not search_results:
                return {'results': 'No clients found'}
            for client in search_results:
                data = client.data
                data = MessageToJson(data)
                result["client%s" % count] = json.loads(data)
                count += 1
            if result == {}:
                self.logger.error('No clients found with provided query.')
                return {'results': 'No clients have been found'}
            self.result = komand.helper.clean(result)
        except Exception as e:
            self.logger.error(e)

    def grr_binaries(self):
        # Havn't tested it, but based on the other functions behaving similarly and the source code
        # I am going to assume this works until tested
        try:
            binaries = self.grrapi.ListGrrBinaries()
            count = 0
            result = {}
            for x in binaries:
                data = x.data
                data = MessageToJson(data)
                result["binary%s" % count] = json.loads(data)
                count += 1
            self.result = komand.helper.clean(result)
        except Exception as e:
            self.logger.error(e)
            self.logger.error('No GRR Binaries')
            return {'results': 'No GRR Binaries have been found'}

    def test(self):
        self.grrapi = self.connection.grrapi
        if self.grrapi:
            return {'results': 'Ready to list'}
        if not self.grrapi:
            return {'results': 'Not ready. Please check your connection with the GRR Client'}

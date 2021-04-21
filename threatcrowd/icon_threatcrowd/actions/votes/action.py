import insightconnect_plugin_runtime
from .schema import VotesInput, VotesOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
# Custom imports below
import socket
from urllib.parse import urlparse
import validators


class Votes(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='votes',
            description=Component.DESCRIPTION,
            input=VotesInput(),
            output=VotesOutput())

    @staticmethod
    def url_ip_check(entity):
        if not entity.startswith('http://'):
            entity = 'http://' + entity

        address = urlparse(entity).netloc
        try:
            socket.gethostbyname(address)
            return address
        except Exception as e:
            raise PluginException(cause='Failed to cast vote.',
                                  assistance='User input must be either a valid email, URL or IP address.',
                                  data=e)

    def entity_check(self, entity):
        # check if entity is email
        if validators.email(entity):
            return entity

        # check if entity is IP or URL
        return self.url_ip_check(entity)

    @staticmethod
    def parse_vote(vote):
        vote_convert = {True: 1, False: 0}
        return vote_convert[vote]

    def run(self, params={}):
        vote = self.parse_vote(params.get(Input.VOTE))
        entity = params.get(Input.ENTITY)
        data = self.connection.client.vote_malicious(vote, self.entity_check(entity))

        if not data or int(data.status_code) > 200:
            self.logger.error('ThreatCrowd API did not return any matches')
            raise PluginException(cause='Vote submission failed for unknown reason.')

        return {Output.STATUS: str(data.status_code)}

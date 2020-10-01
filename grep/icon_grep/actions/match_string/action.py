import komand
from .schema import MatchStringInput, MatchStringOutput, Input, Output
# Custom imports below
from icon_grep.util import utils


class MatchString(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='match_string',
            description='Find pattern in string',
            input=MatchStringInput(),
            output=MatchStringOutput())

    def run(self, params={}):
        text = params.get(Input.TEXT)
        pattern = params.get(Input.PATTERN)
        behavior = params.get(Input.BEHAVIOR)

        output = utils.process_grep(utils.run_grep(self.logger, text, pattern, behavior))

        return {
            Output.FOUND: output.get('found'),
            Output.HITS: output.get('hits'),
            Output.MATCHES: output.get('matches')
        }

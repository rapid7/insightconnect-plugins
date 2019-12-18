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
        output = utils.process_grep(
            utils.echo_lines(
                self.logger,
                params.get(Input.TEXT),
                params.get(Input.PATTERN),
                params.get(Input.BEHAVIOR)
            )
        )

        return {
            Output.FOUND: output.get(utils.FOUND),
            Output.HITS: output.get(utils.HITS),
            Output.MATCHES: output.get(utils.MATCHES)
        }

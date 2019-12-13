import komand
import tempfile
from .schema import MatchStringInput, MatchStringOutput
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
        text = params.get('text')

        path = tempfile.mkdtemp() + "/"
        fname = "tmp.txt"
        with open(path + fname, 'w') as f:
            f.write(text)

        pattern = params.get('pattern')
        behavior = params.get('behavior')
        matches = str.splitlines(utils.print_lines(self.logger, path + fname, pattern, behavior, path))
        if matches:
            found = True
            hits = len(matches)
        else:
            found = False
            matches = ""
            hits = 0
        matches = matches if hits != 0 else []
        return {'found': found, 'hits': hits, 'matches': matches}

import komand
from .schema import MatchBase64Input, MatchBase64Output
# Custom imports below
import shutil
import tempfile
from bs4 import UnicodeDammit
import base64
from komand_grep.util import utils


class MatchBase64(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='match_base64',
                description='Find pattern in base64 file',
                input=MatchBase64Input(),
                output=MatchBase64Output())

    def run(self, params={}):
        try:
            decoded = base64.b64decode(params['data']).decode('utf-8')
        except Exception as ex:
            self.logger.debug(ex)
            self.logger.debug("Error decoding")
            decoded = UnicodeDammit.detwingle(params['data']).decode('utf-8', errors='ignore')

        path = tempfile.mkdtemp()+"/"
        fname = "tmp.txt"
        with open(path+fname,'w') as f:
            f.write(decoded)

        pattern = params.get('pattern')
        behavior = params.get('behavior')
        matches = str.splitlines(utils.print_lines(self.logger, path+fname, pattern, behavior, path))
        if matches:
            found = True
            hits = len(matches)
        else:
            found = False
            matches = ""
            hits = 0
        shutil.rmtree(path)
        matches = matches if hits != 0 else []
        return {'found': found, 'hits': hits, 'matches': matches}

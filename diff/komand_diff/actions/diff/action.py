import difflib
import hashlib

import komand
from .schema import DiffInput, DiffOutput, Input, Output, Component


class Diff(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='diff',
            description=Component.DESCRIPTION,
            input=DiffInput(),
            output=DiffOutput())

    def run(self, params={}):
        """Run action"""

        filename = self.md5sum(params[Input.LABEL])
        compare = params[Input.COMPARE]
        first_run = False
        different = False
        diff = ''

        if not komand.helper.check_cachefile(filename):
            first_run = True

        with komand.helper.open_cachefile(filename) as cache_file:
            self.logger.info(f"Run: Got or created cache file: {cache_file}")

            if not first_run:
                before = cache_file.read()
                self.logger.debug(f"comparing {before} {compare}")
                if compare != before:
                    different = True
                    diff = ''.join(difflib.unified_diff(before, compare, 'before', 'after'))

            cache_file.seek(0)
            cache_file.write(compare)
            cache_file.truncate()

        return {Output.DIFFERENT: different, Output.DIFF: diff}

    @staticmethod
    def md5sum(label_name):
        return hashlib.md5(label_name.encode('utf-8')).hexdigest()

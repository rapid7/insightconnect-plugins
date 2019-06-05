import komand
import hashlib
import difflib
from .schema import DiffInput, DiffOutput


def md5sum(input):
    return hashlib.md5(input.encode('utf-8')).hexdigest()


class Diff(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='diff',
                description='Diff strings',
                input=DiffInput(),
                output=DiffOutput())

    def run(self, params={}):
        """Run action"""

        filename = md5sum(params['label'])
        compare = params['compare']
        first_run = False
        different = False
        diff = ''

        if not komand.helper.check_cachefile(filename):
            first_run = True

        with komand.helper.open_cachefile(filename) as cache_file:
            self.logger.info("Run: Got or created cache file: {file}".format(file=cache_file))

            if not first_run:
                before = cache_file.read()
                self.logger.debug("comparing %s %s", before, compare)
                if compare != before:
                    different = True
                    diff = ''.join(difflib.unified_diff(before, compare, 'before', 'after'))

            cache_file.seek(0)
            cache_file.write(compare) 
            cache_file.truncate()
                
        return { 'different': different, 'diff': diff }

    def test(self):
        """Test action"""
        return { 'different': False, 'diff': ''}

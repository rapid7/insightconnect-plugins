import komand
import os
from .schema import BasenameInput, BasenameOutput


class Basename(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='basename',
                description='Get the basename of a path',
                input=BasenameInput(),
                output=BasenameOutput())

    def run(self, params={}):
        path = str(params.get('path'))
        basename = os.path.basename(path)
        if basename is None or basename is '':
            self.logger.error('Not able to retrieve basename of %s', path)
            raise Exception('Unable to find basename')
        return { 'basename': basename }

    def test(self, params={}):
        path = '/usr/local/bin/stuff'
        basename = os.path.basename(path)
        if not basename == 'stuff':
            raise Exception('Basename Failed')
        return { 'basename': basename }
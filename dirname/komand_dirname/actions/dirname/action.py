import komand
import os
from .schema import DirnameInput, DirnameOutput

class Dirname(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='dirname',
                description='Get the directory name of a path',
                input=DirnameInput(),
                output=DirnameOutput())

    def run(self, params={}):
        path = str(params.get('path'))
        dirname = os.path.dirname(path)
        if dirname is None or dirname is '':
            self.logger.error('Not able to retrieve dirname of %s', path)
            raise Exception('Dirname is empty')
        return { 'dirname': dirname }

    def test(self, params={}):
        path = '/usr/local/bin/stuff'
        dirname = os.path.dirname(path)
        if not dirname == '/usr/local/bin':
            raise Exception('Dirname Failed')
        return { 'dirname': dirname }

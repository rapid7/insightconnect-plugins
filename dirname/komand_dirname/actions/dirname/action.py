import komand
import os

from komand.exceptions import PluginException
from .schema import DirnameInput, DirnameOutput, Input, Output


class Dirname(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='dirname',
            description='Get the directory name of a path',
            input=DirnameInput(),
            output=DirnameOutput())

    def run(self, params={}):
        path = str(params.get(Input.PATH))
        dirname = os.path.dirname(path)
        if dirname is None or dirname == '':
            self.logger.error('Not able to retrieve dirname of %s', path)
            raise PluginException(cause='Dirname is empty', assistance=f'Not able to retrieve dirname of {path}')
        return {Output.DIRNAME: dirname}

    def test(self, params={}):
        path = '/usr/local/bin/stuff'
        dirname = os.path.dirname(path)
        if not dirname == '/usr/local/bin':
            raise Exception('Dirname Failed')
        return {Output.DIRNAME: dirname}

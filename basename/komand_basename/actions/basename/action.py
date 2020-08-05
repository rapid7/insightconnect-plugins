import insightconnect_plugin_runtime
import os
from .schema import BasenameInput, BasenameOutput, Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException


class Basename(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='basename',
                description='Get the basename of a path',
                input=BasenameInput(),
                output=BasenameOutput())

    def run(self, params={}):
        path = params.get(Input.PATH)
        basename = os.path.basename(path)
        if basename is None or basename == '':
            self.logger.error(f"Not able to retrieve basename of {path}")
            raise PluginException('Unable to find basename')

        return {
            Output.BASENAME: basename
        }

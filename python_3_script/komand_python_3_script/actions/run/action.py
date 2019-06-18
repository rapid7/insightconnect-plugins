import komand
from .schema import RunOutput, RunInput, Component
import sys
sys.path.append("/var/cache/python_dependencies/lib/python3.7/site-packages")


class Run(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='run',
                description=Component.DESCRIPTION,
                input=RunInput(),
                output=RunOutput())

    def run(self, params={}):
        self.logger.info('Input: (below)\n\n%s\n', params['input'])
        self.logger.info('Function: (below)\n\n%s\n', params['function'])

        try:
            func = params['function']
            exec(func)
            funcname = func.split(' ')[1].split('(')[0]
            out = locals()[funcname](params['input'])
        except Exception as e:
            raise Exception('Could not run supplied script. Error: ' + str(e))
        try:
            if out is None:
                raise Exception('Output type was None. Ensure that output has a non-None data type')
            return out
        except UnboundLocalError:
            raise Exception('No output was returned. Check supplied script to ensure that it returns output')

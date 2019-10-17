import komand
from .schema import RunInput, RunOutput
# Custom imports below


class Run(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='run',
                description='Run command',
                input=RunInput(),
                output=RunOutput())


    def construct(self, func):
        func += "\n\nreturn run(p)\n"
        func = '\t' + '\t'.join(func.splitlines(True))
        f = """
def python_custom_handler(p={}):
%s
""" % func

        self.logger.debug("%s", f)
        return f

    def run(self, params={}):
        """ Run action"""
        exec(self.construct(params['function']))

        result = python_custom_handler(params['input'])
        return result or {}

    def test(self, params={}):
        """Test action"""
        return {}

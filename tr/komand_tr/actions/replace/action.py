import komand

from .schema import ReplaceInput, ReplaceOutput


class Replace(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='replace',
                description='Runs a tr expression on a string input',
                input=ReplaceInput(),
                output=ReplaceOutput())

    def run(self, params={}):
        text = params.get('text')
        expression = params.get('expression')

        command = 'echo "{}" | tr {}'.format(text, expression)
        self.logger.info('Replace: Executing command: {}'.format(command))
        proc = komand.helper.exec_command(command)

        if proc['rcode'] == 0:
            result = proc['stdout'].decode('utf-8')
            result = result.rstrip()
            return {'result': result}
        else:
            self.logger.error(
                'KomandHelper: ExecCommand: Failed to execute: {}\n{}'.format(
                    command, proc['stderr'].decode('utf-8')
                )
            )
            raise Exception('Text processing failed:\n{}'.format(
                proc['stderr'].decode('utf-8')
            ))

    def test(self):
        return self.run(params={
            'text': 'Long    spaces    here', 'expression': '-s [:space:] ' ''
        })

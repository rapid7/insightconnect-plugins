import pexpect

import komand


class Cmd:
    def __init__(self, logger):
        self.logger = logger

    def call(self, command, password=None):
        """
        Calls a command. In case of any errors (exit code != 0) logs them and
        raises OSError. If password is given, waits for '[Pp]assword.*:' prompt
        and sends it to the command (the password is not logged).
        """
        self.logger.info('Call: Executing: {}'.format(command))

        try:
            if password:
                child = pexpect.spawn(command)
                child.delaybeforesend = None
                index = child.expect(
                    ['[Pp]assword.*: ', '.* done\.'], timeout=30
                )
                if index == 0:
                    child.sendline(password)
                    self.logger.info('Call: Password entered')
                stdout = stderr = child.read().decode()
                exit_code = child.wait()
                child.close()
                self.logger.info(stdout)
            else:
                proc = komand.helper.exec_command(command)
                exit_code = proc['rcode']
                stderr = proc['stderr'].decode()
                stdout = proc['stdout'].decode()
        except pexpect.exceptions.TIMEOUT:
            raise TimeoutError(
                'Timeout occurred for "{}". Please make sure that the Git '
                'repository is available and that the provided credentials '
                'are correct. If the issue persists, please contact Komand '
                'support'.format(command)
            )
        except Exception as e:
            self.logger.error('Call: Unexpected exception: {}'.format(str(e)))
            raise e

        if exit_code != 0:
            raise OSError(
                'Command execution failed: {}\nExit code: {}\n{}'.format(
                    command, exit_code, stderr
                )
            )

        self.logger.info('Call: Command executed successfully')
        return stdout.rstrip()

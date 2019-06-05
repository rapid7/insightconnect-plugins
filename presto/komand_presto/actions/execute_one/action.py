import komand
from .schema import ExecuteOneInput, ExecuteOneOutput
# Custom imports below
import socket
import signal
from pyhive import presto


class ExecuteOne(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='execute_one',
                description='Prepare and execute a database operation (query or command) and return only first row',
                input=ExecuteOneInput(),
                output=ExecuteOneOutput())

    def run(self, params={}):
        c = self.connection.cursor
        operation = params.get('operation')
        parameters = params.get('parameters', None)

        try:
            c.execute(operation)
            row = c.fetchone()

            self.logger.info('Returned row: %s' % (row,))

            if not row:
                row = []
            return {'row': row}

        except presto.DatabaseError as e:
            self.logger.error('There was an error with your SQL query: %s' % e[0]['failureInfo']['message'])
        except Exception as e:
            self.logger.error('An unknown error occurred: %s' % e)

    def test(self):
        host = self.connection.host
        port = self.connection.port

        try:
            socket.inet_aton(host) # Check if is correct ip address
        except socket.error: # DNS
            try:
                socket.gethostbyname(host)
            except socket.error:
                self.logger.error('Hostname %s cannot be resolved by DNS' % host)
                raise

        signal.signal(signal.SIGALRM,self.timeoutHandler)
        signal.alarm(self.connection.timeout)

        c = self.connection.cursor
        c.execute('select 1')

        return {'result': c.fetchone()[0]}

    def timeoutHandler(self, signum, frame):
        self.logger.error('Timeout exceeded (%is)' % self.connection.timeout)
        raise Exception('Timeout exceeded (%is)' % self.connection.timeout)

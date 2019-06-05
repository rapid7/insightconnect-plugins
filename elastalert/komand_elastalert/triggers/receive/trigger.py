import komand
import time
from .schema import ReceiveInput, ReceiveOutput
# Custom imports below
import base64
import json
import socket


class Receive(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='receive',
                description='Listen for and trigger on new alerts from an ElastAlert webhook',
                input=ReceiveInput(),
                output=ReceiveOutput())

    def handler_data(self, recv_data):
        # Parse headers
        try:
            headers, data = recv_data.split('\r\n\r\n')
            self.logger.debug('Data: %s', data)
            self.logger.debug('Headers: %s', headers)
            headers = headers.split('\n')
            req_method = headers[0].strip().split()
        except:
            self.logger.error('Bad HTTP request format')
            return False

        if not isinstance(req_method, list):
            self.logger.error('Unable to find HTTP method')
            return False

        # Validate JSON
        try:
            data_json = json.loads(data)
        except:
            self.logger.error('Unable to decode JSON')
            return False

        if req_method[0] == 'POST':
            # Search for Authorization header
            try:
                # Retrieve Authorization header
                for header in headers:
                    if header.startswith('Authorization: '):
                       auth_header = header
            except:
                self.logger.error('Missing Authorization header')
                return False

            # Retrieve Authorization's Basic value
            try:
                auth = auth_header.split()[2]
            except:
                self.logger.error('Authorization header is incomplete, expecting e.g.: Basic dGVzdAo=')
                return False

            # Retrieve user:pass from Basic Authorization value
            try:
                # There's an extra newline we must strip
                key = base64.b64decode(auth).decode().rstrip('\n')
                self.logger.debug('Client Key: %s', key)
            except:
                self.logger.error('Unable to base64 decode basic authorization value')
                return False

            # Verify Authorization key
            if key == self.connection.auth_key:
              if isinstance(data_json, dict) and len(data_json) > 0:
                  self.send({'alert': data_json})
              else:
                  self.logger.info('No data in message')
                  return False
            else:
                self.logger.debug('Server Key: %s', self.connection.auth_key)
                self.logger.info('Authorization key did not match')
                return False
        else:
            self.logger.info('Not a POST Request')
            time.sleep(2)
            return False
        return False

    def run(self, params={}):
        """Run the trigger"""
        # Send a test event

        BUFF = 4096
        interval = params.get('interval')
        endpoint = params.get('endpoint', '0.0.0.0')
        tcp_port = params.get('tcp_port')

        host = endpoint + ":" + str(tcp_port)
        self.logger.info('Listening on %s', host)

        # Open socket server to listen for messages
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((endpoint, tcp_port))
        # System default backlog for sanity
        server.listen(5)

        while True:
          conn, addr = server.accept()
          recv_data = conn.recv(BUFF)
          conn.send(recv_data)
          conn.close()

          # Handler receiving data
          self.handler_data(recv_data.decode())
          time.sleep(interval)

    def test(self):
        """TODO: Test the trigger"""
        return {}

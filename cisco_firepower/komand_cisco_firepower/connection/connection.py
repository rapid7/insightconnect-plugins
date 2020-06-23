import komand
from .schema import ConnectionSchema
# Custom imports below
import base64
import re
import socket
import ssl
import struct
import select
import time
import OpenSSL.crypto as crypto
from ..util.message_details import MessageDetails
from ..util.message_details import MessageType
from ..util.utils import first
from komand.exceptions import PluginException


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    ONE_UINT = b'!I'
    TWO_UINT = b'!II'

    def connect(self, params={}):
        self.__p12 = params.get('certificate')
        self.__p12_pwd = params.get('certificate_passphrase').get('secretKey')
        self.__cert_file = 'cert.pem'
        self.host = params.get('server')
        self.__port = params.get('port')

        self.logger.info("Connect: Connecting..")
        self.__generate_certificate()
        self.make_connection()
        self.logger.info("Connect: Connected successfully.")

    def make_connection(self):
        self.sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        ctx.load_cert_chain(self.__cert_file)
        self.__connection = ctx.wrap_socket(self.sockt)
        self.__connection.connect((self.host, self.__port))
        self.max_data_size = self.__get_max_data_size()

    def send(self, data_array, timeout=300):
        self.logger.info("Connect: Sending data through socket...")
        error_count = 0
        total_commands = 0

        for data in data_array:
            self.logger.info("Connect: Sending new data set.")
            message_type = MessageType.DATA_PAYLOAD_LENGTH
            msg_details = MessageDetails(message_type, len(data), data)
            response = self.__send_data(msg_details, timeout)
            if response:
                error, commands = self.__parse_response(response)
            else:
                error = 0
                commands = 0
            total_commands += commands
            if error:
                error_count += 1
                self.logger.error("Error in response: {}".format(response))
            self.logger.info("{} commands sent in this data set.".format(commands))

        self.logger.info("{} commands sent in total.".format(total_commands))
        if error_count:
            self.logger.info("{} batches contained error(s).".format(error_count))
        return total_commands, error_count

    def read(self, timeout=300):
        self.logger.info("Connect: Reading from socket...")
        msg_details = self.__get_message_details(timeout)
        data = None
        if msg_details.data or msg_details.msg_length or msg_details.msg_type:
            data = self.__connection.recv(msg_details.msg_length)
            data = data.decode('UTF-8')
        return data

    def test_connection(self):
        if self.__connection._closed:
            raise Exception('Not connected.')
        return {}

    def close(self):
        self.__connection.close()
        self.sockt.close()

    def __send_data(self, msg_details, timeout=300):
        # Send the data type and size
        data_struct = struct.pack(
            self.TWO_UINT, msg_details.msg_type, msg_details.msg_length
        )
        self.__connection.write(data_struct)
        self.logger.debug(
            "Sending {} bytes to socket".format(msg_details.msg_length)
        )
        self.__connection.send(msg_details.data.encode())
        self.logger.debug("Data sent.")
        response = self.read(timeout)
        return response

    def __get_max_data_size(self):
        self.logger.info("Connect: Getting max write size")
        # Request max data size
        data_request = MessageType.DATA_REQUEST
        max_data = MessageType.MAX_DATA
        self.__connection.write(struct.pack(self.TWO_UINT, data_request, 4))
        self.__connection.write(struct.pack(self.ONE_UINT, max_data))

        msg_details = self.__get_message_details()
        data = self.__connection.recv(msg_details.msg_length)

        if not msg_details.is_data_size_message():
            self.logger.error("Message does not include the max data size.")
            raise Exception(str(data))

        data = first(struct.unpack(self.ONE_UINT, data))
        self.logger.debug("Max data size is {}".format(data))
        return data

    def __get_message_details(self, timeout=300):
        # This will block for timeout time or return as soon as the socket is ready to be read
        r, _, _ = select.select([self.__connection], [], [], timeout)
        if not r:
            raise PluginException(cause="Communication timeout with Firepower server.",
                                  assistance="Set the number of records processed at one time to a lower number and try again.")

        data = self.__connection.recv()

        msg_type = self.__custom_unpack(data[0:4], self.ONE_UINT)
        msg_type = first(msg_type)
        msg_value = self.__custom_unpack(data[4:8], self.ONE_UINT)
        msg_value = first(msg_value)

        self.logger.debug(
            "Got message details for type {}, and size {}"
                .format(msg_type, msg_value)
        )
        return MessageDetails(msg_type, msg_value)

    def __generate_certificate(self):
        self.logger.debug('Connect: Generating pem certificate.')
        self.__p12 = base64.b64decode(self.__p12)
        self.__p12 = crypto.load_pkcs12(self.__p12, self.__p12_pwd)
        file_type = crypto.FILETYPE_PEM
        cert = crypto.dump_certificate(file_type, self.__p12.get_certificate())
        key = crypto.dump_privatekey(file_type, self.__p12.get_privatekey())

        with open(self.__cert_file, 'wb') as f:
            for certificate in (cert, key):
                f.write(certificate)

    @staticmethod
    def __parse_response(response):
        commands_processed_message = "Done processing (\d+) commands."
        regex = re.compile(commands_processed_message)
        error = not regex.match(response)
        commands = regex.search(response)
        return error, int(''.join(re.findall('\d+', commands.group())))

    @staticmethod
    def __custom_unpack(data, fmt):
        if data or len(data):
            return struct.unpack(fmt, data)
        return data

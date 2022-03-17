import base64
import re
import socket
import ssl
import struct
from OpenSSL import crypto
from ..util.message_details import MessageDetails
from ..util.message_details import MessageType
from ..util.utils import first
from insightconnect_plugin_runtime.exceptions import PluginException
from urllib.parse import urlsplit


class CiscoFirePowerHostInput:
    def __init__(
        self,
        certificate: str,
        passphrase: str,
        server: str,
        port: int,
        logger,
    ):
        self.__p12 = certificate
        self.__p12_pwd = passphrase
        self.__cert_file = "cert.pem"
        self.__host = urlsplit(server.strip()).netloc
        self.__port = port
        self.logger = logger

        self.__generate_certificate()
        sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        ctx.load_cert_chain(self.__cert_file)
        self.__connection = ctx.wrap_socket(sockt)
        self.__connection.connect((self.__host, self.__port))
        self.max_data_size = self.__get_max_data_size()

    ONE_UINT = b"!I"
    TWO_UINT = b"!II"

    def send(self, data_array):
        self.logger.info("Connect: Sending data through socket...")
        error_count = 0
        total_commands = 0

        for data in data_array:
            self.logger.info("Connect: Sending new data set.")
            message_type = MessageType.DATA_PAYLOAD_LENGTH
            msg_details = MessageDetails(message_type, len(data), data)
            response = self.__send_data(msg_details)
            error, commands = self.__parse_response(response)
            total_commands += commands
            if error:
                error_count += 1
                self.logger.error(f"Error in response: {response}")
            self.logger.info(f"{commands} commands sent in this data set.")

        self.logger.info(f"{total_commands} commands sent in total.")
        if error_count:
            self.logger.info(f"{error_count} batches contained error(s).")
        return total_commands, error_count

    def read(self):
        self.logger.info("Connect: Reading from socket...")
        msg_details = self.__get_message_details()
        data = self.__connection.recv(msg_details.msg_length)
        data = data.decode("UTF-8")
        return data

    def close(self):
        self.__connection.close()

    def __send_data(self, msg_details):
        # Send the data type and size
        data_struct = struct.pack(self.TWO_UINT, msg_details.msg_type, msg_details.msg_length)
        self.__connection.write(data_struct)
        self.logger.debug(f"Sending {msg_details.msg_length} bytes to socket.")
        self.__connection.send(msg_details.data.encode())
        self.logger.debug("Data sent.")
        response = self.read()
        return response

    def __get_max_data_size(self):
        self.logger.info("Connect: Getting max write size.")
        data_request = MessageType.DATA_REQUEST
        max_data_size = MessageType.MAX_DATA
        self.__connection.write(struct.pack(self.TWO_UINT, data_request, 4))
        self.__connection.write(struct.pack(self.ONE_UINT, max_data_size))

        msg_details = self.__get_message_details()
        data = self.__connection.recv(msg_details.msg_length)

        if msg_details.is_data_size_message():
            data = first(struct.unpack(self.ONE_UINT, data))
            self.logger.debug(f"Max data size is {data}.")
            return data

        self.logger.error("Message does not include the max data size.")
        raise PluginException(
            cause="Message does not include the max data size.",
            assistance="Check the logs and if the issue persists please contact support.",
            data=str(data),
        )

    def __get_message_details(self):
        data = self.__connection.recv()

        msg_type = first(self.__custom_unpack(data[0:4], self.ONE_UINT))
        msg_value = first(self.__custom_unpack(data[4:8], self.ONE_UINT))

        self.logger.debug(f"Got message details for type {msg_type}, and size {msg_value}.")
        return MessageDetails(msg_type, msg_value)

    def __generate_certificate(self):
        self.logger.debug("Connect: Generating pem certificate.")
        self.__p12 = base64.b64decode(self.__p12)
        self.__p12 = crypto.load_pkcs12(self.__p12, self.__p12_pwd)
        file_type = crypto.FILETYPE_PEM
        cert = crypto.dump_certificate(file_type, self.__p12.get_certificate())
        key = crypto.dump_privatekey(file_type, self.__p12.get_privatekey())

        with open(self.__cert_file, "wb") as f:
            for certificate in (cert, key):
                f.write(certificate)

    @staticmethod
    def __parse_response(response):
        regex = re.compile("Done processing (\d+) commands.")
        error = not regex.match(response)
        commands = regex.search(response)
        return error, int("".join(re.findall("\d+", commands.group())))

    @staticmethod
    def __custom_unpack(data, fmt):
        if data or len(data):
            return struct.unpack(fmt, data)
        return data

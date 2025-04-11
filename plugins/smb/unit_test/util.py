import json
import logging
import os.path
import sys

sys.path.append(os.path.abspath("../"))
from komand_smb.connection import Connection


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            "host": "11.11.11.11",
            "port": 8080,
            "credentials": {"username": "thisisusername", "password": "thisispassword"},
            "domain": "SMB-DOMAIN-TEST",
            "netbios_name": "smb-domain-test",
            "use_ntlmv2": True,
            "timeout": 60,
        }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def load_json(filename):
        with open((os.path.join(os.path.dirname(os.path.realpath(__file__)), filename))) as file:
            return json.loads(file.read())


class MockSMBSession:
    def __init__(self):
        pass

    @staticmethod
    def getAttributes(*args, **kwargs):
        return SharedFileObject(
            alloc_size=4096,
            create_time=1643738944.6904666,
            file_attribute=32,
            file_id=None,
            file_size=800,
            filename="generator.bat",
            isDirectory=False,
            isNormal=False,
            isReadOnly=False,
            last_access_time=1643839839.8947108,
            last_attr_change_time=1643839839.8947108,
            last_write_time=1643839839.8947108,
            short_name="generator.bat",
        )

    @staticmethod
    def listPath(*args, **kwargs):
        return [
            ListPathObject(
                alloc_size=4096,
                create_time=1643738944.6904666,
                file_attributes=32,
                file_id=None,
                file_size=800,
                filename="generator.bat",
                isDirectory=False,
                isNormal=False,
                isReadOnly=False,
                last_access_time=1643839839.8947108,
                last_attr_change_time=1643839839.8947108,
                last_write_time=1643839839.8947108,
                short_name="GENERA~1.BAT",
            )
        ]

    @staticmethod
    def listShares(*args, **kwargs):
        return [
            ListSharesObject(
                COMM_DEVICE=2,
                DISK_TREE=0,
                IPC=3,
                PRINT_QUEUE=1,
                comments="Remote Admin",
                isSpecial=True,
                isTemporary=False,
                name="ADMIN$",
                type=0,
            ),
            ListSharesObject(
                COMM_DEVICE=2,
                DISK_TREE=0,
                IPC=3,
                PRINT_QUEUE=1,
                comments="Default Share",
                isSpecial=True,
                isTemporary=False,
                name="C$",
                type=0,
            ),
        ]

    @staticmethod
    # unused params inherited from `download_file_input.json.exp`
    def retrieveFile(service_name, path, file_obj, *args, **kwargs):
        file_obj.write(
            b"this is a new log 1\r\nthis is a new log 2\r\nthis is a new log 3\r\nthis is a new log 4\r\n\r\n"
        )


class SharedFileObject:
    def __init__(
        self,
        alloc_size: int,
        create_time: float,
        file_attribute: int,
        file_id: None,
        file_size: int,
        filename: str,
        isDirectory: bool,
        isNormal: bool,
        isReadOnly: bool,
        last_access_time: float,
        last_attr_change_time: float,
        last_write_time: float,
        short_name: str,
    ):
        self.alloc_size = alloc_size
        self.create_time = create_time
        self.file_attribute = file_attribute
        self.file_id = file_id
        self.file_size = file_size
        self.filename = filename
        self.isDirectory = isDirectory
        self.isNormal = isNormal
        self.isReadOnly = isReadOnly
        self.last_access_time = last_access_time
        self.last_attr_change_time = last_attr_change_time
        self.last_write_time = last_write_time
        self.short_name = short_name


class ListPathObject:
    def __init__(
        self,
        alloc_size: int,
        create_time: float,
        file_attributes: int,
        file_id: None,
        file_size: int,
        filename: str,
        isDirectory: bool,
        isNormal: bool,
        isReadOnly: bool,
        last_access_time: float,
        last_attr_change_time: float,
        last_write_time: float,
        short_name: str,
    ):
        self.alloc_size = alloc_size
        self.create_time = create_time
        self.file_attributes = file_attributes
        self.file_id = file_id
        self.file_size = file_size
        self.filename = filename
        self.isDirectory = isDirectory
        self.isNormal = isNormal
        self.isReadOnly = isReadOnly
        self.last_access_time = last_access_time
        self.last_attr_change_time = last_attr_change_time
        self.last_write_time = last_write_time
        self.short_name = short_name


class ListSharesObject:
    def __init__(
        self,
        COMM_DEVICE: int,
        DISK_TREE: int,
        IPC: int,
        PRINT_QUEUE: int,
        comments: str,
        isSpecial: bool,
        isTemporary: bool,
        name: str,
        type: int,
    ):
        self.COMM_DEVICE = COMM_DEVICE
        self.DISK_TREE = DISK_TREE
        self.IPC = IPC
        self.PRINT_QUEUE = PRINT_QUEUE
        self.comments = comments
        self.isSpecial = isSpecial
        self.isTemporary = isTemporary
        self.name = name
        self.type = type

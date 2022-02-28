class MessageType(object):
    MAX_DATA = 1
    DATA_REQUEST = 2
    DATA_PAYLOAD_LENGTH = 3


class MessageDetails(object):
    def __init__(self, msg_type, msg_length, data=None):
        self.msg_type = msg_type
        self.msg_length = msg_length
        self.data = data

    def is_data_size_message(self):
        return self.msg_type == MessageType.MAX_DATA

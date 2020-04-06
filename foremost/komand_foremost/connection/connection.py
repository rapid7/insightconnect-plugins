import komand
from .schema import ConnectionSchema
from komand.exceptions import ConnectionTestException


# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        pass

    def test(self):
        cmd = '/usr/bin/foremost'
        r = komand.helper.exec_command(cmd)
        if r['rcode'] != 0:
            raise ConnectionTestException(cause="Command error",
                                          assistance='Foremost returned with non-zero status')
        return {}

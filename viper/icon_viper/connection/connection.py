import komand
from .schema import ConnectionSchema, Input
from ..util import base
from ..util import config


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.config = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.config = config.Config(params.get(Input.URL), params.get(Input.TOKEN)['secretKey'])

    def test(self):
        response = base.ViperBase(self.config).is_active(self.config)
        if response:
            return {'Connection test successful': True}

        return {'Connection test unsuccessful': False}

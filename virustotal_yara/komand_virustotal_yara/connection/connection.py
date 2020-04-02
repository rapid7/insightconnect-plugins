import komand
from .schema import ConnectionSchema
# Custom imports below
import yara


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        # Checks to make sure Yara loads
        try:
            version = yara.YARA_VERSION
        except ImportError:
            raise ImportError("Error occurred trying to import Yara")
        return {"results": [{"success": True}]}



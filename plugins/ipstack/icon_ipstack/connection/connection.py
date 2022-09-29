import insightconnect_plugin_runtime
<<<<<<< HEAD
from .schema import ConnectionSchema
=======
from .schema import ConnectionSchema, Input
>>>>>>> 09d942e46 (Changed thing to true (#1438))

# Custom imports below


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.token = None

    def connect(self, params):
        self.token = params.get(Input.CRED_TOKEN).get("secretKey")

    def test(self):
        return {"success": True}


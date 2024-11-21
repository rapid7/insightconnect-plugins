import insightconnect_plugin_runtime
from .schema import DeleteInput, DeleteOutput

# Custom imports below


class Delete(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete", description="Delete", input=DeleteInput(), output=DeleteOutput()
        )

    def run(self, params={}):
        """Run action"""
        count = self.connection.redis.delete(params["key"])
        return {"count": count}

    def test(self):
        """Test action"""
        return {}

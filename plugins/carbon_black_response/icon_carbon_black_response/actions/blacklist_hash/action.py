import insightconnect_plugin_runtime
from .schema import BlacklistHashInput, BlacklistHashOutput

# Custom imports below
from cbapi.response.models import BannedHash


class BlacklistHash(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="blacklist_hash",
            description="Ban a hash given its MD5",
            input=BlacklistHashInput(),
            output=BlacklistHashOutput(),
        )

    def run(self, params={}):
        md5 = params.get("md5_hash")

        try:
            banned_hash = self.connection.carbon_black.create(BannedHash)
            banned_hash.md5hash = md5
            banned_hash.text = "Banned by Komand"
            banned_hash.enabled = True
            banned_hash.save()

            return {"success": True}
        except Exception as ex:
            self.logger.error("Failed to blacklist hash %s", ex)
            raise ex

    def test(self):
        if self.connection.test():
            return {}

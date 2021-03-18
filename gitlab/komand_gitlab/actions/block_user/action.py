import komand
from .schema import BlockUserInput, BlockUserOutput

# Custom imports below
import requests


class BlockUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="block_user",
            description="Block Gitlab user",
            input=BlockUserInput(),
            output=BlockUserOutput(),
        )

    def run(self, params={}):
        r_url = "%s/users/%s/block" % (self.connection.url, params.get("id"))

        try:
            r = requests.post(r_url, headers={"PRIVATE-TOKEN": self.connection.token}, verify=False)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            self.logger.error(e)
            raise Exception(e)

        return {"status": r.ok}

    def test(self):
        """TODO: Test action"""
        return {}

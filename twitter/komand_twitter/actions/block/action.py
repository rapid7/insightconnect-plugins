import komand
from .schema import BlockInput, BlockOutput
# Custom imports below


class Block(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='block',
                description='Block user',
                input=BlockInput(), 
                output=BlockOutput())

    def run(self, params={}):

        screen_name = params.get("user")
        self.logger.info("Run: Got screen name: {screen_name}".format(screen_name=screen_name))

        if len(screen_name) == 0:
            assert "Run: Tweet length was 0. Make sure property 'user' is marked required."
            return {'blocked': False}

        # Grab users that have been blocked, then check if the user to block has already been blocked.
        blocked_users = self.connection.client.GetBlocks(skip_status=False)
        for blocked_user in blocked_users:
            if blocked_user.screen_name == screen_name:
                return {'blocked': True}

        blocked_user = self.connection.client.CreateBlock(screen_name=screen_name)

        # Return False if no object was returned - we can't be certain the block was successful.
        if not blocked_user:
            raise Exception("No object returned from Twitter. Uncertain of block success. ")

        return {'blocked': True}

    def test(self, params={}):
        """TODO: Test action"""
        return {} 

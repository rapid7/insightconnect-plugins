import komand
from .schema import DestroyInput, DestroyOutput
# Custom imports below


class Destroy(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='destroy',
                description='Destroy direct message',
                input=DestroyInput(),
                output=DestroyOutput())

    def run(self, params={}):

        # Step 1: Acquire target
        message_id = params.get("message_id")

        # Step 2: Fire teh lazers!
        try:
          destroyed_dm = self.connection.client.DestroyDirectMessage(int(message_id))
          if destroyed_dm is not None:
              # Step 3: Report back with casualties
              return {'destroyed': True}
        except:
            self.logger.error("Direct message %s doesn't exist, it may not have been destroyed by us.", message_id)
            return {'destroyed': False}
            # Step 3b: False target was acquired. No enemy casualties.
        # Step 3c: Fall back.
        self.logger.error('Something weird happened, message %s not destroyed', message_id)
        return {'destroyed': False}

    def test(self):
        """TODO: Test action"""
        return {}

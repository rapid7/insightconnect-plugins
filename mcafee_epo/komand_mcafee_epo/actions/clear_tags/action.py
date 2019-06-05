import komand
from .schema import ClearTagsInput, ClearTagsOutput
# Custom imports below


class ClearTags(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='clear_tags',
                description='Clears the given tag to a supplied list of systems',
                input=ClearTagsInput(),
                output=ClearTagsOutput())

    def run(self, params={}):
        try:
            mc = self.connection.client
            for d in params['devices']:
                mc.run('system.clearTag', d, params['tag'])
            self.logger.info("Tag cleared from {} devices".format(len(params['devices'])))
            return {"message": "Tags cleared from devices successfully"}
        except Exception as e:
            self.logger.error("Tags could not be cleared from some or all devices. Error: " + str(e))
            raise

    def test(self):
        try:
            mc = self.connection.client
            if mc.epo.getVersion():
                return {"message": "test passed"}
        except Exception:
            self.logger.error("An unexpected error occurred during the API request")
            raise

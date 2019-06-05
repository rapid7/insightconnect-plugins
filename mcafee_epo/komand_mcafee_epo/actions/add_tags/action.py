import komand
from .schema import AddTagsInput, AddTagsOutput
# Custom imports below

class AddTags(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_tags',
                description='Assigns the given tag to a supplied list of systems',
                input=AddTagsInput(),
                output=AddTagsOutput())

    def run(self, params={}):
        try:
            mc = self.connection.client
            for d in params['devices']:
                mc.run('system.applyTag', d, params['tag'])
            self.logger.info("Applied to {} devices".format(len(params['devices'])))
            return {"message": "Tags applied to devices successfully"}
        except Exception as e:
            self.logger.error("Tags could not be added to some or all devices. Error: " + str(e))
            raise

    def test(self):
        try:
            mc = self.connection.client
            if mc.epo.getVersion():
                return {"message": "test passed"}
        except Exception:
            self.logger.error("An unexpected error occurred during the API request")
            raise

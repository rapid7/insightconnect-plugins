import komand
from .schema import SystemInfoInput, SystemInfoOutput
# Custom imports below


class SystemInfo(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='system_info',
                description='List system information',
                input=SystemInfoInput(),
                output=SystemInfoOutput())

    def run(self, params={}):
        try:
            cleaned_response = []
            mc = self.connection.client
            response = mc.run('system.find', params['query'])
            self.logger.info("System information has been gathered")
            # Loop through response
            for prop in response:
                # Call clean_dict to clear null values
                cleaned_prop = komand.helper.clean_dict(prop)
                # Added cleaned response to new list
                cleaned_response.append(cleaned_prop)
            # return the cleaned list
            return {"properties": cleaned_response}
        except Exception:
            self.logger.error("Unable to query for system information")
            raise

    def test(self):
        try:
            mc = self.connection.client
            if mc.epo.getVersion():
                return {"properties": [{'test': 'passed'}]}
        except Exception:
            self.logger.error("An unexpected error occurred during the API request")
            raise

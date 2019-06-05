import komand
from .schema import StopAndQuarantineFileInput, StopAndQuarantineFileOutput
# Custom imports below


class StopAndQuarantineFile(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='stop_and_quarantine_file',
                description='Stop execution of a file on a machine and delete it',
                input=StopAndQuarantineFileInput(),
                output=StopAndQuarantineFileOutput())

    def run(self, params={}):
        self.logger.info("Running...")

        machine_id = params.get("machine_id")
        sha1_id = params.get("sha1")
        comment = params.get("comment")

        self.logger.info("Attempting to stop and quarantine file: " + sha1_id)
        self.logger.info("Attempting to stop and quarantine file on machine: " + machine_id)
        response = self.connection.stop_and_quarantine_file(machine_id, sha1_id, comment)
        return {"stop_and_quarantine_response": komand.helper.clean(response)}

    # def test(self):
    #     # TODO: Implement test function
    #     return {}

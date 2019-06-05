import komand
from .schema import LastStatusInput, LastStatusOutput
# Custom imports below


class LastStatus(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='last_status',
                description='Check if the indexation went well',
                input=LastStatusInput(),
                output=LastStatusOutput())

    def run(self, params={}):
        last_statuses = self.connection.api.last_status()
        return {'last_statuses': last_statuses}

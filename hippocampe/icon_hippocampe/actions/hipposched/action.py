import komand
from .schema import HipposchedInput, HipposchedOutput
# Custom imports below


class Hipposched(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='hipposched',
                description='Schedule the launch of shadowbook (for automatic indexation)',
                input=HipposchedInput(),
                output=HipposchedOutput())

    def run(self, params={}):
        time = params.get('time')
        schedule = self.connection.api.hipposched(time)
        return schedule

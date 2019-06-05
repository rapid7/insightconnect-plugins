import komand
from .schema import SubmitEventInput, SubmitEventOutput
# Custom imports below
from komand_sentry.util.events import submit_event


class SubmitEvent(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='submit_event',
                description='Submit a Sentry event',
                input=SubmitEventInput(),
                output=SubmitEventOutput())

    def run(self, params={}):
        dsn = params.get('dsn')
        event_json = params.get('event_json')
        sentry_version = params.get('sentry_version', 7)

        event_id = submit_event(self.logger, event_json, dsn, sentry_version)

        return {'id': event_id}

    def test(self):
        return {'id': '612555152'}

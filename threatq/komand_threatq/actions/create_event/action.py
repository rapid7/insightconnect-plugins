import komand 
from .schema import CreateEventInput, CreateEventOutput
# Custom imports below
from threatqsdk import Event
from threatqsdk import exceptions


class CreateEvent(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_event',
                description='Create a new event',
                input=CreateEventInput(),
                output=CreateEventOutput())

    def run(self, params={}):
        """run creates a new event in Threat Quotient"""
        try:
            event = Event(self.connection.threatq)
            event.set_title(params['title'])
            event.set_desc(params['description'])
            event.set_type(params['type'])
            event.set_date(self.connection.threatq.now())
            eid = event.upload(sources=params['source'])
            return { "id": eid }
        except exceptions.UploadFailedError as ufe:
            err = 'ThreatQ SDK: UploadFailedError: reason %s' % ufe.message
            self.logger.error(err)
        raise Exception('ThreatQ SDK call failed')

    def test(self):
        """TODO: Test action"""
        if self.connection.threatq:
            return {}

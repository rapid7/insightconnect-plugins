import komand
from .schema import CreateIndicatorInput, CreateIndicatorOutput
# Custom imports below
from threatqsdk import exceptions
from threatqsdk import Indicator
from threatqsdk import Source


class CreateIndicator(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_indicator',
                description='Create a new indicator',
                input=CreateIndicatorInput(),
                output=CreateIndicatorOutput())

    def run(self, params={}):
        """run creates a new indicator in Threat Quotient"""
        try:
            ind = Indicator(self.connection.threatq)
            ind.set_value(params['value'])
            ind.set_type(params['type'])
            ind.set_status(params['status'])

            # Upload the indicator and receive new indicator id
            iid = ind.upload(sources=Source(params['source']))
            return { "id": iid }
        except exceptions.UploadFailedError as ufe:
            err = 'ThreatQ SDK: UploadFailedError: reason %s' % ufe.message
            self.logger.error(err)
        raise Exception('ThreatQ SDK call failed')

    def test(self):
        """TODO: Test action"""
        if self.connection.threatq:
            return {}

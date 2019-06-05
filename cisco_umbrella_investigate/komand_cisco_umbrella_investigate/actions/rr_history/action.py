import komand
from .schema import RrHistoryInput, RrHistoryOutput
# Custom imports below


class RrHistory(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='rr_history',
                description='Return the history that Umbrella has seen for a given domain',
                input=RrHistoryInput(),
                output=RrHistoryOutput())

    def run(self, params={}):
        domain = params.get('domain')
        type = params.get('type')

        try:
            if not type:
                rr_history = self.connection.investigate.rr_history(domain)
            else:
                rr_history = self.connection.investigate.rr_history(domain, type)
        except Exception as e:
            self.logger.error("RrHistoryIp: Run: Problem with request")
            raise e

        return {"features": [rr_history.get("features")], "rrs_tf": rr_history.get("rrs_tf")}

    def test(self):
        return {"features": [], "rrs_tf": []}

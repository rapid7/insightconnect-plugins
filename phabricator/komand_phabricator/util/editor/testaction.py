
class TestAction:

    def checkPhabIsEmpty(self, phab):
        if not phab:
            raise Exception('CheckPhabIsEmpty: Empty Phabricator object')

    def wrongHealthCheck(self, phab):
        try:
            phab.conduit.ping()
        except Exception as e:
            raise Exception('HealthCheck: Health check - some problem with connection')

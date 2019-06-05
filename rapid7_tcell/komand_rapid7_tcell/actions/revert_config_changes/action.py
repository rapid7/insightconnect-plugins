import komand
from .schema import RevertConfigChangesInput, RevertConfigChangesOutput
# Custom imports below


class RevertConfigChanges(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='revert_config_changes',
                description='Revert configuration from the previous iteration',
                input=RevertConfigChangesInput(),
                output=RevertConfigChangesOutput())

    def run(self, params={}):
        app_id = params.get('app_id')
        id_ = params.get('id')
        success = self.connection.api.revert_config_changes(app_id, id_)
        return {'success': success}

    def test(self):
        return {}

import komand
from .schema import DeleteTargetInput, DeleteTargetOutput
# Custom imports below
from openvas_lib.common import ClientError
import sys


class DeleteTarget(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_target',
                description='Delete specified target ID in the OpenVAS server',
                input=DeleteTargetInput(),
                output=DeleteTargetOutput())

    def run(self, params={}):
        target_id = str(params.get('target_id'))
        try:
            self.connection.scanner.delete_target(target_id)
        except ClientError:
            return{'success': False, 'message': 'Target to delete not found using supplied target ID'}
        except:
            return{'success': False, 'message': ' | '.join([str(sys.exc_info()[0]), str(sys.exc_info()[1])])}
        return {'success': True, 'message': 'Scan successfully deleted'}

    def test(self):
        # TODO: Implement test function
        return {}

import komand
from .schema import GetPolicyInput, GetPolicyOutput
# Custom imports below


class GetPolicy(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_policy',
                description='Get policy',
                input=GetPolicyInput(),
                output=GetPolicyOutput())

    def run(self, params={}):
        policy = self.connection.client.policies.get(params.get('policy_id', ''))
        return {'policy': policy}

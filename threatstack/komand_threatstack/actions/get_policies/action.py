import komand
from .schema import GetPoliciesInput, GetPoliciesOutput
# Custom imports below


class GetPolicies(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_policies',
                description='Get policies',
                input=GetPoliciesInput(),
                output=GetPoliciesOutput())

    def run(self, params={}):
        policies = self.connection.client.policies.list(**params)
        policy_list = []

        while True:
            try:
                policy = next(policies)
                policy_list.append(policy)
            except TypeError:
                # Nothing found.
                # Not necessarily an error; could be failed search.
                break
            except StopIteration:
                break

        return {'policies': policy_list, 'count': len(policy_list)}

    def test(self):
        '''Test action'''
        return self.run()

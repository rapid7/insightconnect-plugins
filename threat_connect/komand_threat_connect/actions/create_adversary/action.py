import komand
from .schema import CreateAdversaryInput, CreateAdversaryOutput
# Custom imports below


class CreateAdversary(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_adversary',
                description='Create Threatconnect Adversary',
                input=CreateAdversaryInput(),
                output=CreateAdversaryOutput())

    def run(self, params={}):
        adversaries = self.connection.threat_connect.adversaries()

        # name, owner required
        adversary = adversaries.add(params.get('name'), params.get('owner'))

        if params.get('attributes'):
            a_vals = [list(v.values())[0] for v in params.get('attributes')]
            a_keys = [list(k.keys())[0] for k in params.get('attributes')]
            for i in range(len(a_keys)):
                adversary.add_attribute(a_keys[i], a_vals[i])

        if params.get('tags'):
            result_tags = [tag.strip() for tag in params.get('tags').split(',')]
            for r_tag in result_tags:
                adversary.add_tag(r_tag)

        if params.get('security_label'):
            adversary.set_security_label(params.get('security_label'))

        try:
            a = adversary.commit()
            return {'id': a.id}
        except RuntimeError as e:
            self.logger.error('Error: {0}'.format(e))
            raise e

    def test(self):
        owners = self.connection.threat_connect.owners()
        owner = ""
        try:
            owners.retrieve()
        except RuntimeError as e:
            raise e

        for owner in owners:
            owner = owner.name
        return {'Owner Name': owner}
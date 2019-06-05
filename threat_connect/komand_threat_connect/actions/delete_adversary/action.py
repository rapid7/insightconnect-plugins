import komand
from .schema import DeleteAdversaryInput, DeleteAdversaryOutput
# Custom imports below


class DeleteAdversary(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_adversary',
                description='Delete an Adversary in the ThreatConnect platform',
                input=DeleteAdversaryInput(),
                output=DeleteAdversaryOutput())

    def run(self, params={}):
        adversaries = self.connection.threat_connect.adversaries()
        adversary = adversaries.add('', params.get('owner'))
        adversary.set_id(params.get('id'))

        try:
            adversary.delete()
            return {"status": True}
        except RuntimeError:
            return {"status": False}

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

import komand
from .schema import VictimsRetrieveInput, VictimsRetrieveOutput
# Custom imports below


class VictimsRetrieve(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='victims_retrieve',
                description='Retrieve ThreatConnect Victims',
                input=VictimsRetrieveInput(),
                output=VictimsRetrieveOutput())

    def run(self, params={}):
        victims = self.connection.threat_connect.victims()
        victim_obj_list = []

        filter1 = victims.add_filter()

        filter1.add_owner(params.get('owner'))

        if params.get('adversary_id'):
            filter1.add_adversary_id(params.get('adversary_id'))

        if params.get('email_id'):
            filter1.add_email_id(params.get('email_id'))

        if params.get('document_id'):
            filter1.add_document_id(params.get('document_id'))

        if params.get('id'):
            filter1.add_id(params.get('id'))

        if params.get('incident_id'):
            filter1.add_incident_id(params.get('incident_id'))

        if params.get('indicator'):
            filter1.add_indicator(params.get('indicator'))

        if params.get('security_label'):
            filter1.add_security_label(params.get('security_label'))

        if params.get('signature_id'):
            filter1.add_signature_id(params.get('signature_id'))

        if params.get('threat_id'):
            filter1.add_threat_id(params.get('threat_id'))

        if params.get('tag'):
            filter1.add_tag(params.get('tag'))

        if params.get('victim_id'):
            filter1.add_victim_id(params.get('victim_id'))

        try:
            victims.retrieve()
        except RuntimeError as e:
            raise e

        for victim in victims:
            victim_obj = {
                'id': victim.id,
                'name': victim.name,
                'nationality': (victim.nationality or ""),
                'org': (victim.org or ""),
                'suborg': (victim.suborg or ""),
                'work_location': (victim.work_location or ""),
                'weblink': victim.weblink
            }
            victim_obj_list.append(victim_obj)

        return {'victims': victim_obj_list}

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
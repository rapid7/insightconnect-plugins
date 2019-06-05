import komand
from .schema import ThreatsRetrieveInput, ThreatsRetrieveOutput
# Custom imports below
import datetime


class ThreatsRetrieve(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='threats_retrieve',
                description='Retrieve ThreatConnect Threats',
                input=ThreatsRetrieveInput(),
                output=ThreatsRetrieveOutput())

    def run(self, params={}):
        threat_obj_list = []
        threats = self.connection.threat_connect.threats()

        filter1 = threats.add_filter()

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
            filter1 = threats.add_filter()
            # filter1.add_id(params.get('id'))
        except AttributeError as e:
            raise e

        try:
            threats.retrieve()
        except RuntimeError as e:
            raise e

        for threat in threats:
            threat_obj = {
                'id': (threat.id or -1),
                'name': (threat.name or ""),
                'date_added': (datetime.datetime.strptime(threat.date_added, '%Y-%d-%mT%H:%M:%SZ').isoformat() or ""),
                'weblink': (threat.weblink or "")
            }
            threat_obj_list.append(threat_obj)

        return {'threats': threat_obj_list}

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
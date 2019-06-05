import komand
from .schema import IncidentsRetrieveInput, IncidentsRetrieveOutput
# Custom imports below
import datetime


class IncidentsRetrieve(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='incidents_retrieve',
                description='Retrieve ThreatConnect Incidents',
                input=IncidentsRetrieveInput(),
                output=IncidentsRetrieveOutput())

    def run(self, params={}):
        incidents = self.connection.threat_connect.incidents()
        incident_obj_list = []

        filter1 = incidents.add_filter()

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
            incidents.retrieve()
        except RuntimeError as e:
            raise e

        for incident in incidents:
            incident_obj = {
                'id': incident.id,
                'name': incident.name,
                'date_added': (datetime.datetime.strptime(incident.date_added, '%Y-%d-%mT%H:%M:%SZ').isoformat() or ""),
                'event_date': (datetime.datetime.strptime(incident.event_date, '%Y-%d-%mT%H:%M:%SZ').isoformat() or ""),
                'weblink': incident.weblink
            }
            incident_obj_list.append(incident_obj)

        return {'incidents': incident_obj_list}

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
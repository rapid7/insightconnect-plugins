import komand
from .schema import EmailsRetrieveInput, EmailsRetrieveOutput
# Custom imports below


class EmailsRetrieve(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='emails_retrieve',
                description='Retrieve ThreatConnect E-mails',
                input=EmailsRetrieveInput(),
                output=EmailsRetrieveOutput())

    def run(self, params={}):
        email_obj_list = []
        emails = self.connection.threat_connect.emails()

        filter1 = emails.add_filter()
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

        try:
            emails.retrieve()
        except RuntimeError as e:
            raise e

        for email in emails:
            email_obj = {
                'id': (email.id or ""),
                'name': (email.name or ""),
                'date_added': (email.date_added or ""),
                'weblink': (email.weblink or ""),
                'header': (email.header or ""),
                'subject': (email.subject or ""),
                'from_address': (email.from_address or ""),
                'to': (email.to or ""),
                'body': (email.body or ""),
                'score': (email.score or ""),
            }
            email_obj_list.append(email_obj)

        return {'emails': email_obj_list}

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
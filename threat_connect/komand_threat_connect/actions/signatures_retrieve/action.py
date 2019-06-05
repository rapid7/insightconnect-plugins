import komand
from .schema import SignaturesRetrieveInput, SignaturesRetrieveOutput
# Custom imports below
import datetime


class SignaturesRetrieve(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='signatures_retrieve',
                description='Retrieve ThreatConnect Signatures',
                input=SignaturesRetrieveInput(),
                output=SignaturesRetrieveOutput())

    def run(self, params={}):
        sig_obj_list = []
        signatures = self.connection.threat_connect.signatures()

        filter1 = signatures.add_filter()

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
            filter1 = signatures.add_filter()
            # filter1.add_id(params.get('id'))
        except AttributeError as e:
            raise e

        try:
            signatures.retrieve()
        except RuntimeError as e:
            raise e

        for signature in signatures:
            sig_obj = {
                'id': signature.id,
                'name': signature.name,
                'date_added': (
                            datetime.datetime.strptime(signature.date_added, '%Y-%d-%mT%H:%M:%SZ').isoformat() or ""),
                'weblink': signature.weblink
            }
            sig_obj_list.append(sig_obj)

        return {"signatures": sig_obj_list}

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
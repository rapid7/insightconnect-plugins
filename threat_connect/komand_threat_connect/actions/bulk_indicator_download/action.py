import komand
from .schema import BulkIndicatorDownloadInput, BulkIndicatorDownloadOutput
# Custom imports below
import datetime


class BulkIndicatorDownload(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='bulk_indicator_download',
                description='Retrieve ThreatConnect Bulk Indicator Download',
                input=BulkIndicatorDownloadInput(),
                output=BulkIndicatorDownloadOutput())

    def run(self, params={}):
        indicators = self.connection.threat_connect.bulk_indicators()
        indicator_obj_list = []

        filter1 = indicators.add_filter()
        filter1.add_owner(params.get('owner'))

        if params.get('confidence'):
            filter1.add_pf_confidence(params.get('confidence'))

        if params.get('attribute'):
            filter1.add_pf_attribute(params.get('attribute'))

        if params.get('date_added'):
            filter1.add_pf_date_added(params.get('date_added'))

        if params.get('last_modified'):
            filter1.add_pf_last_modified(params.get('last_modified'))

        if params.get('rating'):
            filter1.add_pf_rating(params.get('rating'))

        if params.get('tag'):
            filter1.add_pf_tag(params.get('tag'))

        if params.get('threat_assess_confidence'):
            filter1.add_pf_threat_assess_confidence(params.get('threat_assess_confidence'))

        if params.get('threat_assess_rating'):
            filter1.add_pf_threat_assess_rating(params.get('threat_assess_rating'))

        if params.get('type'):
            filter1.aadd_pf_type(params.get('type'))

        # Retrieve Indicators and Apply Filters
        try:
            indicators.retrieve()
        except Exception as e:
            raise e

        # Iterate Through Results
        for indicator in indicators:
            indicator_obj = {
                'id': indicator.id,
                'owner_name': (indicator.owner_name or ""),
                'date_added': (
                            datetime.datetime.strptime(indicator.date_added, '%Y-%d-%mT%H:%M:%SZ').isoformat() or ""),
                'last_modified': (datetime.datetime.strptime(indicator.last_modified,
                                                             '%Y-%d-%mT%H:%M:%SZ').isoformat() or ""),
                'rating': (indicator.rating or ""),
                'threat_assess_rating': (str(indicator.threat_assess_rating) or ""),
                'confidence': (indicator.confidence or ""),
                'threat_assess_confidence': (str(indicator.threat_assess_confidence) or ""),
                'type': (indicator.type or ""),
                'weblink': indicator.weblink
            }

            indicator_obj_list.append(indicator_obj)

        return {'bulk_indicators': indicator_obj_list}

    def test(self):
        owners = self.connection.threat_connect.owners()
        owner = ""
        try:
            owners.retrieve()
        except Exception as e:
            raise e

        for owner in owners:
            owner = owner.name
        return {'Owner Name': owner}
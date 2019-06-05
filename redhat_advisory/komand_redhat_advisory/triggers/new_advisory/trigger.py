import komand
import time
from .schema import NewAdvisoryInput, NewAdvisoryOutput
# Custom imports below
import requests
import datetime


_API_HOST = 'https://access.redhat.com/labs/securitydataapi'


class NewAdvisory(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='new_advisory',
            description='Trigger on new advisory',
            input=NewAdvisoryInput(),
            output=NewAdvisoryOutput())

        self.after = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.include_cvrf = False

    def get_cvrf(self, id_):
        if not id_:
            return
        query = "%s/cvrf/%s.json" % (_API_HOST, id_)
        r = requests.get(query)

        if r.status_code == 200:
            results = r.json()
            if results:
                self.logger.info('got cvrf: %s', results)
                return results.get('cvrfdoc')

    def list_advisories(self, start=''):
        query = "%s/cvrf.json" % (_API_HOST)

        r = requests.get(query, { 'after': start })

        if r.status_code != 200:
            self.logger.error('ERROR: Invalid request; returned {} for the following '
                          'query:\n{}'.format(r.status_code, query))
            return []

        results = r.json()
        return results or []

    def find_source_reference(self, refs):
        refs = refs or []
        for r in refs:
            if r.get('type') == 'Self':
                return r['url']

        return ''

    def process_advisory(self, a):
        """
        Normalize some of the incoming data
        """
        self.logger.debug('got event %s', a)

        a['rhsa'] = a.pop('RHSA') or ""
        a['cves'] = a.pop('CVEs') or []
        source = self.get_cvrf(a.get('rhsa')) or {}

        if source.get('document_title'):
            a['title'] = source['document_title']
        if source.get('document_type'):
            a['type'] = source['document_type']
        if source.get('document_publisher'):
            a['publisher'] = source['document_publisher']

        if source.get('document_notes') and source['document_notes'].get('note'):
            a['notes'] =  source['document_notes']['note'] or []
            a['notes'] = '\n'.join(a['notes'])

        if source.get('document_references') and source['document_references'].get('reference'):
            a['references'] = source['document_references']['reference']
            a['url'] = self.find_source_reference(source['document_references']['reference'])

        if self.include_cvrf:
            a['source'] = source

        return a

    def process(self):
        self.logger.info('processing from: %s', self.after)
        advisories = self.list_advisories(self.after)
        self.after = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        for a in advisories:
            a = self.process_advisory(a)
            self.send(a)

    def run(self, params={}):
        """Run the trigger"""

        self.after = params.get('after') or datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.include_cvrf = params.get('include_cvrf')

        # send a test event
        while True:
            self.process()
            time.sleep(30)

    def test(self):
        """Test the trigger by returning an advisory"""
        advisories = self.list_advisories('2016-10-1')
        self.after = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.include_cvrf = True

        for a in advisories:
            return self.process_advisory(a)

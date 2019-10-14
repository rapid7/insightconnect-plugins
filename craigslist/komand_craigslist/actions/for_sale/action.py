import komand
from .schema import ForSaleInput, ForSaleOutput
# Custom imports below
import craigslist
import requests
from ...util import util


class ForSale(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='for_sale',
                description='Search the for sale section',
                input=ForSaleInput(),
                output=ForSaleOutput())

    def run(self, params={}):
        """TODO: Run action"""
        postings=[]

        base_filter = {
           'search_titles': params.get('search_titles'),
           'posted_today': params.get('posted_today'),
           'has_image': params.get('has_image'),
           'query': params.get('query'),
           'search_distance': params.get('search_distance'),
           'zip_code': params.get('zip_code')
        }
        section_filter = params.get('section_filter')
        # The two filters base and section need to be combined into actual filter
        the_filter = base_filter.copy()
        the_filter.update(section_filter)
        self.logger.info('Filter: %s', the_filter)

        # Translate category name to its short hand form
        self.logger.info('Translated category: %s', util.for_sale_category.get('music instr'))
        cat=util.for_sale_category.get(params.get('category'))

        # Make request
        resp = craigslist.CraigslistForSale(
                   site=params.get('site'),
                   category=cat,
                   filters=the_filter,
               )

        # Iterate through returned object of dicts
        for posting in resp.get_results():
             # None types will fail on return because they don't match the spec
             for key in posting:
                 if posting[key] == None:
                     posting[key] = 'N/A'
             postings.append(posting)

        return { 'sale_posting': postings }

    def test(self):
        url = 'https://www.craigslist.org/about/'
        try:
            resp = requests.get(url)
            resp.raise_for_status()
        except:
            self.logger.error('Failed to retrieve test url: %s', url)
            raise

        self.logger.info('Successful request to %s', url)
        return { 'success': 'https://www.craigslist.org/about/'}

import komand
from .schema import ForSaleInput, ForSaleOutput, Input, Output, Component
# Custom imports below
import craigslist
from ...util import util


class ForSale(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='for_sale',
            description=Component.DESCRIPTION,
            input=ForSaleInput(),
            output=ForSaleOutput())

    def run(self, params={}):
        postings = []

        base_filter = {
            'search_titles': params.get(Input.SEARCH_TITLES),
            'posted_today': params.get(Input.POSTED_TODAY),
            'has_image': params.get(Input.HAS_IMAGE),
            'query': params.get(Input.QUERY),
            'search_distance': params.get(Input.SEARCH_DISTANCE),
            'zip_code': params.get(Input.ZIP_CODE)
        }
        section_filter = params.get(Input.SECTION_FILTER)
        # The two filters base and section need to be combined into actual filter
        the_filter = base_filter.copy()
        the_filter.update(section_filter)
        self.logger.info(f'Filter: {the_filter}')

        # Translate category name to its short hand form
        music_instr = util.for_sale_category.get('music instr')
        self.logger.info(f'Translated category: {music_instr}')
        cat = util.for_sale_category.get(params.get(Input.CATEGORY))

        # Make request
        resp = craigslist.CraigslistForSale(
            site=params.get(Input.SITE),
            category=cat,
            filters=the_filter,
        )

        # Iterate through returned object of dicts
        for posting in resp.get_results():
            # None types will fail on return because they don't match the spec
            for key in posting:
                if posting[key] is None:
                    posting[key] = 'N/A'
            postings.append(posting)

        return {Output.SALE_POSTING: postings}

import komand
from .schema import SearchDbInput, SearchDbOutput, Input, Output
# Custom imports below
from typing import Dict, List
import requests
from komand_rapid7_vulndb.util import utils


class SearchDb(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='search_db',
            description='Search the database to find vulnerabilities and exploits',
            input=SearchDbInput(),
            output=SearchDbOutput())

    # def run1(self, params={}):
    #     # Get params
    #     search = params.get(Input.SEARCH)
    #     data_base = params.get(Input.DATABASE)
    #
    #     search = search.replace(" ", "+")
    #     self.logger.info(f'Searching for {search}')
    #
    #     # Set database xpath
    #     temp = path_helper.set_xpath(data_base)
    #     xpath = temp['xpath']
    #     db = temp['db']
    #     self.logger.info('Database set')
    #
    #     # Create web browser
    #     base_url = f'https://www.rapid7.com/db/search?utf8=%E2%9C%93&q={search}&t={db}'
    #     vuldb_browser = browser.VulnDBBrowser(data_base)
    #     results = vuldb_browser.scrape_vuldb(base_url, xpath)
    #     print(f"RESULTS: {results}")
    #     if results['results']:
    #         return {Output.SEARCH_RESULTS: results['results'],
    #                 Output.RESULTS_FOUND: results['found']}
    #     else:
    #         return {Output.RESULTS_FOUND: results['found']}

    # def run(self, params={}):
    #
    #     # Get params
    #     search = params.get(Input.SEARCH)
    #     data_base = params.get(Input.DATABASE)
    #
    #     base_url = "https://vdb-kasf1i23nr1kl2j4.rapid7.com/v1/search"
    #     vuldb_browser = browser.VulnDBBrowser(data_base)
    #     results = vuldb_browser.scrape_vuldb(base_url, xpath)
    #     print(f"RESULTS: {results}")
    #     if results['results']:
    #         return {Output.SEARCH_RESULTS: results['results'],
    #                 Output.RESULTS_FOUND: results['found']}
    #     else:
    #         return {Output.RESULTS_FOUND: results['found']}


    def t(params: Dict):
        # Get params
        search = params.get(Input.SEARCH)
        data_base = params.get(Input.DATABASE)

        q = {"query": search}
        q = utils.R7DB.set_type(q, data_base)
        data = utils.R7DB.get_query(q)
        metadata = data['metadata']
        results = utils.R7DB.paginate(q, metadata['total_pages'])
        print(results)
        return {Output.RESULTS_FOUND: None}



def t(params: Dict):
    params = {"query": "microsoft", "type": "Nexpose"}
    URL = "https://vdb-kasf1i23nr1kl2j4.rapid7.com/v1/search"
    resp = requests.get(URL, params=params, allow_redirects=False)
    data = resp.json()
    md = (data['metadata'])
    for p in range(md['total_pages']):
        if p > 10:
            break
        params["page"] = p
        resp = requests.get(URL, params=params, allow_redirects=False)
        data = resp.json()['data']
        for vd in data:
            print(f"type:{vd['type']}, content_type: {vd['content_type']}")

    print(data['data'][0].keys())
    # dict_keys(['id', 'type', 'identifier', 'title', 'description', 'data',
    #            'references', 'created_at', 'updated_at', 'published_at',
    #            'content_type'])

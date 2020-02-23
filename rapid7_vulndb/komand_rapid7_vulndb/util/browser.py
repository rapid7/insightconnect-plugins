import re
from nntplib import NNTPReplyError

from komand_rapid7_vulndb.util.log_helper import LogHelper
from lxml import html
from selenium import webdriver

from komand.exceptions import PluginException


class VulnDBBrowser:

    def __init__(self, data_base: str, logger=None):
        """
        :param data_base: The data base to search.
        :param logger: allows the class to communicate with the plugin logger.
        """
        self.data_base = data_base

        if logger:
            self.logger = logger
        else:
            self.logger = LogHelper().logger

        #: str: A HTML document created from the body for the request.
        self.html_element = None
        #: str: A HTML document created from the head for the request.
        self.head_html_element = None
        #: object:  A PhantomJS web browser object.
        self.browser = None
        #: list of str: The search results that will be returned to Komand/ICON.
        self.search_results = []
        #: str: Used to help determine if a returned result is a Vulnerability Database, or a Metasploit Module object.
        self.module_name = None
        # TODO figure out what this does. Type string
        self.vuln_db_details = None

    def scrape_vuldb(self, base_url: str, xpath: str) -> dict:
        # Create web browser
        self.browser = webdriver.PhantomJS()
        self.logger.info('Headless browser established')
        all_results = []

        # Iterates over all the pages found
        while True:
            # Set url
            self.browser.get(base_url)
            # create HTML docs for head and body
            inner_html = self.browser.execute_script("return document.body.innerHTML")
            head_html = self.browser.execute_script("return document.head.innerHTML")
            self.head_html_element = html.document_fromstring(head_html)
            self.html_element = html.document_fromstring(inner_html)

            self.vuln_db_details = self.html_element.xpath("//*[@id='torso']/div/article[@class='vulndbDetails']")
            # Check to see if results exist
            backsearch_one = self.html_element.xpath('//*[@id="torso"]/div/div[2]/div[1]/a/@href')
            backsearch_two = self.html_element.xpath('//*[@id="torso"]/div/article/span/a/@href')
            if not backsearch_one and not backsearch_two:
                self.browser.close()
                return {'found': False}
            elif self.vuln_db_details:
                # One iteration, specific details
                self.module_name = self.html_element.xpath('//*[@id="torso"]/div/article/section[2]/h1/text()')
                if self.module_name == ['Module Name']:
                    # Metasploit module
                    xpath = {'name': '//*[@id="torso"]/div/article/h1/text()',
                             'module_name': '//*[@id="torso"]/div/article/section[2]/p/text()',
                             'summary': '//*[@id="torso"]/div/article/section[1]/p/text()',
                             'reliability': '//*[@id="torso"]/div/article/section[5]/ul/li/a/text()',
                             'module_options': '//*[@id="torso"]/div/article/section[7]/p/text()',
                             'source_code': '//*[@id="torso"]/div/article/section[6]/ul/li[1]/a/@href',
                             'history': '//*[@id="torso"]/div/article/section[6]/ul/li[2]/a/@href'}
                    all_results.extend(self.search(xpath))
                elif self.module_name == ['Description']:
                    # Vulnerability
                    xpath = {'name': '//*[@id="torso"]/div/article/h1/text()',
                             'severity': '//*[@id="torso"]/div/article/section[1]/table/tbody/tr/td[1]/text()',
                             'summary': '//*[@id="torso"]/div/article/section[2]/p/text()',
                             'published': '//*[@id="torso"]/div/article/section[1]/table/tbody/tr/td[3]/text()'}
                    all_results.extend(self.search(xpath))
            else:
                self.logger.info("Searching...")
                all_results.extend(self.search(xpath))
            page_disabled = self.html_element.xpath('//*[@id="torso"]/div/div[2]/div[2]/ul/li[@class="nextResult"]/a/@class')
            next_url = self.html_element.xpath('//*[@id="torso"]/div/div[2]/div[2]/ul/li[@class="nextResult"]/a/@href')
            if page_disabled == ['disabled']:
                self.browser.close()
                return {'results': all_results, 'found': True}
            elif not next_url:
                self.browser.close()
                return {'results': all_results, 'found': True}
            # Indicates more results loop over again to add them
            else:
                next_url = self.html_element.xpath('//*[@id="torso"]/div/div[2]/div[2]/ul/li[@class="nextResult"]/a/@href')
                base_url = "https://rapid7.com" + str(next_url[0])

    # Input xpath output data found
    def get_variables(self, **kwargs) -> dict:
        data = {}
        for key, value in kwargs.items():
            try:
                data[key] = self.html_element.xpath(value)
            except NNTPReplyError as e:
                raise PluginException(cause="Server Error",
                                      assistance='HTML has changed for the vulnerability database. Contact support for help.',
                                      data=e)
        return data

    # Input data outputs search_results as json
    @staticmethod
    def convert_variables(**kwargs) -> list:
        search_results = []
        for i in range(0, max(len(x) for x in kwargs.values())):
            new_dict = {}
            for k in kwargs.keys():
                if i < len(kwargs[k]):
                    new_dict[k] = kwargs[k][i]
            search_results.append(new_dict)
        return search_results

    # Input search_results output fixed search_results
    def adjust_variables(self, search_results: list):
        if self.data_base == "All":
            link = self.html_element.xpath('//h4[@class]/a/@href')
            for i in range(0, len(link)):
                search_results[i]['link'] = link[i]
        for result in search_results:
            if 'summary' in result:
                result['summary'] = re.sub(r"\s+", " ", result['summary'])
            if self.module_name == ['Description']:
                solution = self.html_element.xpath('//*[@id="torso"]/div/article/section[4]/text()')
                solution = solution[1]
                result['solution'] = re.sub(r"\s+", "", solution)
            if 'link' in result and (not self.data_base == "All"):
                result['link'] = "https://rapid7.com" + result['link']
            if 'published' in result:
                try:
                    result['published'] = result['published'].split(": ")[1]
                except IndexError:
                    continue
            if (self.module_name == ['Module Name']) or (self.module_name == ['Description']):
                link = self.head_html_element.xpath('//head/link[2]/@href')
                result['link'] = link[0]
            if 'severity' in result:
                try:
                    result['severity'] = result['severity'].split(": ")[1]
                except IndexError:
                    continue

    # Inputs xpath and outputs search_results
    def search(self, xpath: dict) -> list:
        self.logger.info("Searching...")
        html_xpath = self.get_variables(**xpath)
        # Iterates and removes extra whitespace on name
        html_xpath['name'] = list(filter(lambda x: not re.match(r'\s+', x), html_xpath['name']))
        if not self.vuln_db_details and self.data_base != "All":
            html_xpath['link'] = list(filter(lambda x: not re.match(r'^http', x), html_xpath['link']))
        search_results = self.convert_variables(**html_xpath)
        self.adjust_variables(search_results)
        return search_results

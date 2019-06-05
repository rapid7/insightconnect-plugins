import komand
from .schema import UploadInput, UploadOutput
# Custom imports below
import requests
import base64
import time
import re


class Upload(komand.Action):

    __UPLOAD_URL = "https://www.networktotal.com/upload.php"
    __PRELIMINARY_SEARCH_URL = "https://www.networktotal.com/search.php?json=1&q={one}&pmd5={two}"
    __REQ_FAIL_TEXT = "Non-200 status code received!"

    def __init__(self):
        super(self.__class__, self).__init__(
                name='upload',
                description='Upload PCAP file',
                input=UploadInput(),
                output=UploadOutput())

    def run(self, params={}):
        pcap_bytes = params.get("pcap")

        pcap_file = base64.b64decode(pcap_bytes)  # Decode base64 into our PCAP file

        response_text = self.upload_file(file=pcap_file)
        self.logger.info("Run: Got response: {response}".format(response=response_text))

        search_url = self.create_search_url(response_text=response_text)
        self.logger.info("Run: Created search URL: {url}".format(url=search_url))

        results = self.search(url=search_url)
        signatures = results["events"]
        md5 = results["md5"]

        return {"md5": md5, "signatures": signatures}

    def upload_file(self, file):
        """Uploads file to NetworkTotal and returns the response text."""
        response = requests.post(url=self.__UPLOAD_URL, files={"uploaded": file})
        if response.status_code == 200:
            time.sleep(5)  # Based on NetworkTotal upload script. Give NT time to process request.
            return response.text
        else:
            raise Exception(self.__REQ_FAIL_TEXT)

    def create_search_url(self, response_text):
        """Uses regex to capture components from response text to create appropriate search URL."""
        re1 = re.compile("(?<=q=)(.*)(?=&)")
        re2 = re.compile("(?<=&pmd5=)(.*)(?=\">)")

        part_one = re1.search(response_text).group(1)
        part_two = re2.search(response_text).group(1)

        search_url = self.__PRELIMINARY_SEARCH_URL.format(one=part_one, two=part_two)
        return search_url

    def search(self, url):
        """Performs a search against NetworkTotal and returns the JSON response."""
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(self.__REQ_FAIL_TEXT)


    def test(self):
        """TODO: Test action"""
        return {}

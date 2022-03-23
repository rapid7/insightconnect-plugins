from insightconnect_plugin_runtime.exceptions import PluginException

# import all transformations
from komand_rapid7_vulndb.util.transform import (
    transform,
    serialize_fields,
    normalize_published_field,
    flatten_data_field,
    serialize_alternate_ids,
    generate_link_attr,
    pop_non_relevant_search_fields,
    pop_non_relevant_module_fields,
    pop_non_relevant_vuln_fields,
)
from typing import Dict
import requests
import copy
from urllib.parse import urljoin

from komand_rapid7_vulndb.util.util import Util


class Search:
    """
    Rapid7 vulnerability database Search API ETL utilities.
    """

    search_url: str = "https://vdb-kasf1i23nr1kl2j4.rapid7.com/v1/search"

    @classmethod
    @Util.retry(tries=1, timeout=30, exceptions=PluginException, backoff_seconds=1)
    def execute_query(cls, query: Dict) -> Dict:
        """
        Executes API query by sending a request to API
        and extracting the result as a python data structure

        :param query: free form text
        :return: Data as dictionary
        """
        response = requests.get(cls.search_url, params=query, allow_redirects=False)
        _response_error_handler(response.status_code, response.text)
        return response.json()

    @classmethod
    def paginate(cls, query: Dict, num_of_pages: int) -> [Dict]:
        """
        Iterates over available result pages in the API and concatenates the
        results into a single list of dictionaries

        :param query: free form text
        :param num_of_pages: number of pages to query
        :return: List of results
        """

        res: [Dict] = []
        for page_num in range(num_of_pages):
            query["page"] = page_num
            page = cls.execute_query(query)
            for dct in page["data"]:
                res.append(
                    transform(
                        dct,
                        pop_non_relevant_search_fields,
                        generate_link_attr,
                        normalize_published_field,
                    )
                )
        return res

    @classmethod
    def set_query_db_type(cls, query: Dict, plugin_inp_db: str) -> Dict:
        """
        Creates query with the database type to interact with
        based on plugin input
        """
        typed_query = copy.deepcopy(query)
        if plugin_inp_db == "Vulnerability Database":
            typed_query["type"] = "Nexpose"
        if plugin_inp_db == "Metasploit Modules":
            typed_query["type"] = "Metasploit"
        return typed_query

    @classmethod
    def get_results(cls, search_for: str, db: str) -> [Dict]:
        """Finds results based on input parameters"""

        # get number of pages required to get the full result
        query = {"query": search_for}
        query = cls.set_query_db_type(query, db)
        data = cls.execute_query(query)
        num_of_pages = data["metadata"]["total_pages"]

        # get all the pages
        return cls.paginate(query, num_of_pages)


class Content:
    """
    Rapid7 vulnerability database Content API ETL utilities.
    """

    content_url: str = "https://vdb-kasf1i23nr1kl2j4.rapid7.com/v1/content/"

    module_fields_to_serialize: [str] = ["architectures", "references", "authors"]
    vuln_fields_to_serialize: [str] = [
        "solutions",
        "references",
    ]

    @classmethod
    @Util.retry(tries=1, timeout=30, exceptions=PluginException, backoff_seconds=1)
    def retrieve_by_identifier(cls, identifier: str):
        # extract data from API
        response = requests.get(urljoin(cls.content_url, identifier))
        _response_error_handler(response.status_code, response.text)
        return response.json()

    @classmethod
    def get(cls, identifier: str) -> Dict:

        """
        This function extracts data from API and transforms it to match
        plugin schema

        :param identifier: selects required transformations
        :return:  transformed data
        """

        modifiers = []
        data = cls.retrieve_by_identifier(identifier)

        # Fix for bug in API where an int is returned in some conditions on severity
        # E.g. msft-cve-2019-0708
        # "content_result": { "severity": 10 }
        if "data" in data:
            if "severity" in data["data"]:
                if isinstance(data["data"]["severity"], int):
                    data["data"]["severity"] = str(data["data"]["severity"])

        # define how and which order to transform the data
        if data["content_type"] == "module":
            modifiers = [
                flatten_data_field,
                normalize_published_field,
                pop_non_relevant_module_fields,
                *serialize_fields(cls.module_fields_to_serialize),
            ]
        if data["content_type"] == "vulnerability":
            modifiers = [
                flatten_data_field,
                serialize_alternate_ids,
                normalize_published_field,
                pop_non_relevant_vuln_fields,
                *serialize_fields(cls.vuln_fields_to_serialize),
            ]

        # transform the data
        return transform(data, *modifiers)


def _response_error_handler(status_code: int, text: str):
    if 400 <= status_code < 500:
        if status_code == 404:
            raise PluginException(
                cause="The requested resource could not be found.",
                assistance="Please ensure that the input parameters are correct.",
                data=text,
            )
        raise PluginException(
            preset=PluginException.Preset.UNKNOWN,
            data=text,
        )
    if status_code >= 500:
        raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=text)

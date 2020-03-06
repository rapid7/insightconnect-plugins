from komand.exceptions import PluginException

from typing import Dict, List, Callable, Union
import requests
import copy
import sys
from urllib.parse import urljoin


class R7VDB:
    """
    Rapid7 vulnerability database API utilities
    This class is used by the rapid7_vulndb plugin for
    extracting https://vdb.rapid7.com/swagger_doc API data

    """

    search_url: str = "https://vdb-kasf1i23nr1kl2j4.rapid7.com/v1/search"
    content_url: str = 'https://vdb-kasf1i23nr1kl2j4.rapid7.com/v1/content/'
    seach_fields: List[str] = ["title", "published_at", "identifier"]
    content_common_fields: List[str] = ["title", "description", "content_type",
                                        "published_at", "references"]
    content_module_fields: List[str] = ["architectures", "authors", "rank",
                                        "reliability"]
    content_vuln_fields: List[str] = ["severity", "solutions", "alternate_ids"]
    content_module_fields_to_serialize: List[str] = ["architectures",
                                                     "references", "authors"]
    content_vuln_fields_to_serialize: List[str] = ["solutions", "alternate_ids"]

    @classmethod
    def resolve_db_type(cls, input_db: str) -> str:
        fn = sys._getframe().f_code.co_name
        cls.validate(fn, strings=[input_db])
        if input_db == 'Vulnerability Database':
            return 'Nexpose'
        if input_db == 'Metasploit Modules':
            return 'Metasploit'

    @classmethod
    def set_query_db_type(cls, query: Dict, plugin_inp_db: str) -> Dict:
        fn = sys._getframe().f_code.co_name
        cls.validate(fn, dicts=[query], strings=[plugin_inp_db])
        typed_query = copy.deepcopy(query)
        db_type = cls.resolve_db_type(plugin_inp_db)
        typed_query["type"] = db_type
        return typed_query

    @classmethod
    def get_query(cls, query: Dict) -> Dict:
        fn = sys._getframe().f_code.co_name
        cls.validate(fn, dicts=[query])
        try:
            response = requests.get(cls.search_url, params=query,
                                    allow_redirects=False)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise PluginException(
                cause="Unexpected http error",
                data=str(e),
                assistance="If the issue persists please contact support.",
            )
        try:
            data = response.json()
        except ValueError as e:
            raise PluginException(
                cause="Unexpected data format received from Rapid7 API",
                data=str(e),
                assistance="If the issue persists please contact support.")
        return data

    @classmethod
    def paginate_search(cls, query: Dict, num_of_pages: int) -> List[Dict]:
        fn = sys._getframe().f_code.co_name
        cls.validate(fn, dicts=[query], ints=[num_of_pages])
        res: List[Dict] = []
        for page_num in range(num_of_pages):
            query["page"] = page_num
            data = cls.get_query(query)
            for d in data["data"]:
                res.append(cls.make_search_result(d))
        return res

    @classmethod
    def make_search_result(cls, api_data: Dict) -> Dict:
        fn = sys._getframe().f_code.co_name
        cls.validate(fn, dicts=[api_data])

        def link_attr_modifier(d: Dict):
            d.update({"link": cls.content_url + d.get("identifier")})
            d.pop("identifier")

        return cls.gen_dict(api_data, cls.seach_fields,
                            link_attr_modifier,
                            make_unknown_modifier("published_at"))

    @classmethod
    def get_content(cls, identifier: str) -> Dict:
        fn = sys._getframe().f_code.co_name
        cls.validate(fn, strings=[identifier])
        try:
            response = requests.get(
                urljoin(cls.content_url, identifier),
                allow_redirects=False)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise PluginException(
                cause="Unexpected http error",
                data=str(e),
                assistance="If the issue persists please contact support.",
            )
        try:
            data = response.json()
        except ValueError as e:
            raise PluginException(
                cause="Unexpected data format received from Rapid7 API",
                data=str(e),
                assistance="If the issue persists please contact support.")
        return cls.make_content_result(data)

    @classmethod
    def make_content_result(cls, api_data: Dict) -> Dict:
        fn = sys._getframe().f_code.co_name
        cls.validate(fn, dicts=[api_data])
        result_fields = []
        modifiers = []
        if api_data["content_type"] == "module":
            result_fields = cls.content_module_fields + cls.content_common_fields
            modifiers.extend(make_list_serialization_modifiers(
                cls.content_module_fields_to_serialize))
        if api_data["content_type"] == "vulnerability":
            result_fields = cls.content_vuln_fields + cls.content_common_fields
            modifiers.extend(make_list_serialization_modifiers(
                cls.content_vuln_fields_to_serialize))
        flat_data = flatten_data(api_data)
        modifiers.append(make_unknown_modifier("published_at"))
        return cls.gen_dict(flat_data, result_fields, *modifiers)

    @classmethod
    def gen_dict(cls, orig: Dict, keys: List[str],
                 *modifiers: Callable[[Dict], None]) -> Dict:
        """
        Generic method that allows to generate new dictionary
        by extracting subset of the keys form the original dictionary
        and applying any number of callbacks to modify the final result

        :param orig: original dictionary
        :param keys: list of keys to extract
        :param modifiers: callback functions to apply on the generated list
        :return: generated dictionary
        """
        fn = sys._getframe().f_code.co_name
        cls.validate(fn, dicts=[orig], lists=[keys], callables=modifiers)
        res = {k: orig[k] for k in keys}
        for modify in modifiers:
            modify(res)
        return res

    @classmethod
    def validate(cls, origin: str,
                 strings: List[str] = None,
                 ints: List[int] = None,
                 dicts: List[Dict] = None,
                 lists: List[List] = None,
                 callables: List[Callable] = None):
        """
        Generic  args validator that validate common types

        :param origin: name of the origin function
        :param strings: strings to validate
        :param ints: ints to validate
        :param dicts: dictionaries to validate
        :param lists:
        :param callables:

        :raises PluginException
        """
        errs: List[str] = []
        if strings:
            for s in strings:
                if not isinstance(s, str):
                    errs.append(f"{origin} arg {s} is not string")
        if ints:
            for i in ints:
                if not isinstance(i, int):
                    errs.append(f"{origin} arg {i} is not int")
        if dicts:
            for d in dicts:
                if not isinstance(d, dict):
                    errs.append(f"{origin} arg {d} is not dict")
        if lists:
            for lst in lists:
                if not isinstance(lst, list):
                    errs.append(f"{origin} arg {lst} is not list")
        if callables:
            for clb in callables:
                if not callable(clb):
                    errs.append(f"{origin} arg {clb} is not callable")

        if len(errs) != 0:
            raise PluginException(
                cause=PluginException.Preset.SERVER_ERROR,
                assistance=PluginException.Preset.UNKNOWN,
                data=",".join(errs)
            )


def make_list_serialization_modifiers(fields: List[str]) \
        -> List[Callable[[Dict], None]]:
    modifiers: List[Callable[[Dict], None]] = []
    for field in fields:
        modifier = make_list_serialization_modifier(field)
        modifiers.append(modifier)
    return modifiers


def make_list_serialization_modifier(field: str) -> Callable[[Dict], None]:
    # close on specific field
    def f(data: Dict):
        if field in data and isinstance(data[field], List):
            data[field] = ",".join(data[field])

    # return closure
    return f


def make_unknown_modifier(field: str) -> Callable[[Dict], None]:
    # close on specific field
    def f(data: Dict):
        if field in data:
            if not data[field]:
                data[field] = "unknown"

    # return closure
    return f


def published_attr_modifier(d: Dict):
    if not d["published_at"]:
        d["published_at"] = "unknown"


def flatten_data(data: Dict) -> Dict:
    new_data = copy.deepcopy(data)
    for k, v in new_data["data"].items():
        if k not in new_data:
            new_data[k] = v
    return new_data

# def make_unknown_modifiers(fields: List[str]) -> List[Callable[[Dict], None]]:
#     modifiers = []
#     for field in fields:
#         modifier = make_unknown_modifier(field)
#         modifiers.append(modifier)
#     return modifiers
#

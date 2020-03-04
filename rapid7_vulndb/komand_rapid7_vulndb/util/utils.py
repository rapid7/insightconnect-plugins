from komand.exceptions import PluginException

from typing import Dict, List, Union
import requests
import copy


class R7DB:
    base_url: str = "https://vdb-kasf1i23nr1kl2j4.rapid7.com/v1/search"

    @classmethod
    def plugin_to_api_db_type(cls, input_db: str) -> str:
        if input_db == 'Vulnerability Database':
            return 'Nexpose'
        if input_db == '':
            return 'Metasploit'
        return 'all'

    @classmethod
    def set_type(cls, query: Dict[str, Union[str, int]], plugin_inp_db: str) -> \
            Dict[str, Union[str, int]]:
        db_type = cls.plugin_to_api_db_type(plugin_inp_db)
        if db_type != "All":
            typed_query = copy.deepcopy(query)
            typed_query["type"] = db_type
            return typed_query
        return query

    @classmethod
    def get_query(cls, query: Dict["str", Union["str", "int"]]) -> Dict:
        try:
            response = requests.get(cls.base_url, params=query,
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
    def paginate(cls, query: Dict["str", Union["str", "int"]],
                 num_of_pages: int) -> List[Dict["str", Union["str", "int"]]]:
        res: List[Dict[str, Union[str, int]]] = []
        for page_num in range(num_of_pages):
            query["page"] = page_num
            data = cls.get_query(query)
            res.append(data)
        return res

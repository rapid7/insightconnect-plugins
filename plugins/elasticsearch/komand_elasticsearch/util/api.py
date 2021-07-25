from komand_elasticsearch.util.request_api import RequestAPI
from logging import Logger


class ElasticSearchAPI(RequestAPI):
    def __init__(self, url: str, logger: Logger, ssl_verify: bool, username: str = None, password: str = None):
        super(ElasticSearchAPI, self).__init__(
            url=url, logger=logger, ssl_verify=ssl_verify, username=username, password=password
        )

    def index(self, index: str, _id: str = None, params: dict = None, document: dict = None, _type: str = None) -> dict:
        return super()._index(index=index, _type="_doc", _id=_id, params=params, document=document)

    def update(self, index: str, _type: str, _id: str, params: dict = None, script: dict = None) -> dict:
        return self._call_api("POST", f"{index}/_update/{_id}", params, {"script": script})

    def search_documents(self, index: str, json_data: dict = {}, routing: str = None, _type: str = None) -> dict:
        return super()._search_documents(path=f"{index}/_search", routing=routing, json_data=json_data)

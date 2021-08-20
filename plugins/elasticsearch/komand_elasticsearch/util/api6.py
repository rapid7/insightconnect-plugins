from komand_elasticsearch.util.request_api import RequestAPI
from logging import Logger


class ElasticSearchAPI6(RequestAPI):
    def __init__(self, url: str, logger: Logger, ssl_verify: bool, username: str = None, password: str = None):
        super(ElasticSearchAPI6, self).__init__(
            url=url, logger=logger, ssl_verify=ssl_verify, username=username, password=password
        )

    def index(self, index: str, _type: str, _id: str = None, params: dict = None, document: dict = None) -> dict:
        if not _type:
            _type = "_doc"

        return super()._index(index=index, _type=_type, _id=_id, params=params, document=document)

    def update(self, index: str, _type: str, _id: str, params: dict = None, script: dict = None) -> dict:
        if not _type:
            _type = "_doc"

        return self._call_api("POST", f"{index}/{_type}/{_id}/_update", params, {"script": script})

    def search_documents(self, index: str, json_data: dict = {}, routing: str = None, _type: str = None) -> dict:
        if _type:
            path = f"{index}/{_type}/_search"
        else:
            path = f"{index}/_search"

        return super()._search_documents(path, routing, json_data)

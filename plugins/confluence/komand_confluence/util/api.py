from typing import Dict, Any, Union

from atlassian import Confluence

from komand_confluence.util.util import exception_handler

import logging


class ConfluenceAPI:
    def __init__(
        self,
        url: str,
        username: str,
        api_token: str,
        cloud: bool = False,
    ):
        self.url = url
        self.username = username
        self.api_token = api_token
        self.cloud = cloud
        self.confluence = Confluence

    def login(self):
        self.confluence = Confluence(
            url=self.url,
            username=self.username,
            password=self.api_token,
            cloud=self.cloud,
        )

    def health_check(self):
        self.confluence.health_check()

    @exception_handler
    def get_page_id(self, title: str, space: str) -> str:
        return self.confluence.get_page_id(title=title, space=space)

    @exception_handler
    def get_page_by_id(self, page_id: str) -> Dict[str, Any]:
        return self.confluence.get_page_by_id(
            page_id=page_id,
            expand="body.view,space,history,version,ancestors",
            status=None,
            version=None,
        )

    @exception_handler
    def get_page_content(self, page_id: str) -> Union[Dict[str, Any], None]:
        data = self.confluence.get_page_by_id(page_id=page_id, expand="body.view", status=None, version=None)
        if data:
            return data.get("body", {}).get("view", {}).get("value")
        return None

    @exception_handler
    def store_page_content(self, content: str, title: str, space: str) -> Dict[str, Any]:
        page_exists = self.page_exists(space=space, title=title)
        if page_exists:
            logging.info("Updating page...")
            page_id = self.get_page_id(title=title, space=space)
            return self.confluence.update_page(page_id=page_id, title=title, body=content)
        else:
            logging.info("Creating a new page...")
            return self.confluence.create_page(title=title, body=content, space=space)

    @exception_handler
    def page_exists(self, space: str, title: str) -> bool:
        return self.confluence.page_exists(space=space, title=title)


from atlassian import Confluence

from komand_confluence.util.util import exception_handler

import logging
class ConfluenceAPI:

  def __init__(self, url: str = "", username: str = "", password: str = "", cloud: bool = False, client_id: str = "", token: str = ""):
    self.url = url
    self.username = username
    self.password = password
    self.client_id = client_id
    self.token = token
    self.cloud = cloud
    self.confluence = Confluence

  def login(self):
    if self.client_id and self.token:
      oauth2_dict = {
        "client_id": self.client_id,
        "token": self.token,
      }
      self.confluence = Confluence(url=self.url, oauth2=oauth2_dict, cloud=self.cloud)
    elif self.username and self.password:
      self.confluence = Confluence(url=self.url, username=self.username, password=self.password, cloud=self.cloud)

  def health_check(self):
    return self.confluence.health_check()

  @exception_handler
  def get_page_id(self, title: str, space: str):
    return self.confluence.get_page_id(title=title, space=space)

  @exception_handler
  def get_page_by_id(self, page_id: str):
    return self.confluence.get_page_by_id(page_id=page_id, expand="body.view,space,history,version,ancestors", status=None, version=None)

  @exception_handler
  def get_page_content(self, page_id: str):
    data = self.confluence.get_page_by_id(page_id=page_id, expand="body.view", status=None, version=None)
    if data:
      return data.get("body", {}).get("view", {}).get("value")
    return None

  @exception_handler
  def store_page_content(self, content: str, title: str, space: str):
    page_exists = self.page_exists(space=space, title=title)
    if page_exists:
      logging.info("Updating page...")
      page_id = self.get_page_id(title=title, space=space)
      return self.confluence.update_page(page_id=page_id, title=title, body=content)
    else:
      logging.info("Creating a new page...")
      return self.confluence.create_page(title=title, body=content, space=space)

  @exception_handler
  def page_exists(self, space: str, title: str):
    return self.confluence.page_exists(space=space, title=title)

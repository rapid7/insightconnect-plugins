
from atlassian import Confluence


class API:
  def __init__(self, url: str, username: str, password: str, cloud: bool, client_id: str, token: str):
    self.url = url
    self.username = username
    self.password = password
    self.client_id = client_id
    self.token = token
    self.cloud = cloud
    self.confluence = Confluence()



  def login(self):
    if self.client_id and self.token:
      oauth2_dict = {
        "client_id": self.client_id,
        "token": self.token,
      }
      self.confluence = Confluence(url=self.url, oauth2=oauth2_dict, cloud=self.cloud)
    elif self.username and self.password:
      self.confluence = Confluence(url=self.url, username=self.username, password=self.password, cloud=self.cloud)

  def test(self):
    self.confluence.health_check()

  def get_page(self, page_id: str):
    return self.confluence.get_page_by_id(page_id=page_id)

  def get_page_content(self, page_id: str):
    return self.confluence.get_page_by_id(page_id=page_id)

  def store_page_content(self, content: str, page: str, space: str):
    return self.confluence.create_page(title=page, body=content, space=space)

  def handle_responses(self):
    return False


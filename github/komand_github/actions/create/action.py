import komand
import github
from .schema import CreateInput, CreateOutput



class Create(komand.Action):
  def __init__(self):
      super(self.__class__, self).__init__(
              name='create',
              description='Create an issue ticket',
              input=CreateInput(),
              output=CreateOutput())


  def run(self, params={}):
    if params.get('organization') and params.get('repository'):
      g = self.connection.github_user
      repo = g.get_organization(params.get('organization')).get_repo(params.get('repository'))
    else:
      g = self.connection.user
      repo = g.get_repo(params.get('repository'))

    issue_params = {"title": params.get("title"), "body": params.get("body")}

    if params.get("assignee"):
        issue_params.update({"assignee": params.get("assignee")})
    if params.get("milestone"):
        milestone = repo.get_milestone(params.get("milestone"))
        issue_params.update({"milestone": milestone})
    if params.get("labels"):
        labels_raw = params.get('labels').split(',')
        issue_params.update({"labels": labels_raw})

    issue = repo.create_issue(**issue_params)

    return {'url': issue.html_url}

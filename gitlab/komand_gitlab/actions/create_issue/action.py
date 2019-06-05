import komand
from .schema import CreateIssueInput, CreateIssueOutput
# Custom imports below
import json
import requests
import urllib


class CreateIssue(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_issue',
                description='Create issue',
                input=CreateIssueInput(),
                output=CreateIssueOutput())

    def clean_json(self, obj):
        new_json = []
        for key, value in obj.items():
          if value is None:
            value = ''
          if key == 'assignee' and value == "":
              value = {}
          if key == 'milestone' and value == "":
              value = {}
          new_json.append((key, value))
        output = json.dumps(dict(new_json))
        return json.loads(output)

    def run(self, params={}):
        issue_params = []

        if params.get('id'):
          issue_params.append(('id', params.get('id')))
        if params.get('title'):
          issue_params.append(('title', params.get('title')))
        if params.get('description'):
          issue_params.append(('description', params.get('description')))
        if params.get('confidential'):
          issue_params.append(('confidential', params.get('confidential')))
        if params.get('assignee_ids'):
          issue_params.append(('assignee_id', params.get('assignee_id')))
        if params.get('milestone_id'):
          issue_params.append(('milestone_id', params.get('milestone_id')))
        if params.get('labels'):
          issue_params.append(('labels', params.get('labels')))
        if params.get('created_at'):
          issue_params.append(('created_at', params.get('created_at')))
        if params.get('due_date'):
          issue_params.append(('due_date', params.get('due_date')))
        if params.get('merge_request'):
          issue_params.append(('merge_request_to_resolve_discussions_of', params.get('merge_request')))
        if params.get('discussion_resolve'):
          issue_params.append(('discussion_to_resolve', params.get('discussion_resolve')))

        r_url = '%s/projects/%s/issues' % (self.connection.url, params.get('project_id'))
        r_url += '?%s' % (urllib.parse.urlencode(issue_params))

        try:
          r = requests.post(r_url, headers={'PRIVATE-TOKEN': self.connection.token}, verify=False)
          if r.ok:
            return self.clean_json(json.loads(json.dumps(r.json())))
          raise Exception(r.text)
          return
        except requests.exceptions.RequestException as e:  # This is the correct syntax
          self.logger.error(e)
          raise Exception(e)

    def test(self):
        """TODO: Test action"""
        return {}

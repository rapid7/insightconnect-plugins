import komand
import json
import requests
from .schema import CreateIssueOutput, CreateIssueInput


class CreateIssue(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_issue',
                description='Create issue on Bitbucket',
                input=CreateIssueInput(),
                output=CreateIssueOutput())

    def run(self, params={}):

      try:

        issue = {
            'title': params.get('title'), 
            'priority': ('major' if params.get('priority') == 'None' else params.get('priority')), 
            'kind': ('bug' if params.get('kind') == 'None' else params.get('kind')),
            'state': ('new' if params.get('state') == 'None' else params.get('state'))
            }
        issue = dict((keys, v.lower()) for keys, v in issue.items())
        
        if params.get('content'):
          issue['content'] = {'raw': params.get('content')}
        if params.get('component'):
          issue['component'] = {'name': params.get('component')}
        if params.get('assignee'):
          issue['assignee'] = {'username' : params.get('assignee')}
        if params.get('version'):
          issue['version'] = {'name' : params.get('version')}
        if params.get('milestone'):
          issue['milestone'] = {'name' : params.get('milestone')}

        self.connection.bucket_session.headers.update({'Content-Type': 'application/json'})
        api_call = self.connection.base_api + '/repositories/' + self.connection.username + '/' + params.get('repository').lower() + '/issues'
        response = self.connection.bucket_session.post(api_call, data = json.dumps(issue))
        if response.status_code == 201:
          self.logger.info('Issue Successfully created')
          return {'status': 'Issue Successfully created'}
        else:
          resp_obj = response.json()
          return {'error': resp_obj['error']['message']}

      except requests.exceptions.RequestException as e:
        raise e

    def test(self):
      try:
        api_call = self.connection.base_api + '/user'
        response = self.connection.bucket_session.get(api_call)
        if response.status_code == 200:
          return {'status': 'Success - api 2.0 still works'}
      except requests.exceptions.RequestException as e:
        return {'status': 'Error'}

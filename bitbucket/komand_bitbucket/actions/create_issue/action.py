import komand
import json
import requests
from .schema import CreateIssueOutput, CreateIssueInput, Input, Component
from komand.exceptions import PluginException


class CreateIssue(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='create_issue',
            description=Component.DESCRIPTION,
            input=CreateIssueInput(),
            output=CreateIssueOutput())

    def run(self, params={}):
        try:
            issue = {
                'title': params.get(Input.TITLE),
                'priority': ('major' if params.get(Input.PRIORITY) == 'None' else params.get(Input.PRIORITY)),
                'kind': ('bug' if params.get(Input.KIND) == 'None' else params.get(Input.KIND)),
                'state': ('new' if params.get(Input.STATE) == 'None' else params.get(Input.STATE))
            }
            issue = dict((keys, v.lower()) for keys, v in issue.items())

            if params.get(Input.CONTENT):
                issue['content'] = {'raw': params.get(Input.CONTENT)}
            if params.get(Input.COMPONENT):
                issue['components'] = {'name': params.get(Input.COMPONENT)}
            if params.get(Input.ASSIGNEE):
                issue['assignee'] = {'username': params.get(Input.ASSIGNEE)}
            if params.get(Input.VERSION):
                issue['versions'] = {'name': params.get(Input.VERSION)}
            if params.get(Input.MILESTONE):
                issue['milestones'] = {'name': params.get(Input.MILESTONE)}

            self.connection.bucket_session.headers.update({'Content-Type': 'application/json'})
            api_call = f'{self.connection.base_api}/repositories/{self.connection.username}/{params.get(Input.REPOSITORY).lower()}/issues'
            response = self.connection.bucket_session.post(api_call, data=json.dumps(issue))
            if response.status_code == 201:
                self.logger.info('Issue Successfully created')
                return {'status': 'Issue Successfully created'}
            else:
                resp_obj = response.json()
                return {'error': resp_obj['error']['message']}

        except requests.exceptions.RequestException as e:
            raise PluginException(
                cause='User repository error',
                data=e
            )

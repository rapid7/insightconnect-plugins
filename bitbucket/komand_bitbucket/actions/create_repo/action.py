import komand
import json
from komand_bitbucket.util import helpers
from .schema import CreateRepoInput, CreateRepoOutput, Input, Output, Component
from komand.exceptions import PluginException


class CreateRepo(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='create_repo',
            description=Component.DESCRIPTION,
            input=CreateRepoInput(),
            output=CreateRepoOutput())

    def run(self, params={}):
        repo_name = params.get(Input.TITLE).lower()
        try:
            repository = {
                'has_issues': params.get(Input.HAS_ISSUES),  # default False
                'is_private': params.get(Input.IS_PRIVATE),  # default False
                'scm': params.get(Input.TYPE).lower(),  # hg or git default git
                'description': params.get(Input.DESCRIPTION),
                'has_wiki': params.get(Input.HAS_WIKI)
            }
            self.connection.bucket_session.headers.update({'Content-Type': 'application/json'})
            api_call = self.connection.base_api + '/repositories/' + self.connection.username + '/' + repo_name
            repo = self.connection.bucket_session.post(api_call, data=json.dumps(repository))
            repo_obj = repo.json()

            if 'name' not in repo_obj:
                raise PluginException(
                    cause='Create repository error.',
                    assistance='Repository not created'
                )

            try:
                repo_info = helpers.clean_json({
                    'name': repo_obj['name'],
                    'git clone': repo_obj['links']['clone'][0]['href'],
                    'url': repo_obj['links']['html']['href']
                })
                return {Output.REPOSITORY: repo_info}
            except ValueError:
                return {"status": repo_obj['error']['message']}

        except Exception as e:
            raise PluginException(
                cause='Create repository error',
                data=e
            )

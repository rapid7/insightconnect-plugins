import komand
import requests
from .schema import DeleteRepoInput, DeleteRepoOutput, Input, Output, Component
from komand.exceptions import PluginException


class DeleteRepo(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='delete_repo',
            description=Component.DESCRIPTION,
            input=DeleteRepoInput(),
            output=DeleteRepoOutput())

    def run(self, params={}):
        try:
            api_call = f'{self.connection.base_api}/repositories/{self.connection.username}/{params.get(Input.TITLE).lower()}'
            repo = self.connection.bucket_session.delete(api_call)
            if repo.status_code == 204:
                self.logger.info('Run:Repo Successfully deleted')
                return {Output.STATUS: 'Success'}
            else:
                repo_obj = repo.json()
                return {Output.STATUS: repo_obj['error']['message']}

        except requests.exceptions.RequestException as e:
            raise PluginException(
                cause='Create repository error',
                data=e
            )

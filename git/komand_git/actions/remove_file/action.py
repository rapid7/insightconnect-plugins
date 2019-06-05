import komand
from .schema import RemoveFileInput, RemoveFileOutput
# Custom imports below


class RemoveFile(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='remove_file',
                description='Remove a file from the repository',
                input=RemoveFileInput(),
                output=RemoveFileOutput())

    def run(self, params={}):
        file_path = params.get('file_path')

        git_repository = self.connection.git_repository
        result = {}

        self.logger.info('Run: Removing {} from repository'.format(file_path))
        try:
            git_repository.remove(file_path)
            commit_hash = git_repository.commit('Remove {}'.format(file_path))
            result['commit_id'] = commit_hash
            git_repository.push()

            self.logger.info(
                'Run: File {} removed successfully'.format(file_path)
            )
            result['commit_url'] = git_repository.get_commit_url(commit_hash)
            result['success'] = True
        except Exception as e:
            self.logger.error(
                'RemoveFile: Exception: Failed to remove {}:\n{}'.format(
                    file_path, str(e)
                )
            )
            result['success'] = True

        return komand.helper.clean_dict(result)

    def test(self):
        return {
            'success': True,
            'commit_id': 'ee646cea7356dbd8be91490082a5596422dfbd3d',
            'commit_url':
                'https://gitlab.com/komand-test/test-repository/' +
                'commit/ee646cea7356dbd8be91490082a5596422dfbd3d'
        }

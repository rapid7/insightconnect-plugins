import komand
from .schema import AddFileInput, AddFileOutput
# Custom imports below
import base64


class AddFile(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_file',
                description='Add a file to the repository',
                input=AddFileInput(),
                output=AddFileOutput())

    def run(self, params={}):
        file_path = params.get('file_path')
        file_contents = params.get('file_contents', '')

        git_repository = self.connection.git_repository
        result = {}

        self.logger.info('Run: Adding {} to repository'.format(file_path))
        try:
            file_contents = base64.b64decode(file_contents)
            git_repository.create_file(file_path, file_contents)
            git_repository.add(file_path)
            commit_hash = git_repository.commit(
                'Add new file {}'.format(file_path)
            )
            result['commit_id'] = commit_hash
            git_repository.push()

            self.logger.info(
                'Run: File {} added successfully'.format(file_path)
            )
            result['commit_url'] = git_repository.get_commit_url(commit_hash)
            result['success'] = True
        except Exception as e:
            self.logger.error(
                'AddFile: Exception: Failed to add {}:\n{}'.format(
                    file_path, str(e)
                )
            )
            result['success'] = False

        return komand.helper.clean_dict(result)

    def test(self):
        return {
            'success': True,
            'commit_id': 'ee646cea7356dbd8be91490082a5596422dfbd3d',
            'commit_url':
                'https://gitlab.com/komand-test/test-repository/' +
                'commit/ee646cea7356dbd8be91490082a5596422dfbd3d'
        }

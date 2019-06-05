import komand
from .schema import AppendLineToFileInput, AppendLineToFileOutput


class AppendLineToFile(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='append_line_to_file',
                description='Append a line to a file and commit it',
                input=AppendLineToFileInput(),
                output=AppendLineToFileOutput())

    def run(self, params={}):
        file_path = params.get('file_path')
        line = params.get('line')

        git_repository = self.connection.git_repository
        result = {}

        self.logger.info('Run: Appending {} to {}'.format(line, file_path))
        try:
            git_repository.append_line_to_file(file_path, line)
            git_repository.add(file_path)
            commit_hash = git_repository.commit(
                'Update file {}'.format(file_path)
            )
            result['commit_id'] = commit_hash
            git_repository.push()

            self.logger.info(
                'Run: File {} updated successfully'.format(file_path)
            )
            result['commit_url'] = git_repository.get_commit_url(commit_hash)
            result['success'] = True
        except Exception as e:
            self.logger.error(
                'AppendLineToFile: Exception: Failed to update {}:\n{}'.format(
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

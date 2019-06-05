import os
import uuid
from pathlib import Path
from urllib.parse import urlparse

from komand_git.util.cmd import Cmd


class GitRepository:
    ALLOWED_PROTOCOLS = ('ssh', 'http', 'https')

    def __init__(self, repository_url, username, secret, logger):
        self.repository_url = repository_url
        self.username = username
        self.secret = secret
        self.hostname = self._get_hostname()
        self.protocol = self._get_protocol()
        self.repository_name = self._get_repository_name()
        self.user_repository_url = self._get_user_repository_url()
        self.logger = logger
        self.cmd = Cmd(logger)

        self.validate_protocol()

        self.clone_repository()

    def validate_protocol(self):
        if not self.protocol:
            self.logger.error('ValidateProtocol: Protocol not found!')
            raise Exception('Protocol not found')

        if self.protocol not in self.ALLOWED_PROTOCOLS:
            self.logger.error(
                'ValidateProtocol: Protocol {} is not supported'.format(
                    self.protocol
                )
            )
            raise Exception('Protocol not supported: {}'.format(self.protocol))

    def clone_repository(self):
        self.logger.info('CloneRepository: Cloning git repository')

        self.cmd.call('mkdir -p ~/.ssh')
        self.cmd.call(
            'ssh-keyscan -H {} >> ~/.ssh/known_hosts'.format(self.hostname)
        )
        repository_name = '{}_{}'.format(self.repository_name, uuid.uuid4())
        self.cmd.call(
            'git clone {} {}'.format(
                self.user_repository_url, repository_name
            ), self.secret
        )
        os.chdir(repository_name)
        try:
            self.cmd.call('git config user.email "komand@example.com"')
            self.cmd.call('git config user.name "Komand"')
        except Exception as e:
            self.logger.error(
                'CloneRepository: Failed to clone the repository. ' +
                'Make sure that the password and username are correct'
            )
            raise e

    def add(self, path):
        self.cmd.call('git add {}'.format(path))

    def remove(self, path):
        self.cmd.call('git rm {}'.format(path))

    def commit(self, message):
        """
        Commits current changes. Returns full commit hash.
        """
        message = message.replace('"', '')
        self.cmd.call('git commit -m "{}"'.format(message))
        return self.cmd.call('git rev-parse HEAD')

    def get_commit_url(self, commit_hash):
        if self.hostname in ['github.com', 'gitlab.com', 'bitbucket.org']:
            repository_url = os.path.splitext(
                self.repository_url.rstrip('/')
            )[0]
            url = (
                '{}/commits/{}' if self.hostname == 'bitbucket.org' else
                '{}/commit/{}'
            )
            return url.format(repository_url, commit_hash)
        return None

    def push(self):
        self.cmd.call('git push', self.secret)

    def create_file(self, path, bytes_contents):
        path = path.lstrip('/')

        if Path(path).exists():
            self.logger.error('Path: File {} already exists'.format(path))
            raise FileExistsError('File {} already exists'.format(path))
        else:
            try:
                folder_path = os.path.dirname(path)
                Path(folder_path).mkdir(parents=True, exist_ok=True)
                with open(path, 'wb') as f:
                    f.write(bytes_contents)
            except OSError as e:
                self.logger.error(
                    'Open: OSError: Cannot write to file {}:\n{}'.format(
                        path, str(e)
                    )
                )
                raise e

    def append_line_to_file(self, path, line):
        path = path.lstrip('/')

        f = Path(path)
        if not f.exists():
            self.logger.error('Path: File {} does not exist'.format(path))
            raise FileNotFoundError('File {} does not exist'.format(path))
        elif not f.is_file():
            self.logger.error('Path: {} is not a file'.format(path))
            raise FileNotFoundError('{} is not a file'.format(path))
        else:
            try:
                with open(path, 'a+') as f:
                    f.seek(0, 2)
                    size = f.tell()
                    if size:
                        f.seek(size - 1, 0)
                        end_char = f.read()
                        if end_char != '\n':
                            f.write('\n')
                    f.write(line)
            except OSError as e:
                self.logger.error(
                    'Open: OSError: Cannot write to file {}:\n{}'.format(
                        path, str(e)
                    )
                )
                raise e

    def _get_hostname(self):
        return urlparse(self.repository_url).hostname

    def _get_protocol(self):
        return urlparse(self.repository_url).scheme

    def _get_repository_name(self):
        b = self.repository_url.rstrip('/')
        repository_name = b.split('/')[-1]
        return os.path.splitext(repository_name)[0]

    def _get_user_repository_url(self):
        path = urlparse(self.repository_url).path

        return '{}://{}@{}{}'.format(
            self.protocol, self.username, self.hostname, path
        )

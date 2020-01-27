import komand
from .schema import ProjectUpdatedInput, ProjectUpdatedOutput
# Custom imports below
import time
import requests
import hashlib
from functools import reduce
from komand_passivetotal.util import util


class ProjectUpdated(komand.Trigger):

    # Constants
    CACHE_FILE_NAME = "project_updated_hash_file"

    def __init__(self):
        super(self.__class__, self).__init__(
                name='project_updated',
                description='Looks for Updates to a project',
                input=ProjectUpdatedInput(),
                output=ProjectUpdatedOutput())

    def run(self, params={}):
        auth = requests.auth.HTTPBasicAuth(self.connection.username, self.connection.api_key)
        name = params.get('project_name')
        sleep_time = params.get('frequency', 30)
        while True:
            try:
                base_url = 'https://api.passivetotal.org/v2/artifact'
                out = {'project': util.get_project_by_name(name, auth)}
                r = requests.get(base_url, auth=auth, params=out).json()
                artifacts = r.get('artifacts',  {})
                if artifacts:
                    self.logger.info("Artifacts found!")
                    guids = list(map(lambda i: i['guid'], artifacts))
                    guids_sorted = sorted(guids)
                    guid_string = reduce((lambda g1, g2: g1 + g2), guids_sorted)
                    new_hash = hashlib.md5(guid_string.encode())
                    new_hash = new_hash.hexdigest()

                    with komand.helper.open_cachefile(self.CACHE_FILE_NAME) as cache_file:
                        old_hash = cache_file.readline()
                        if old_hash != new_hash:
                            self.logger.info('Project updated')
                            self.logger.info('Old hash: %s, New Hash: %s', old_hash, new_hash)
                            self.send({'artifact': artifacts})
                            cache_file.write(new_hash)
                time.sleep(sleep_time)
            except Exception as e:
                self.logger.error('Could not retrieve artifacts. Error: ' + str(e))
                raise

    def test(self):
        auth = requests.auth.HTTPBasicAuth(self.connection.username, self.connection.api_key)
        r = requests.get('https://api.passivetotal.org/v2/account', auth=auth)
        if r.status_code != 200:
            msg = r.json()
            self.logger.error(msg)
            raise Exception(msg)

        return {'test': 'Successful authentication'}

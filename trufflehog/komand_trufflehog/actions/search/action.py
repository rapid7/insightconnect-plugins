import komand
from .schema import SearchInput, SearchOutput
# Custom imports below
from truffleHog import truffleHog
import json
import re


class Search(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search',
                description='Looks for exposed secrets in the commit history and branches',
                input=SearchInput(),
                output=SearchOutput())

    def run(self, params={}):
        git_url = params.get('git_url')
        do_entropy = params.get('do_entropy')
        do_regex = params.get('do_regex')
        since_commit = params.get('since_commit')
        max_depth = params.get('max_depth')
        custom_regex = params.get('custom_regexes')
        if custom_regex is None:
            custom_regex = {}
        else:
            for key in custom_regex:
                custom_regex[key] = re.compile(custom_regex[key])
        try:
            scan = truffleHog.find_strings(git_url, printJson=True, do_entropy=do_entropy, do_regex=do_regex,
                                           since_commit=since_commit, custom_regexes=custom_regex, max_depth=max_depth,
                                           surpress_output=True)
            git_url = re.sub('\.git', '', git_url)
            found_issues = scan['foundIssues']
            found = {}
            issues = []
            count = 0
            for issue in found_issues:
                with open(issue, 'r') as issue:
                    data = json.loads([line.rstrip() for line in issue][0], strict=False)
                    commit_hash = data['commitHash']
                    # diff = data['diff']
                    # url = re.search("(?P<url>https?://[^\s]+)", diff).group("url")
                    # url = re.sub('\.git', '', url)
                    commit_url = git_url + '/commit/' + commit_hash
                    data.update({'url': str(commit_url)})
                    # found.update({'issue%s' % count: data})
                    found['issue%s' % count] = data
                    issues.append(data)
                count += 1
            return {'issues': issues}

        except Exception:
            self.logger.error('Please enter the correct variables for the input')

    def test(self):
        return {'issues': [{'Test': 'Test'}]}

from jira.resources import User


class JiraApi:
    def __init__(self, jira_client, is_cloud, logger):
        self.jira_client = jira_client
        self.is_cloud = is_cloud
        self.logger = logger

    def delete_user(self, accountId):
        url = self.jira_client._options['server'] + '/rest/api/latest/user/?accountId=%s' % accountId
        r = self.jira_client._session.delete(url)

        if 200 <= r.status_code <= 299:
            return True
        else:
            self.logger.error(r.status_code)
            return False

    def find_users(self, query, max_results=10):
        return self.jira_client._fetch_pages(User, None, 'user/search', 0, max_results, {'query': query})

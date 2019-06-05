import komand
from .schema import UpdateIssueInput, UpdateIssueOutput
# Custom imports below
import json


class UpdateIssue(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_issue',
                description='Update a Sentry issue',
                input=UpdateIssueInput(),
                output=UpdateIssueOutput())

    def run(self, params={}):
        issue_id = params.get('issue_id')

        issue_update_json = {}
        for key in (
            'status', 'assignedTo', 'hasSeen',
            'isBookmarked', 'isSubscribed', 'isPublic'
        ):
            if key in params:
                issue_update_json[key] = params[key]

        issue = self.connection.sentry_connection.request(
            'PUT', 'issues/{}/'.format(issue_id), json=issue_update_json
        )

        return {'issue': issue}

    def test(self):
        return json.loads("""
        {
          "issue": {
            "lastSeen": "2018-07-18T19:39:30Z",
            "numComments": 0,
            "userCount": 0,
            "culprit": "myself",
            "title": "SyntaxError: Hello!",
            "id": "612555152",
            "type": "error",
            "annotations": [],
            "metadata": {
              "type": "SyntaxError",
              "value": "Hello!"
            },
            "status": "resolved",
            "isPublic": false,
            "hasSeen": true,
            "shortId": "PYTHONTEST-5",
            "firstSeen": "2018-07-18T19:39:30Z",
            "count": "1",
            "permalink": "https://sentry.io/komand-test/pythontest/issues/612555152/",
            "level": "error",
            "isSubscribed": false,
            "isBookmarked": false,
            "project": {
              "slug": "pythontest",
              "id": "1244809",
              "name": "PythonTest"
            },
            "statusDetails": {}
          }
        }
        """)

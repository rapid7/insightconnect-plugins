import komand
from .schema import ListProjectIssuesInput, ListProjectIssuesOutput
# Custom imports below
import json


class ListProjectIssues(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_project_issues',
                description='List all issues of a Sentry project',
                input=ListProjectIssuesInput(),
                output=ListProjectIssuesOutput())

    def run(self, params={}):
        organization_slug = params['organization_slug']
        project_slug = params['project_slug']

        query_params = {
            key: params.get(key, None) for key in
            ('statsPeriod', 'shortIdLookup', 'query')
        }

        url = 'projects/{}/{}/issues/'.format(organization_slug, project_slug)
        issues = self.connection.sentry_connection.request(
            'GET', url, query_params=query_params, pagination_enabled=True
        )

        return {'issues': issues}

    def test(self):
        return json.loads("""
        {
          "issues": [
            {
              "lastSeen": "2018-07-18T19:39:30Z",
              "numComments": 0,
              "userCount": 0,
              "stats": {
                "24h": [
                  [
                    1532034000,
                    0
                  ],
                  [
                    1532037600,
                    0
                  ],
                  [
                    1532041200,
                    0
                  ],
                  [
                    1532044800,
                    0
                  ],
                  [
                    1532048400,
                    0
                  ]
                ]
              },
              "culprit": "\\"myself\\"",
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
            },
            {
              "lastSeen": "2018-07-18T19:31:13Z",
              "numComments": 0,
              "userCount": 0,
              "stats": {
                "24h": [
                  [
                    1532070000,
                    0
                  ],
                  [
                    1532073600,
                    0
                  ],
                  [
                    1532077200,
                    0
                  ],
                  [
                    1532080800,
                    0
                  ],
                  [
                    1532084400,
                    0
                  ],
                  [
                    1532088000,
                    0
                  ],
                  [
                    1532091600,
                    0
                  ]
                ]
              },
              "title": "SyntaxError: Wattttt! AHAHAH",
              "id": "612424900",
              "type": "error",
              "annotations": [],
              "metadata": {
                "type": "SyntaxError",
                "value": "Wattttt! AHAHAH"
              },
              "status": "resolved",
              "subscriptionDetails": {
                "reason": "unknown"
              },
              "isPublic": true,
              "hasSeen": true,
              "shortId": "PYTHONTEST-4",
              "shareId": "82d18ebc2c7b42c0a2594410ca06e21d",
              "firstSeen": "2018-07-18T16:51:40Z",
              "count": "3",
              "permalink": "https://sentry.io/komand-test/pythontest/issues/612424900/",
              "level": "error",
              "isSubscribed": true,
              "isBookmarked": true,
              "project": {
                "slug": "pythontest",
                "id": "1244809",
                "name": "PythonTest"
              },
              "statusDetails": {}
            }
          ]
        }
        """)

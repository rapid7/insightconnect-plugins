import komand
from .schema import ListIssueEventsInput, ListIssueEventsOutput
# Custom imports below
import json


class ListIssueEvents(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_issue_events',
                description='List all events of a Sentry issue',
                input=ListIssueEventsInput(),
                output=ListIssueEventsOutput())

    def run(self, params={}):
        issue_id = params.get('issue_id')

        events = self.connection.sentry_connection.request(
            'GET', 'issues/{}/events/'.format(issue_id),
            pagination_enabled=True
        )

        return {'events': events}

    def test(self):
        return json.loads("""
        {
          "events": [
            {
              "eventID": "266e5b557237474eb56e9c2eeaac4a15",
              "packages": {},
              "tags": [
                {
                  "value": "error",
                  "key": "level"
                },
                {
                  "value": "\\"myself\\"",
                  "key": "transaction"
                }
              ],
              "contexts": {},
              "dateReceived": "2018-07-18T19:39:30Z",
              "dateCreated": "2018-07-18T19:39:30Z",
              "fingerprints": [
                "e098a2aa93a10a036b357c3d190c56c3"
              ],
              "metadata": {
                "type": "SyntaxError",
                "value": "Hello!"
              },
              "groupID": "612555152",
              "platform": "other",
              "errors": [
                {
                  "data": {
                    "name": "timestamp",
                    "value": "2018-07-16T00:00:00+02:00"
                  },
                  "message": "Discarded invalid value for parameter 'timestamp'",
                  "type": "invalid_data"
                },
                {
                  "data": {
                    "name": "event_id",
                    "value": "abcd"
                  },
                  "message": "Discarded invalid value for parameter 'event_id'",
                  "type": "invalid_data"
                }
              ],
              "context": {},
              "entries": [
                {
                  "type": "exception",
                  "data": {
                    "values": [
                      {
                        "value": "Hello!",
                        "type": "SyntaxError"
                      }
                    ],
                    "hasSystemFrames": false
                  }
                }
              ],
              "message": "SyntaxError Hello! \\"myself\\"",
              "sdk": {
                "version": "1.0.0",
                "name": "komand",
                "upstream": {
                  "isNewer": false,
                  "name": "komand"
                }
              },
              "type": "error",
              "id": "25152283073",
              "size": 410
            }
          ]
        }
        """)

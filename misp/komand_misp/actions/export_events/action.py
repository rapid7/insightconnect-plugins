import komand
from .schema import ExportEventsInput, ExportEventsOutput
# Custom imports below
import requests
import base64
import json


class ExportEvents(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='export_events',
                description='Export all events in XML format',
                input=ExportEventsInput(),
                output=ExportEventsOutput())

    def run(self, params={}):
        key = self.connection.key
        event_id = params.get('event_id')
        with_attachment = params.get('encode_attachments')
        tags = params.get('tags')
        from_ = params.get('from')
        to_ = params.get('to')
        last = params.get('last')

        path = '/events/xml/download.json'
        url = self.connection.url + path
        headers = {'Accept': 'application/json', 'content-type': 'application/json', 'Authorization': key}

        request = {}
        request['withAttachment'] = with_attachment
        if event_id:
            request['eventid'] = event_id
        if tags:
            request['tags'] = tags
        if from_:
            request['from'] = from_
        if to_:
            request['to'] = to_
        if last:
            request['last'] = last

        post = {'request': request}

        # Generate request
        response = requests.post(url, data=json.dumps(post), headers=headers, verify=False)

        # Raise exception if 200 response is not returned
        if response.status_code != 200:
            response_json = response.json()
            message = str(response_json['message'])
            self.logger.error(message)
            raise Exception(message)

        # Encode data as b64
        events = base64.b64encode(response.text.encode('ascii'))

        return {'events': events.decode("utf-8")}

    def test(self):
        client = self.connection.client
        output = client.test_connection()
        return {'events': ''}

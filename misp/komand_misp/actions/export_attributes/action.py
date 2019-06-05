import komand
from .schema import ExportAttributesInput, ExportAttributesOutput
# Custom imports below
import json
import requests
import base64


class ExportAttributes(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='export_attributes',
            description='Export all attributes in CSV format',
            input=ExportAttributesInput(),
            output=ExportAttributesOutput())

    def run(self, params={}):
        key = self.connection.key
        event_id = params.get('event_id')
        ignore = params.get('include')
        tags = params.get('tags')
        category = params.get('category')
        type_ = params.get('type')
        include_context = params.get('include_context')
        from_ = params.get('from')
        to_ = params.get('to')
        last = params.get('last')

        path = '/events/csv/download'
        url = self.connection.url + path
        headers = {'content-type': 'application/json', 'Authorization': key}

        request = {}
        request['ignore'] = ignore
        request['includeContext'] = include_context
        if event_id:
            request['eventid'] = event_id
        if tags:
            request['tags'] = tags
        if category:
            request['category'] = category
        if type_:
            request['type'] = type_
        if from_:
            request['from'] = from_
        if to_:
            request['to'] = to_
        if last:
            request['last'] = last

        # Generate request
        response = requests.post(url, data=json.dumps(request), headers=headers, verify=False)

        # Raise exception if 200 response is not returned
        if response.status_code != 200:
            response_json = response.json()
            message = str(response_json['message'])
            self.logger.error(message)
            raise Exception(message)

        # Encode data as b64
        attributes = base64.b64encode(response.text.encode('ascii'))

        return {"attributes": attributes.decode("utf-8")}

    def test(self):
        client = self.connection.client
        output = client.test_connection()
        return {"attributes": ''}

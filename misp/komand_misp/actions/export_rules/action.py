import komand
from .schema import ExportRulesInput, ExportRulesOutput
# Custom imports below
import requests
import base64


class ExportRules(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='export_rules',
            description='Export Snort or Suricata rules',
            input=ExportRulesInput(),
            output=ExportRulesOutput())

    def run(self, params={}):
        key = self.connection.key
        _format = params.get('format')
        event_id = params.get('event_id')
        frame = params.get('frame')
        tags = params.get('tags')
        _from = params.get('from')
        _to = params.get('to')
        last = params.get('last')

        path = '/events/nids/%s/download' % _format
        if event_id:
            path = "%s/%s" % (path, event_id)
        else:
            path = "%s/null" % path
        path = "%s/%s" % (path, frame)
        if tags:
            # If more than 1 tag, separate with &&
            if len(tags) > 1:
                tags_str = tags[0]
                tags.pop(0)
                for i in tags:
                    tags_str = "%s&&%s"(tags_str, i)
                path = "%s/%s" % (path, tags_str)
            else:
                path = "%s/%s" % (path, tags)
        else:
            path = "%s/null" % path
        if _from:
            path = "%s/%s" % (path, _from)
        else:
            path = "%s/null" % path
        if _to:
            path = "%s/%s" % (path, _to)
        else:
            path = "%s/null" % path
        if last:
            path = "%s/%s" % (path, last)
        else:
            path = "%s/null" % path
        url = self.connection.url + path
        headers = {'content-type': 'application/json', 'Authorization': key}

        # Generate request
        response = requests.get(url, headers=headers, verify=False)

        # Raise exception if 200 response is not returned
        if response.status_code != 200:
            response_json = response.json()
            message = str(response_json['message'])
            self.logger.error(message)
            raise Exception(message)

        # Encode data as b64
        rules = base64.b64encode(response.text.encode('ascii'))

        return {"rules": rules.decode("utf-8")}

    def test(self):
        client = self.connection.client
        output = client.test_connection()
        return {"rules": ''}

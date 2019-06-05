import komand
from .schema import ExportHashesInput, ExportHashesOutput
# Custom imports below
import requests
import base64


class ExportHashes(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='export_hashes',
            description='Export hashes from HIDS database',
            input=ExportHashesInput(),
            output=ExportHashesOutput())

    def run(self, params={}):
        key = self.connection.key
        format_ = params.get('format')
        tags = params.get('tags')
        from_ = params.get('from')
        to_ = params.get('to')
        last = params.get('last')

        path = '/events/hids/%s/download' % format_
        if tags:
            # If more than 1 tag, separate with &&
            if len(tags) > 1:
                tags_str = tags[0]
                tags.pop(0)
                for i in tags:
                    tags_str = "%s&&%s" % (tags_str, i)
                path = "%s/%s" % (path, tags_str)
            else:
                tags_str = str(tags[0])
                path = "%s/%s" % (path, tags_str)
        else:
            path = "%s/null" % path
        if from_:
            path = "%s/%s" % (path, from_)
        else:
            path = "%s/null" % path
        if to_:
            path = "%s/%s" % (path, to_)
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
        hashes = base64.b64encode(response.text.encode('ascii'))

        return {"hashes": hashes.decode("utf-8")}

    def test(self):
        client = self.connection.client
        output = client.test_connection()
        return {"hashes": ''}

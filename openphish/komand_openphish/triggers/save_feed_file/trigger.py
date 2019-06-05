import komand
import time
from .schema import SaveFeedFileInput, SaveFeedFileOutput, Input, Output
# Custom imports below
import base64
import requests


class SaveFeedFile(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='save_feed_file',
                description='Store the results of the feed file locally',
                input=SaveFeedFileInput(),
                output=SaveFeedFileOutput())

    def run(self, params={}):
        """Run the trigger"""
        while True:
            feed_file = self.get_file_if_changed()
            if feed_file:
                with komand.helper.open_cachefile('/var/cache/feed.txt') as f:
                    f.write(feed_file.decode("utf-8"))

                self.send({
                    Output.STATUSCODE: 200,
                    Output.ENCODEDFEEDFILE: base64.b64encode(feed_file).decode("utf-8")
                })

            time.sleep(params.get(Input.INTERVAL, 5))

    def get_file_if_changed(self):
        with komand.helper.open_cachefile('/var/cache/.etag') as f:
            etag = f.read()
        if not etag:
            etag = ""

        response = requests.get(self.connection.url, headers={'If-None-Match': etag})
        if response.status_code == 304:
            return None

        if response.status_code == 200:
            with komand.helper.open_cachefile('/var/cache/.etag') as f:
                f.write(response.headers.get("etag"))
            return response.content

        self.logger.error(
            "Error: Received HTTP %d status code from OpenPhish. Please check OpenPhish url "
            "and try again. If the issue persists please contact support. "
            "Server response was: %s" % (response.status_code, response.text)
        )
        return None

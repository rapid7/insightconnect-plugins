import komand
from .schema import GetScreenshotsInput, GetScreenshotsOutput
# Custom imports below
import json
import requests
import base64



class GetScreenshots(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_screenshots',
                description='Returns one (jpeg) or all (zip) screenshots associated with the specified task ID',
                input=GetScreenshotsInput(),
                output=GetScreenshotsOutput())

    def run(self, params={}):
        server = self.connection.server
        task_id = params.get('task_id', '')
        screenshot_id = params.get('screenshot_id', '')
        
        if screenshot_id:
            endpoint = server + "/tasks/screenshots/%d/%s" % (task_id, screenshot_id)
        else:
            endpoint = server + "/tasks/screenshots/%d" % (task_id)
        
        try:
            r = requests.get(endpoint)
            r.raise_for_status()
            if r.headers['Content-Type'] == "image/jpeg" or r.headers['Content-Type'] == "application/zip":
                content = r.content
                return {'screenshots': base64.b64encode(content).decode('UTF-8') }        
        
        except Exception as e:
            self.logger.error("Error: " + str(e))

    def test(self):
        out = self.connection.test()
        out['screenshots'] = ''
        return out
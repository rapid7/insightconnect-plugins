import komand
from komand.exceptions import PluginException
from .schema import UnapproveFileLocallyInput, UnapproveFileLocallyOutput
# Custom imports below
import json
import requests


class UnapproveFileLocally(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='unapprove_file_locally',
                description='Remove local approval for a file',
                input=UnapproveFileLocallyInput(),
                output=UnapproveFileLocallyOutput())

    def run(self, params={}):
        file_id = params.get('file_id')
        url = self.connection.host + '/api/bit9platform/v1/fileInstance/%d' % file_id

        self.logger.info("Getting file instance info...")
        file_info_request = self.connection.session.get(url, verify=self.connection.verify)

        try:
            file_info_request.raise_for_status()
        except requests.exceptions.RequestException as e:
            self.logger.info(f"Call to Carbon Black raised exception: {e}")
            raise PluginException(cause="Call to Carbon Black failed!",
                                  assistance="The connection may not be configured properly or an invalid "
                                             "file ID was found.")

        file_instance_object = file_info_request.json()
        file_instance_object['localState'] = 1

        self.logger.info("Removing approval for local file...")

        r = self.connection.session.put(url, json.dumps(file_instance_object), verify=self.connection.verify)

        try:
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            self.logger.info(f"Request content: {r.text}")
            self.logger.info(f"Call to Carbon Black raised exception: {e}")
            raise PluginException(cause="Call to Carbon Black failed",
                                  assistance="The connection may not be configured properly, please"
                                             "check your connection settings.")


        result = komand.helper.clean(r.json())

        return {"file_instance": result}

    def test(self):
        url = self.connection.host + "/api/bit9platform/v1/approvalRequest?limit=-1"  # -1 returns just the count (lightweight call)

        request = self.connection.session.get(url=url, verify=self.connection.verify)

        try:
            request.raise_for_status()
        except:
            raise Exception('Run: HTTPError: %s' % request.text)

        return {}

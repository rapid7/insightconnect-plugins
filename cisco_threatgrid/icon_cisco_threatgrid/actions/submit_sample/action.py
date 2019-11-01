import komand
from .schema import SubmitSampleInput, SubmitSampleOutput, Input, Output, Component
# Custom imports below
import base64
from komand.exceptions import PluginException


class SubmitSample(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='submit_sample',
                description=Component.DESCRIPTION,
                input=SubmitSampleInput(),
                output=SubmitSampleOutput())

    def run(self, params={}):

        # File handling
        file_ = params.get(Input.SAMPLE, None)
        try:
            file_bytes = base64.b64decode(file_['content'])
        except Exception:
            raise PluginException(cause=PluginException.Preset.BASE64_DECODE, data=file_["content"])

        callback_url = params.get(Input.CALLBACK_URL)
        email_notification = params.get(Input.EMAIL_NOTIFICATION)
        network_exit = params.get(Input.NETWORK_EXIT)
        playbook = params.get(Input.PLAYBOOK)
        private = params.get(Input.PRIVATE)
        sample = file_bytes
        sample_filename = params.get(Input.SAMPLE_FILENAME)
        sample_password = params.get(Input.SAMPLE_PASSWORD)
        tags = params.get(Input.TAGS)
        vm = params.get(Input.VM)

        data = {
            "callback_url": callback_url,
            "email_notification": email_notification,
            "network_exit": network_exit,
            "playbook": playbook,
            "private": private,
            "sample_filename": sample_filename,
            "sample_password": sample_password,
            "tags": tags,
            "vm": vm,
        }
        files = {"sample": sample}

        result = self.connection.api.submit_sample(data=data, files=files)

        return {Output.RESULTS: komand.helper.clean(result)}

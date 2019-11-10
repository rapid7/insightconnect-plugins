import komand
from .schema import SubmitUrlInput, SubmitUrlOutput, Input, Output, Component
# Custom imports below


class SubmitUrl(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='submit_url',
                description=Component.DESCRIPTION,
                input=SubmitUrlInput(),
                output=SubmitUrlOutput())

    def run(self, params={}):
        url = params.get(Input.URL)
        callback_url = params.get(Input.CALLBACK_URL)
        email_notification = params.get(Input.EMAIL_NOTIFICATION)
        network_exit = params.get(Input.NETWORK_EXIT)
        playbook = params.get(Input.PLAYBOOK)
        private = params.get(Input.PRIVATE)
        tags = params.get(Input.TAGS)
        vm = params.get(Input.VM)

        data = {
            "callback_url": callback_url,
            "email_notification": email_notification,
            "network_exit": network_exit,
            "playbook": playbook,
            "private": private,
            "tags": tags,
            "vm": vm,
        }

        sample = '[InternetShortcut]\nURL={}'.format(url)
        files = {"sample": sample}

        result = self.connection.api.submit_sample(data=data, files=files)

        return {Output.RESULTS: komand.helper.clean(result)}

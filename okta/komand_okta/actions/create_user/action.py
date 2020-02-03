import komand
from .schema import CreateUserInput, CreateUserOutput, Input, Component
# Custom imports below
import json
import requests
from komand.exceptions import PluginException


class CreateUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='create_user',
            description=Component.DESCRIPTION,
            input=CreateUserInput(),
            output=CreateUserOutput())

    def run(self, params={}):
        okta_url = self.connection.okta_url
        # We need to handle nextLogin ourselves, we simplified the UI for user
        try:
            # This is an optional field
            # https://developer.okta.com/docs/api/resources/users#request-parameters
            nl = params[Input.NEXTLOGIN]
            if nl:
                params[Input.NEXTLOGIN] = 'changePassword'
            if not nl:
                params[Input.NEXTLOGIN] = 'false'
        except KeyError:
            # Docs say Type: String  Required: FALSE  Default: FALSE
            params[Input.NEXTLOGIN] = 'false'

        # Build API URL
        url = requests.compat.urljoin(okta_url, '/api/v1/users')

        # This request needs URL params, we build these here
        url_params = {
            # Turning boolean False into string false, same for True
            "activate": str(params.get(Input.ACTIVATE, True)).lower(),
            "provider": str(params.get(Input.PROVIDER, False)).lower(),
            "nextLogin": str(params.get(Input.NEXTLOGIN, False)).lower()
        }
        self.logger.info("URL params: " + str(url_params))

        # Build POST data object
        data = self.build_post(params)

        # Make the request with all the things we carefully built
        response = self.connection.session.post(url, params=url_params, json=data)
        # Could contain credentials so debug only
        self.logger.debug("Body params: " + str(response.request.body))

        try:
            data = response.json()
        except json.decoder.JSONDecodeError:
            self.logger.error('Okta: API Response: ' + response.text)

        # Success
        if response.status_code == 200:
            # Post processing and clean-up
            # Check if status key exists before grabbing the current state
            if 'status' in data:
                if data['status'] == 'ACTIVE':
                    self.logger.info('Okta: The user activation process is complete')
            # Check if transitioning key exists before grabbing the current state
            if 'transitioningToStatus' in data:
                if data['transitioningToStatus'] == 'ACTIVE':
                    self.logger.info("Okta: In-progress asynchronous status transition")
            # Possibly None is not of type u'string' on some null keys in response
            return komand.helper.clean(data)

        # Failure
        else:
            # Post processing
            if 'errorCauses' in data:
                # 400 {
                #         'errorCode': 'E0000001',
                #         'errorSummary': 'Api validation failed: login',
                #         'errorLink': 'E0000001',
                #         'errorId': 'oaeLSaBdN2JQVOErInD8HDGfA',
                #         'errorCauses': [
                #                 {'errorSummary': 'login: The field cannot be left blank'},
                #                 {'errorSummary': 'firstName: The field cannot be left blank'},
                #                 ...
                #         ]
                #     }
                if isinstance(data['errorCauses'], list):
                    # If list is not empty log its contents
                    if data['errorCauses']:
                        self.logger.error('Okta: API errorCauses: ' + str(data['errorCauses']))

                        # User may already exist with this particular error
                        if response.status_code == 400:
                            if 'errorCode' in data:
                                if data["errorCode"] == "E0000001":
                                    # Iterate over list of errorSummary objects
                                    for error in data['errorCauses']:
                                        if 'errorSummary' in error:
                                            if 'An object with this field already exists' in error['errorSummary']:
                                                raise PluginException(
                                                    cause='Okta: Create user failed. The user may already exist',
                                                    assistance=error['errorSummary'])

            if 'errorSummary' in data:
                # 405: {
                #        u'errorCode': u'E0000022',
                #        u'errorSummary': u'The endpoint does not support the provided HTTP method',
                #        u'errorLink': u'E0000022',
                #        u'errorCauses': [],
                #        u'errorId': u'oaexVslu0CIQCWH63QtUs4kSw'
                #     }
                self.logger.error('Okta: API errorSummary: ' + data['errorSummary'])

        # Non-successful catch all
        raise PluginException(
            cause='Okta: Create user failed unexpectedly.',
            assistance=' Make sure any provided objects, such as profile or credentials match the Okta schemas.'
                       ' For more details, see https://developer.okta.com/docs/api/resources/users#request-parameters'
        )

    def build_post(self, params):
        """
        Build POST request data
        :param params: User's params input
        :return: New object
        """
        data = {'profile': params.get(Input.PROFILE)}
        # "credentials": {
        #   "password": {
        #     "value": "test123DOG$test"
        #   },
        #   "recovery_question": {
        #     "answer": "Wat it do?",
        #     "question": "Party bus"
        #   },
        #   "provider": {
        #     "type": "OKTA",
        #     "name": "OKTA"
        #   }
        # }

        # Only grab if user supplied it
        if 'credentials' in params:
            data['credentials'] = params.get(Input.CREDENTIALS)
            # If some of these are empty we must remove them otherwise API will complain
            if not params.get(Input.CREDENTIALS).get('password').get('value'):
                del data['credentials']['password']
            if not params.get(Input.CREDENTIALS).get('recovery_question').get('answer'):
                del data['credentials']['recovery_question']
            # This may no longer be here from above
            if 'recovery_question' in params.get(Input.CREDENTIALS):
                if not params.get(Input.CREDENTIALS).get('recovery_question').get('question'):
                    del data['credentials']['recovery_question']
            if not params.get(Input.CREDENTIALS).get('provider').get('name'):
                del data['credentials']['provider']
            # This may no longer be here from above
            if 'provider' in params.get(Input.CREDENTIALS):
                if not params.get(Input.CREDENTIALS).get('provider').get('type'):
                    del data['credentials']['provider']

        if 'groupIds' in params:
            data['groupIds'] = params.get(Input.GROUPIDS)

        return data

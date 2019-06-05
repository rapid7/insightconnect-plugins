import komand
from .schema import CreateBlockedSenderPolicyInput, CreateBlockedSenderPolicyOutput, Input, Output
# Custom imports below
from komand_mimecast.util import util


class CreateBlockedSenderPolicy(komand.Action):

    # URI for create blocked sender policy
    _URI = '/api/policy/blockedsenders/create-policy'

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_blocked_sender_policy',
                description='Creates a blocked sender policy',
                input=CreateBlockedSenderPolicyInput(),
                output=CreateBlockedSenderPolicyOutput())

    def run(self, params={}):
        # Import variables from connection
        url = self.connection.url
        username = self.connection.username
        password = self.connection.password
        access_key = self.connection.access_key
        secret_key = self.connection.secret_key
        app_id = self.connection.app_id
        app_key = self.connection.app_key
        auth_type = self.connection.auth_type

        source_ips = params.get(Input.SOURCE_IPS)
        option = params.get(Input.OPTION)

        data = {'option': option}

        # Generate policy dictionary
        policy = {}
        for key, value in params.items():
            temp = util.normalize(key, value)
            policy.update(temp)

        # Remove source_ips and option from policy as they should not be directly in that dictionary
        if params.get(Input.SOURCE_IPS):
            del policy['sourceIps']
        del policy['option']

        # Transform source_ips from comma delimited string to list
        if params.get(Input.SOURCE_IPS):
            source_ips = source_ips.split(',')

        # Add conditions dic to policy
        if source_ips:
            policy['conditions'] = {'sourceIPs': source_ips}

        # Add policy to data
        data['policy'] = policy

        # Mimecast request
        mimecast_request = util.MimecastRequests()
        response = mimecast_request.mimecast_post(url=url, uri=CreateBlockedSenderPolicy._URI, username=username,
                                                  password=password, auth_type=auth_type,
                                                  access_key=access_key, secret_key=secret_key,
                                                  app_id=app_id, app_key=app_key, data=data)

        # Logout
        logout = util.Authentication()
        logout_result = logout.logout(url=url, username=username, password=password,
                                      auth_type=auth_type, access_key=access_key,
                                      secret_key=secret_key, app_id=app_id, app_key=app_key)

        try:
            # Test for logout fail
            if logout_result['fail']:
                self.logger.error(logout_result['fail'])
                try:
                    raise Exception(
                        'Could not log out. Contact support for help. Status code is {}, see log for details'.format(
                            response['meta']['status']))
                except KeyError:
                    self.logger.error(response)
                    raise Exception(
                        'Unknown error. The Mimecast server did not respond correctly, see log for details.')

        except KeyError:
            # Unknown key error
            self.logger.error(logout_result)
            raise Exception(
                'Unknown error. The Mimecast server did not respond correctly, see log for details.')

        return {Output.SENDER_POLICY: response['data']}

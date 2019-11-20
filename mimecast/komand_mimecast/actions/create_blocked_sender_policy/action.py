import komand
from .schema import CreateBlockedSenderPolicyInput, CreateBlockedSenderPolicyOutput, Input, Output
# Custom imports below
from komand_mimecast.util import util


class CreateBlockedSenderPolicy(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_blocked_sender_policy',
                description='Creates a blocked sender policy',
                input=CreateBlockedSenderPolicyInput(),
                output=CreateBlockedSenderPolicyOutput())

    def run(self, params={}):
        # Import variables from connection
        url = self.connection.url
        uri = self.connection.CREATE_BLOCKED_SENDER_POLICY_URI
        access_key = self.connection.access_key
        secret_key = self.connection.secret_key
        app_id = self.connection.app_id
        app_key = self.connection.app_key

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
        response = mimecast_request.mimecast_post(url=url, uri=uri,
                                                  access_key=access_key, secret_key=secret_key,
                                                  app_id=app_id, app_key=app_key, data=data)

        return {Output.SENDER_POLICY: response['data']}

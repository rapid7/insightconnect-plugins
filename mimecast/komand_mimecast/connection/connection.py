import komand
from .schema import ConnectionSchema

# Custom imports below
from komand_mimecast.util import util


class Connection(komand.Connection):
    # The distinct URIs from Mimecast for each action
    GET_MANAGED_URL_URI = '/api/ttp/url/get-all-managed-urls'
    DELETE_MANAGED_URL_URI = '/api/ttp/url/delete-managed-url'
    CREATE_MANAGED_URL_URI = '/api/ttp/url/create-managed-url'
    ADD_GROUP_MEMBER_URI = '/api/directory/add-group-member'
    CREATE_BLOCKED_SENDER_POLICY_URI = '/api/policy/blockedsenders/create-policy'
    FIND_GROUPS_URI = '/api/directory/find-groups'
    DECODE_URL_URI = '/api/ttp/url/decode-url'
    GET_TTP_URL_LOGS_URI = '/api/ttp/url/get-logs'
    PERMIT_OR_BLOCK_SENDER_URI = '/api/managedsender/permit-or-block-sender'

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        # set Variables
        self.url = params.get('url')
        self.app_id = params.get('app_id')
        self.app_key = params.get('app_key').get('secretKey')
        self.secret_key = params.get('secret_key').get('secretKey')
        self.access_key = params.get('access_key').get('secretKey')

    def test(self):
        payload = {
            'data': []
        }

        uri = "/api/account/get-account"

        # Mimecast request
        mimecast_request = util.MimecastRequests()
        mimecast_request.mimecast_post(url=self.url, uri=uri,
                                       access_key=self.access_key, secret_key=self.secret_key,
                                       app_id=self.app_id, app_key=self.app_key, data=payload)

        return {'connection': 'successful'}

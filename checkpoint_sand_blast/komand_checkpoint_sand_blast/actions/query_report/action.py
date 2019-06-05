import komand
from .schema import QueryReportInput, QueryReportOutput
# Custom imports below
import json
import requests
import time


class QueryReport(komand.Action):

    _QUERY = 'query'
    _HEADERS = {'Content-type': 'application/json'}
    _HTTPERROR = {301: 'moved permanently',
                  400: 'bad request',
                  401: 'unauthorized',
                  403: 'forbidden',
                  404: 'not found',
                  500: 'internal server error',
                  503: 'service unavailable',
                  000: 'Unknown Status Code'
                  }

    def __init__(self):
        super(self.__class__, self).__init__(
                name='query_report',
                description='Query the status of a file',
                input=QueryReportInput(),
                output=QueryReportOutput())

    def run(self, params={}):
        file_digest = params.get('file_digest')
        file_digest_type = params.get('file_digest_type')
        file_type = params.get('file_type')
        file_name = params.get('file_name')
        features = params.get('features')
        quota = params.get('quota')
        features_list = features.split(",")

        # Build URL
        url = self.connection.url + self._QUERY

        # Build request JSON
        request = {"request": {file_digest_type: file_digest}}
        if file_type:
            request['request']['file_type'] = file_type
        if file_name:
            request['request']['file_name'] = file_name
        if features:
            # Error correction to allow only valid features
            temp_list = list()
            good_features = ['te', 'av', 'extraction']
            # Loop to check all features against a list of valid features
            for feature in features_list:
                if feature in good_features:
                    temp_list.append(feature)
                else:
                    # Log that a requested feature was invalid
                    self.logger.error('{} is not a valid feature'.format(feature))
            # if one or more features was valid
            if temp_list:
                features_list = temp_list
                request['request']['features'] = features_list
            # all features were invalid
            else:
                self.logger.error('feature input was invalid.'
                                  ' valid features are te av and extraction.')
                raise ValueError('invalid feature')
        if quota:
            request['request']['quota'] = quota
        request = json.dumps(request)
        self.logger.info('query request: {}'.format(request))

        try:
            response = self.connection.session.post(url, headers=self._HEADERS, data=request)
        except requests.RequestException as e:
            raise Exception(e)
        if response.status_code == 200:
            response_json = response.json()
            code = response_json['response']['status']['code']
            if code == 1001:
                return {'query_response': response_json['response'], 'found': True}
            elif code == 1003:
                time.sleep(8)
                response = self.connection.session.post(url, headers=self._HEADERS, data=request)
                response_json = response.json()
                return {'query_response': response_json['response']}
            elif code == 1004:
                return {'found': False}
            else:
                label = response_json['response']['status']['label']
                message = response_json['response']['status']['message']
                self.logger.error('There was a issue with the return from Checkpoint: {}'
                                  .format(message))
                raise Exception('Checkpoint error {code} {label}'.format(code=code, label=label))

        else:
            status_code_message = self._HTTPERROR.get(response.status_code, self._HTTPERROR[000])
            self.logger.error("{status} ({code})".format(status=status_code_message,
                                                         code=response.status_code))
            raise Exception('HTTP Error code{}'.format(response.status_code))

    def test(self):
        # TODO: Implement test function
        return {}

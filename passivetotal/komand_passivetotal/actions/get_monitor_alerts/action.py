import komand
from .schema import GetMonitorAlertsInput, GetMonitorAlertsOutput
# Custom imports below
import requests
from copy import deepcopy
from komand_passivetotal.util import util


class GetMonitorAlerts(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_monitor_alerts',
                description='Retrieve all alerts associated with an artifact or project',
                input=GetMonitorAlertsInput(),
                output=GetMonitorAlertsOutput())

    def run(self, params={}):
        try:
            base_url = "https://api.passivetotal.org/v2/monitor"
            auth = requests.auth.HTTPBasicAuth(self.connection.username, self.connection.api_key)

            url_params = deepcopy(params)
            # if params['project'] != '' and params['artifact'] != '':
            #     self.logger.info('Project and artifact both specified, defaulting to artifact')
            #     del url_params['project']
            # elif params['project'] != '':
            #     url_params["project"] = util.get_project_by_name(params['project'], auth)
            url_params["project"] = util.get_project_by_name(params['project'], auth)

            if params['start'] == '0001-01-01T00:00:00Z':
                del url_params['start']
            else:
                url_params['start'] = url_params['start'].replace('T', ' ')[:-6]

            if params['end'] == '0001-01-01T00:00:00Z':
                del url_params['end']
            else:
                url_params['end'] = url_params['end'].replace('T', ' ')[:-6]

            r = requests.get(base_url, auth=auth, params=url_params).json()
            return {"results": r['results'], "total_records": r['totalRecords']}

        except Exception as e:
            self.logger.error("Could not retrieve monitor alerts. Error: " + str(e))
            raise

    def test(self):
        auth = requests.auth.HTTPBasicAuth(self.connection.username, self.connection.api_key)
        r = requests.get("https://api.passivetotal.org/v2/account", auth=auth).json()
        if 'fullName' in r:
            return {"results": {"message": "Connection succeeded"}}
        raise Exception("Connection failed")

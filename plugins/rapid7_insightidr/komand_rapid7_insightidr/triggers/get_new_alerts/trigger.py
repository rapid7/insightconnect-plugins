import insightconnect_plugin_runtime
import time
from .schema import GetNewAlertsInput, GetNewAlertsOutput, Input, Output, Component
# Custom imports below
import datetime
import json
from insightconnect_plugin_runtime.helper import clean
from komand_rapid7_insightidr.util.endpoints import Alerts
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper

class GetNewAlerts(insightconnect_plugin_runtime.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="get_new_alerts",
                description=Component.DESCRIPTION,
                input=GetNewAlertsInput(),
                output=GetNewAlertsOutput())

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        # END INPUT BINDING - DO NOT REMOVE
        self.logger.info("Get Alerts: trigger started")
        input_frequency = params.get(Input.FREQUENCY)

        # Set initial set for storing initial alert_rrn values
        initial_alerts = set()
    
        # Flag to track the first execution
        first_execution = True

        while True:
            start_time = datetime.datetime.utcnow() - datetime.timedelta(minutes=20)
            
            search = clean(
                {
                    "start_time": start_time.strftime("%Y-%m-%dT%H:%M:%SZ")
                }
            )
            data = clean(
                {
                    "search": search
                }
            )

            self.connection.session.headers["Accept-version"] = "strong-force-preview "
            request = ResourceHelper(self.connection.session, self.logger)

            endpoint = Alerts.get_alert_serach(self.connection.url)
            response = request.resource_request(endpoint, "post", payload=data)

            result = json.loads(response.get("resource"))
        
            total_items = result['metadata'].get('total_items', 0)
    
            alerts = result.get("alerts", [])
            
            #If there are more than 100 results fetch more until all results are stored.
            if total_items > 100:
                index = 100
                while index < total_items:
                    data = clean({"search": {"start_time": start_time.strftime("%Y-%m-%dT%H:%M:%SZ"), "index": index}})
                    self.connection.session.headers["Accept-version"] = "strong-force-preview "
                    request = ResourceHelper(self.connection.session, self.logger)

                    endpoint = Alerts.get_alert_serach(self.connection.url)
                    response = request.resource_request(endpoint, "post", payload=data)
                    
                    result = json.loads(response.get("resource"))
                    alerts.extend(result.get("alerts", []))
                    index += 100
            
            #If not the first iteration send new alerts to output and create new list to compare on next fetch
            if not first_execution:
                for alert in alerts:
                    alert_rrn = alert['rrn']
                    if alert_rrn not in initial_alerts:
                        self.send_alert(alert)
                initial_alerts.clear()
                for alert in alerts:
                    alert_rrn = alert['rrn']
                    initial_alerts.add(alert_rrn)
            #For first iteration store alert_rrn's for last 20 minutes for comparison on next fetch.
            else:
                initial_alerts.update(alert['rrn'] for alert in alerts)
                first_execution = False

            # Back off before next iteration (sleep for 15 seconds)
            time.sleep(input_frequency)
                        

    def send_alert(self, alert: dict):
        self.logger.info(f"Alert found: {alert.get('rrn')}")
        self.send({Output.ALERT: clean(alert)})
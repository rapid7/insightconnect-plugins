import komand
import time
from .schema import GetNewEventsInput, GetNewEventsOutput
# Custom imports below

class GetNewEvents(komand.Trigger):
    CACHE_FILE_NAME = "event_cache"

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_new_events',
                description='Retrieves new events from ESM',
                input=GetNewEventsInput(),
                output=GetNewEventsOutput())

    def run(self, params={}):
        """Run the trigger"""
        alert_id = {"name": "AlertID", "types": ["STRING"]}
        esm_session = self.connection.esm_session
        event_information = {}

        config = {"config":{"includeTotal": False}}
        config["config"]["timeRange"] = params.get("timerange")
        config["config"]["fields"] = params.get("fields")
        config["config"]["filters"] = params.get("filters")

        # Check to see if AlertID is not in config
        if alert_id not in config["config"]["fields"]:
            config["config"]["fields"].append(alert_id)

        # Create Cache and build content
        with komand.helper.open_cachefile(self.CACHE_FILE_NAME) as cache_file:
            self.logger.debug("Run: Got or created cache file: {file}".format(file=cache_file))
            contents = cache_file.readlines()
            contents = [x.strip() for x in contents]

        result_id = dict()
        status_complete = False
        exe_qry = "qryExecuteDetail?type=EVENT&reverse=false"
        get_status = "qryGetStatus"
        get_results = "qryGetResults?startPos=0&numRows=0&reverse=false"

        qry_url = self.connection.url + exe_qry
        qry_status = self.connection.url + get_status
        qry_results = self.connection.url + get_results

        # Execute Query
        def execute_qry(url, config):
            resp = esm_session.post(url, json=config, verify=False)
            result_id["resultID"] = resp.json()["return"]["resultID"]

        # Check status
        def checkStatus(url, result_id):
            resp = esm_session.post(url, json=result_id, verify=False)
            return resp.json()["return"]["complete"]

        # Retrieve Results
        def retrieveResults(url, status_complete, result_id):
            if status_complete:
                try:
                    resp = esm_session.post(url, json=result_id, verify=False)
                    return resp.json()
                except Exception as e:
                    self.logger.error(e)
                    raise
            else:
                self.logger.info("Waiting")
                return None

        while True:
            execute_qry(qry_url, config)
            new_content = []
            time.sleep(.5)
            while not status_complete:
                status_complete = checkStatus(qry_status, result_id)
                if status_complete:
                    data = retrieveResults(qry_results, status_complete, result_id)
                    if data["return"]:
                        for event in data["return"]["rows"]:
                            for param_data in event["values"]:
                                event_location = event["values"].index(param_data)
                                event_parameter = data["return"]["columns"][event_location]["name"]
                                event_information[event_parameter] = param_data
                                if "Alert.AlertID"in event_information:
                                    eventID = str(event_information["Alert.AlertID"])
                                    if eventID not in contents:
                                        new_content.append(eventID)
                                        contents.append(eventID)
                                        self.send({"event_information":event_information})
            with komand.helper.open_cachefile(self.CACHE_FILE_NAME, append=True) as cache_file:
                for item in new_content:
                    cache_file.write(item + "\n")
            time.sleep(params.get("interval", 2))  # working logic for timeouts
            status_complete = False

    def test(self):
        # TODO: Implement test function
        return {}

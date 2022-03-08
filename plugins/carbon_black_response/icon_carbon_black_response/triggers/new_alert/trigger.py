import insightconnect_plugin_runtime
from .schema import NewAlertInput, NewAlertOutput

# Custom imports below
import time
from cbapi.response.models import Alert


class NewAlert(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="new_alert",
            description="Fires when a new alert is found",
            input=NewAlertInput(),
            output=NewAlertOutput(),
        )

    def run(self):
        """Run the trigger"""
        # TODO: this currently selects alerts that have happened in the past 5 minutes
        # TODO: since we don't have a good solution for distributed caching
        # TODO: at the moment, this is a best attempt.
        # TODO: potentially also want to use the cache_file to mark progress, but
        # TODO: again this will fail in HA
        five_minutes_secs = 5 * 60
        while True:
            try:
                alert_query = self.connection.carbon_black.select(Alert).where("created_time:-5m")
                for alert in alert_query:
                    new_alert = {
                        "alert_severity": alert.alert_severity,
                        "sensor_criticality": alert.sensor_criticality,
                        "hostname": alert.hostname,
                        "report_score": alert.report_score,
                        "feed_name": alert.feed_name,
                        "created_time": alert.created_time.isoformat(),
                        "os_type": alert.os_type,
                        "feed_rating": alert.feed_rating,
                        "ioc_confidence": alert.ioc_confidence,
                        "unique_id": alert.unique_id,
                        "md5": alert.md5,
                        "sensor_id": alert.sensor_id,
                        "feed_id": alert.feed_id,
                        "ioc_attr": alert.ioc_attr,
                        "status": alert.status,
                        "alert_type": alert.alert_type,
                    }

                    # If ioc_attr is blank it will return a {} else it returns a string
                    # This handles this issue, so we don't get an error
                    if new_alert["ioc_attr"] == {}:
                        new_alert["ioc_attr"] = ""

                    self.send({"alert": new_alert})
            except Exception as ex:
                self.logger.error("Failed to get alerts: %s", ex)
                raise ex

            # sleep for 5 minutes before getting the next results
            self.logger.info(f"Sleeping for {five_minutes_secs} seconds...")
            time.sleep(five_minutes_secs)

    def test(self):
        if self.connection.test():
            return {}

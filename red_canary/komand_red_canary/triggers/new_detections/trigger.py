import komand
import time
from .schema import NewDetectionsInput, NewDetectionsOutput

# Custom imports below
import maya
from komand_red_canary.util.cacher import load_cache, cache


class NewDetections(komand.Trigger):
    CACHE_FILE_NAME = "detection_cache_"

    def __init__(self):
        super(self.__class__, self).__init__(
            name="new_detections",
            description="Checks for new Detections",
            input=NewDetectionsInput(),
            output=NewDetectionsOutput(),
        )

    def run(self, params={}):

        force_offset = params.get("force_offset")

        date_offset = params.get("date_offset")

        self.logger.info("Date Offset: {} ".format(date_offset))

        # If date is left blank in the UI
        if date_offset == "0001-01-01T00:00:00Z":
            date_offset = None

        # Set date_offset to maya.MayaDT
        if date_offset:
            date_offset = maya.MayaDT.from_rfc3339(date_offset)

        # New cache util. Will return maya DT
        cache_file_name, cache_date = load_cache(
            self.CACHE_FILE_NAME,
            self.connection.customer_id,
            self.logger,
            force_offset,
            date_offset,
        )

        detection_date_list = []

        while True:
            try:

                detections = self.connection.api.get_detections(since=cache_date)

                self.logger.info("[*] Reviewing detection")
                for detection in detections:
                    detection_date = maya.MayaDT.from_rfc3339(
                        detection["attributes"]["time_of_occurrence"]
                    ).datetime()
                    if detection_date > cache_date:
                        detection_date_list.append(detection_date)
                        self.send({"detection": detection})

                # Set cache date to max its seen
                if detection_date_list:
                    max_date = max(detection_date_list)
                    self.logger.info(
                        f"[*] Checking if Max Date {max_date} > Current Cache Date {cache_date}"
                    )
                    if max_date > cache_date:
                        cache_date = max_date
                        cache(cache_file_name, cache_date, self.logger)

                # reset list
                detection_date_list = []

                time.sleep(params.get("frequency", 5))
            except Exception as e:
                raise Exception(
                    "An error occurred while reading detections: {}".format(e)
                )

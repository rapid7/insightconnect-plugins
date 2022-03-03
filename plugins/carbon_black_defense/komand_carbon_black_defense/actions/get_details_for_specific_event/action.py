import time
from datetime import datetime

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import GetDetailsForSpecificEventInput, GetDetailsForSpecificEventOutput, Input, Output


class GetDetailsForSpecificEvent(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_details_for_specific_event",
            description="Retrieve details for an individual event given the event ID",
            input=GetDetailsForSpecificEventInput(),
            output=GetDetailsForSpecificEventOutput(),
        )

    def run(self, params={}):

        event_id = params.get(Input.EVENT_IDS)
        if len(event_id) == 0:
            raise PluginException(
                cause="Error. No event IDs were provided as input.",
                assistance="Please enter at least one event ID.",
            )
        id_ = self.connection.get_job_id_for_detail_search(event_ids=event_id)
        self.logger.info(f"Got job ID for detail search: {id_}")
        if id_ is None:
            return {Output.SUCCESS: False, Output.EVENTINFO: {}}
        detail_search_status = self.connection.check_status_of_detail_search(id_)

        # check if status of
        # detail search is complete by checking if the completed property
        # in results is not equal to the contacted property
        t1 = datetime.now()
        for _ in range(0, 9999):
            if not detail_search_status:
                detail_search_status = self.connection.check_status_of_detail_search(id_)
                if (datetime.now() - t1).seconds > 60:
                    break
                time.sleep(3)
            else:
                break
        response = self.connection.retrieve_results_for_detail_search(job_id=id_)
        data = insightconnect_plugin_runtime.helper.clean(response)

        return {
            Output.SUCCESS: True,
            Output.EVENTINFO: data,
        }

import komand
from .schema import SearchInput, SearchOutput, Component, Input
# Custom imports below
from pyotrs import DynamicField
import maya
from datetime import datetime, timedelta


class Search(komand.Action):

    TIMEFRAME = {
        "week": datetime.utcnow() - timedelta(days=7)
    }

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search',
                description=Component.DESCRIPTION,
                input=SearchInput(),
                output=SearchOutput())

    def run(self, params={}):
        client = self.connection.client

        search_params = {}
        df = []
        try:
            client.session_create()
        except Exception as e:
            raise Exception("Unable to connect to OTRS webservice! Please check your connection information and \
            that you have properly configured OTRS webservice. Information on configuring the webservice can be found \
            in the Connection help")


        # Time search params
        # TODO: Add support for searching tickets with date

        #if params.get("date"):
        #    if params.get("date").startswith("0001-01-01"):
        #        del(params["date"])
        #    else:
        #        ticket_date = maya.MayaDT.rfc3339(params.get("date")).datetime()
        #        #search_params[""] = ticket_date

        # set queue
        if params.get("queue"):
            search_params["Queues"] = params.get("queue")

        # set customer id
        if params.get("cust_id"):
            search_params["CustomerID"] = params.get("cust_id")

        # set external search params
        external_params = params.get("external_params")
        if external_params:
            for param in external_params:
                for k, v in param.items():
                    search_params[k] = v

        # set dynamic fields
        dynamic_fields = params.get('dynamic_fields')
        if dynamic_fields:
            for field in dynamic_fields:
                df_payload = dict()
                df_payload["name"] = field.get("name")
                df_payload["value"] = field.get("value")
                df_payload["search_operator"] = field.get("operation", "Equals")
                df_payload["search_patterns"] = field.get("patterns")
                df.append(DynamicField(**df_payload))
            search_params["dynamic_fields"] = df

        tickets = client.ticket_search(**search_params)

        return {'ticket_ids': tickets}


import insightconnect_plugin_runtime
from .schema import GetAuditEventsInput, GetAuditEventsOutput, Input, Output, Component

# Custom imports below
from komand_mimecast.util.constants import DATA_FIELD, META_FIELD, PAGINATION_FIELD
from ...util.util import Utils


class GetAuditEvents(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_audit_events",
            description=Component.DESCRIPTION,
            input=GetAuditEventsInput(),
            output=GetAuditEventsOutput(),
        )

    def run(self, params={}):
        data = {}
        pagination = {}
        for key, value in params.get(Input.AUDIT_EVENTS_DATA).items():
            data.update(Utils.normalize(key, value))
        for key, value in params.get(Input.AUDIT_EVENTS_PAGINATION, {}).items():
            pagination.update(Utils.normalize(key, value))
        response = self.connection.client.get_audit_events(
            data=data,
            meta_data={PAGINATION_FIELD: pagination},
        )
        return {
            Output.RESPONSE: response.get(DATA_FIELD, []),
            Output.PAGINATION: response.get(META_FIELD, {}).get(PAGINATION_FIELD, {}),
        }

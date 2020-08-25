import komand
from .schema import GetRcaObjectInput, GetRcaObjectOutput, Input, Component
# Custom imports below
from ...util import util


class GetRcaObject(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_rca_object',
            description=Component.DESCRIPTION,
            input=GetRcaObjectInput(),
            output=GetRcaObjectOutput())

    def run(self, params={}):
        return self.connection.api.execute(
            "put",
            "/WebApp/OSCE_iES/OsceIes/ApiEntry",
            {
                "Url": "V1/Content/ShowContent",
                "TaskType": util.TaskType.value_of(params.get(Input.TASK_TYPE, util.DEFAULT_TASK_TYPE)),
                "TaskId": params.get(Input.TASK_ID),
                "ContentId": params.get(Input.CONTENT_ID),
                "TopN": params.get(Input.LIMIT)
            }
        )

import komand
from .schema import InsertOutput, InsertInput
# Custom imports below


class Insert(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='insert',
                description='Store an object into Dynamo',
                input=InsertInput(),
                output=InsertOutput())

    def run(self, params={}):
        table_name = params.get("table")
        expr = params.get("condition_expression")
        t = self.connection.dynamodb.Table(table_name)
        data = params.get("data")
        kwargs = {"Item": data}
        if (expr is not None) and (len(expr) > 0):
            kwargs["ConditionExpression"] = expr
        t.put_item(**kwargs)
        return {"success": True}

    def test(self):
        """TODO: Test action"""
        return {}

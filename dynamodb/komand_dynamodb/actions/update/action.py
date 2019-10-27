import komand
from .schema import UpdateInput, UpdateOutput
# Custom imports below


class Update(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='update',
                description='A full update of all fields in a  single object in Dynamo. Performs a read, updates the provided fields, then a full write back. Will fail if Dynamo rejects the update unless force is true',
                input=UpdateInput(),
                output=UpdateOutput())

    def run(self, params={}):
        pk = params.get("key")
        data = params.get("data")
        table_name = params.get("table")
        cond_expr = params.get("condition_expression")
        t = self.connection.dynamodb.Table(table_name)
        props = {}
        exp = "set "
        for key in data:
            pkey = ":" + key
            # Need to prep the data by prefixing the : so it meets the search api expectation
            props[pkey] = data[key]
            # Append to the expression
            exp += key + " = " + pkey + ","
        exp = exp[:-1] # Chop off the trailing comma
        kwargs = {
            "Key": pk,
            "UpdateExpression": exp,
            "ExpressionAttributeValues": props,
        }
        if (cond_expr is not None) and (len(cond_expr) > 0):
            kwargs["ConditionExpression"] = cond_expr

        t.update_item(**kwargs)
        return {"success":True}

    def test(self):
        """TODO: Test action"""
        return {}

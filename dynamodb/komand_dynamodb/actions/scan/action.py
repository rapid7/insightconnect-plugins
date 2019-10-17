import komand
from .schema import ScanInput, ScanOutput
# Custom imports below
from boto3.dynamodb.conditions import Attr


class Scan(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='scan',
                description='Scan Dynamo and return any objects found',
                input=ScanInput(),
                output=ScanOutput())

    def run(self, params={}):
        """TODO: Run action"""
        table_name = params.get("table")
        # Get the table ref
        t = self.connection.dynamodb.Table(table_name)
        # If they're using an index, slap it on there
        index = params.get("index")
        filter_exp = None
        if params.get("params"):
            args = params.get("params")  # I already regret naming them this
            for key in args:
                if filter_exp is None:
                    filter_exp = Attr(key).eq(args.get(key))
                else:
                    filter_exp = filter_exp & Attr(key).eq(args.get(key))
            kwargs = {"FilterExpression": filter_exp}
        else:
            kwargs = {}
        # Run the query, will raise an exception if something breaks
        
        if (index is not None) and (len(index) > 0):
            self.logger.info("Length: %s", len(index))
            kwargs["IndexName"] = index

        results = t.scan(**kwargs)
        return {
            "records": results['Items'],
            "count": results['Count'
            ],
        }

    def test(self):
        """TODO: Test action"""
        return {}

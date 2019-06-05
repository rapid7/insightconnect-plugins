import komand
from .schema import JsonToCsvInput, JsonToCsvOutput
# Custom imports below
import csv
import base64
from io import BytesIO


class JsonToCsv(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='json_to_csv',
                description='Convert a JSON array to CSV',
                input=JsonToCsvInput(),
                output=JsonToCsvOutput())

    def run(self, params={}):
        input_json = params.get("json")

        output = BytesIO()
        csv_writer = csv.writer(output)

        count = 0
        for l in input_json:
            if count is 0:
                header = l.keys()
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(l.values())

        resulting_csv = output.getvalue()

        encoded = base64.encodestring(resulting_csv)

        return {"csv": encoded}

    def test(self):
        return {"csv": ""}

import insightconnect_plugin_runtime
from .schema import JsonToCsvInput, JsonToCsvOutput, Input, Output, Component
# Custom imports below
import csv
import base64
from io import StringIO


class JsonToCsv(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='json_to_csv',
                description=Component.DESCRIPTION,
                input=JsonToCsvInput(),
                output=JsonToCsvOutput())

    def run(self, params={}):
        input_json = params.get(Input.JSON)

        output = StringIO()
        csv_writer = csv.writer(output)

        count = 0
        for entry in input_json:
            if count == 0:
                header = entry.keys()
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(entry.values())

        encoded = base64.encodebytes(output.getvalue().encode())

        return {Output.CSV: encoded.decode()}

import csv
from io import StringIO

def read_csv(csv_string):
    f = StringIO(csv_string)
    reader = csv.DictReader(f)

    fields = reader.fieldnames
    out_dict = []
    for row in reader:
        out_dict.append(row)

    return fields, out_dict


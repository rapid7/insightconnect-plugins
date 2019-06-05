from sqlalchemy_utils import analyze


def generate_results(conn_type, connection, query, parameters, logger):
    output = {}
    results = []
    operation = None
    rows_affected = None
    header = None

    if conn_type.lower() != "mssql":
        try:
            a = analyze(connection.session, query).plan
            logger.info(a)
            rows_affected = a["Plan Rows"]
            operation = a["Operation"]
        except KeyError:
            rows_affected = a["Plan Rows"]
            operation = 'unknown'
        except Exception as e:
            logger.info(e)
            operation = 'unknown'

    rows = connection.session.execute(query) if len(
        parameters) == 0 else connection.session.execute(query, parameters)
    if rows.is_insert or operation == "Insert":
        connection.session.commit()
        return {"status": "successfully inserted %d rows" % int(rows_affected)}
    if not rows.returns_rows:
        connection.session.commit()
        return {"status": "operation success"}

    output["status"] = "operation success"

    row_count = 0
    for i, row in enumerate(rows):
        if i == 0:
            header = row.keys()
            output["header"] = header
        if len(row) > 0:
            row_count += 1
            result_row = {}
            for j, col in enumerate(row.keys()):
                try:
                    v = str(row[col])
                except:
                    v = row[col]
                result_row[header[j]] = v
            results.append(result_row)
    output["results"] = results
    return output
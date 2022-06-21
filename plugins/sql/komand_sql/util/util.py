from sqlalchemy_utils import analyze


def generate_results(conn_type, connection, query, parameters, logger):
    output = {}
    results = []
    operation = None
    rows_affected = None
    header = None

    if conn_type.lower() != "mssql":
        analyze_response = {}
        try:
            analyze_response = analyze(connection.session, query).plan
            logger.info(analyze_response)
            rows_affected = analyze_response["Plan Rows"]
            operation = analyze_response["Operation"]
        except KeyError:
            if analyze_response.get("Plan Rows", default_value=False):
                rows_affected = analyze_response["Plan Rows"]
            else:
                rows_affected = 0
            operation = "unknown"
        except Exception as e:
            logger.info(e)
            operation = "unknown"

    if len(parameters) == 0:
        rows = connection.session.execute(query)
    else:
        rows = connection.session.execute(query, parameters)

    if rows.is_insert or operation == "Insert":
        connection.session.commit()
        return {"status": f"successfully inserted {rows_affected} rows."}

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
                except Exception:
                    v = row[col]
                result_row[header[j]] = v
            results.append(result_row)
    output["results"] = results
    return output

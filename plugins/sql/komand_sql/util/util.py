from insightconnect_plugin_runtime.exceptions import PluginException


def generate_results(connection, query, parameters, logger):  # noqa: MC0001
    output = {}
    results = []
    header = None

    try:
        if len(parameters) == 0:
            rows = connection.session.execute(query)
        else:
            rows = connection.session.execute(query, parameters)
        rows_affected = rows.rowcount

    except Exception as error:
        logger.error(f"Error executing query {query}. Error: {error}")
        return {"status": "error", "error": str(error)}

    if query.strip().lower().startswith(("insert", "update", "delete")):
        connection.session.commit()
        return {"status": f"Successfully affected {rows_affected} rows."}

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
                except PluginException:
                    v = row[col]
                result_row[header[j]] = v
            results.append(result_row)
    output["results"] = results
    return output

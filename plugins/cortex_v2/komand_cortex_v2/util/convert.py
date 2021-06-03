def report_to_dict(report):
    return report.json()


def analyzers_to_dicts(analyzers):
    return _convert_to_dicts(
        analyzers,
        ("id", "version", "dataTypeList", "name", "description", "license", "author", "url"),
    )


def job_to_dict(job, api):
    job = _convert_to_dict(job, ("status", "date", "id", "analyzerId"))
    job["artifacts"] = _artifacts_to_dicts(api.jobs.get_artifacts(job["id"]))
    return job


def jobs_to_dicts(jobs, api):
    return [job_to_dict(j, api) for j in jobs]


def _artifacts_to_dicts(artifacts):
    return _convert_to_dicts(artifacts, ("dataType", "data"))


def _convert_to_dicts(objects, keys):
    return [_convert_to_dict(o, keys) for o in objects]


def _convert_to_dict(object_, keys):
    return {key: getattr(object_, key) for key in keys}

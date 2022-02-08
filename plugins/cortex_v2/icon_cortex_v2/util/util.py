from typing import List, Dict


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


def filter_analyzers(analyzers: List[Dict]):
    return [filter_analyzer(analyzer) for analyzer in analyzers]


def filter_analyzer(analyzer: Dict):
    return {k: v for k, v in analyzer.items() if k in
            {"id", "version", "dataTypeList", "name", "description", "license", "author", "url"}}


def filter_jobs(jobs: List[Dict]):
    return [filter_job(job) for job in jobs]


def filter_job(job: Dict):
    return {k: v for k, v in job.items() if k in {"status", "date", "id", "analyzerId"}}


def filter_job_artifacts(artifacts: List[Dict]):
    return [filter_job_artifact(artifact) for artifact in artifacts]


def filter_job_artifact(artifact: Dict):
    return {k: v for k, v in artifact.items() if k in {"dataType", "data"}}


def eq_(field, value):
    # Based on https://github.com/TheHive-Project/Cortex4py/blob/2.1.0/cortex4py/query.py#L2
    return {"_field": field, "_value": value}


def and_(criteria):
    # Based on https://github.com/TheHive-Project/Cortex4py/blob/2.1.0/cortex4py/query.py#L22
    return {"_and": criteria}

from typing import List, Dict


def filter_analyzers(analyzers: List[Dict]):
    return [filter_analyzer(analyzer) for analyzer in analyzers]


def filter_analyzer(analyzer: Dict):
    return {
        k: v
        for k, v in analyzer.items()
        if k in {"id", "version", "dataTypeList", "name", "description", "license", "author", "url"}
    }


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

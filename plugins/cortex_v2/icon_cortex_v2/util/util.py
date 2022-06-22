from typing import List, Dict, Any


RELEVANT_ANALYZER_KEYS = {"id", "version", "dataTypeList", "name", "description", "license", "author", "url"}
RELEVANT_JOB_KEYS = {"status", "date", "id", "analyzerId"}
RELEVANT_JOB_ARTIFACT_KEYS = {"dataType", "data"}


def filter_analyzers(analyzers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [filter_analyzer(analyzer) for analyzer in analyzers]


def filter_analyzer(analyzer: Dict[str, Any]) -> Dict[str, Any]:
    return {key: value for key, value in analyzer.items() if key in RELEVANT_ANALYZER_KEYS}


def filter_jobs(jobs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [filter_job(job) for job in jobs]


def filter_job(job: Dict[str, Any]) -> Dict[str, Any]:
    return {key: value for key, value in job.items() if key in RELEVANT_JOB_KEYS}


def filter_job_artifacts(artifacts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [filter_job_artifact(artifact) for artifact in artifacts]


def filter_job_artifact(artifact: Dict[str, Any]) -> Dict[str, Any]:
    return {key: value for key, value in artifact.items() if key in RELEVANT_JOB_ARTIFACT_KEYS}


def eq_(field: Any, value: Any) -> Dict[str, Any]:
    # Based on https://github.com/TheHive-Project/Cortex4py/blob/2.1.0/cortex4py/query.py#L2
    return {"_field": field, "_value": value}


def and_(criteria: Any) -> Dict[str, Any]:
    # Based on https://github.com/TheHive-Project/Cortex4py/blob/2.1.0/cortex4py/query.py#L22
    return {"_and": criteria}

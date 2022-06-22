from typing import List, Dict, Any


def filter_analyzers(analyzers: List[Dict]) -> List[Dict]:
    return [filter_analyzer(analyzer) for analyzer in analyzers]


def filter_analyzer(analyzer: Dict) -> Dict:
    return {
        key: value
        for key, value in analyzer.items()
        if key in {"id", "version", "dataTypeList", "name", "description", "license", "author", "url"}
    }


def filter_jobs(jobs: List[Dict]) -> List[Dict]:
    return [filter_job(job) for job in jobs]


def filter_job(job: Dict) -> Dict:
    return {key: value for key, value in job.items() if key in {"status", "date", "id", "analyzerId"}}


def filter_job_artifacts(artifacts: List[Dict]) -> List[Dict]:
    return [filter_job_artifact(artifact) for artifact in artifacts]


def filter_job_artifact(artifact: Dict) -> Dict:
    return {key: value for key, value in artifact.items() if key in {"dataType", "data"}}


def eq_(field: Any, value: Any) -> Dict:
    # Based on https://github.com/TheHive-Project/Cortex4py/blob/2.1.0/cortex4py/query.py#L2
    return {"_field": field, "_value": value}


def and_(criteria: Any) -> Dict:
    # Based on https://github.com/TheHive-Project/Cortex4py/blob/2.1.0/cortex4py/query.py#L22
    return {"_and": criteria}

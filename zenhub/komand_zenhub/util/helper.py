def plus_one_to_json(plus_one):
    return {
        'user_id': plus_one.get('user_id', -1),
        'created_at': plus_one.get('created_at', '')
    }


def issue_data_to_json(issue, metadata={}):
    return {
        'issue_number': issue.get('issue_number', metadata.get('issue_number', -1)),
        'repo_id': issue.get('repo_id', metadata.get('repo_id', -1)),
        'is_epic': issue.get('is_epic', False),
        'position': issue.get('position', -1),
        'pipeline_name': issue.get('pipeline', {}).get('name', metadata.get('pipeline_name', '')),
        'estimate_value': issue.get('estimate', {}).get('value', -1),
        'plus_ones': list(map(plus_one_to_json, issue.get('plus_ones', [])))
    }


def issue_event_to_json(event):
    return {
        'user_id': event.get('user_id', -1),
        'type': event.get('type', ''),
        'created_at': event.get('created_at', ''),
        'from_pipeline_name': event.get('from_pipeline', {}).get('name', ''),
        'to_pipeline_name': event.get('to_pipeline', {}).get('name', ''),
        'from_estimate_value': event.get('from_estimate', {}).get('value', -1),
        'to_estimate_value': event.get('to_estimate', {}).get('value', -1)
    }


def pipeline_data_to_json(pipeline, metadata={}):
    pipeline_name = pipeline.get('name', '')
    metadata['pipeline_name'] = pipeline_name
    return {
        'pipeline_id': pipeline.get('id'),
        'pipeline_name': pipeline_name,
        'issues': list(map(
            lambda i: issue_data_to_json(i, metadata),
            pipeline.get('issues', [])
        ))
    }


def repository_data_to_json(repository, metadata={}):
    return {
        'pipelines': list(map(
            lambda p: pipeline_data_to_json(p, metadata),
            repository.get('pipelines', [])
        ))
    }


def issue_reference_to_json(issue):
    return {
        'repo_id': issue.get('repo_id', -1),
        'issue_number': issue.get('issue_number', -1),
        'issue_url': issue.get('issue_url', '')

    }


def epic_data_to_json(epic):
    return {
        'total_epic_estimates_value': epic.get('total_epic_estimates', {}).get('value', -1),
        'issues': list(map(issue_data_to_json, epic.get('issues', []))),
        'estimate_value': epic.get('estimate', {}).get('value', -1),
        'pipeline_name': epic.get('pipeline', {}).get('name', '')
    }

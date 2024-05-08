task_first_run = {}

task_first_run_output = {
    "last_alert_hashes": ["b78568edeb07d22535d7b06454a4ce89a6589768"],
    "last_alert_time": "2024-04-25T15:38:38.389Z",
    "last_observation_hashes": ["f1c41f48654ec39d4614a0e924b2a6b96fa9f32e"],
    "last_observation_time": "2024-04-25T15:39:38.389Z",
}

task_subsequent_output = {
    "last_alert_hashes": ["b78568edeb07d22535d7b06454a4ce89a6589768"],  # hash of last alert retrieved
    "last_alert_time": "2024-04-25T15:45:00.000000Z",  # now - 15 minutes as no new alerts returned
    "last_observation_hashes": ["c3fcde686f2fa6ed6b97b4f7f1b476dddfe19fab"],
    "last_observation_time": "2024-04-25T15:45:38.389Z",
}


task_subsequent_output_no_observation_job = {
    "last_alert_hashes": ["b78568edeb07d22535d7b06454a4ce89a6589768"],  # hash of last alert retrieved
    "last_alert_time": "2024-04-25T15:45:00.000000Z",  # now - 15 minutes as no new alerts returned
    "last_observation_hashes": ["f1c41f48654ec39d4614a0e924b2a6b96fa9f32e"],
    "last_observation_time": "2024-04-25T15:39:38.389Z",
}


observations_more_pages = {
    "last_alert_hashes": ["9bceab49bf5441923e8fe8345195d5ec4d270193"],
    "last_alert_time": "2024-04-25T15:50:38.389Z",
    "last_observation_hashes": ["c3fcde686f2fa6ed6b97b4f7f1b476dddfe19fab"],
    "last_observation_time": "2024-04-25T15:45:38.389Z",
}

observation_job_not_finished = {
    "last_alert_hashes": ["9bceab49bf5441923e8fe8345195d5ec4d270193"],
    "last_alert_time": "2024-04-25T15:50:38.389Z",
    "last_observation_hashes": ["f1c41f48654ec39d4614a0e924b2a6b96fa9f32e"],
    "last_observation_time": "2024-04-25T15:39:38.389Z",
    "last_observation_job": "1234-abcd-5678-sqs",
    "last_observation_job_time": "2024-04-25T16:00:00.000000Z",
}

task_rate_limit_getting_observations = {
    "last_alert_hashes": ["b78568edeb07d22535d7b06454a4ce89a6589768"],
    "last_alert_time": "2024-04-25T15:38:38.389Z",
    "last_observation_time": "2024-04-25T15:40:00.000000Z",  # time that the observation job queried until
    "last_observation_job": "1234-abcd-5678-sqs",
    "last_observation_job_time": "2024-04-25T16:00:00.000000Z",
    "rate_limited_until": "2024-04-25T16:05:00.000000Z",
}

task_401_on_second_request = {
    "last_alert_hashes": ["b78568edeb07d22535d7b06454a4ce89a6589768"],
    "last_alert_time": "2024-04-25T15:38:38.389Z",
    "last_observation_hashes": ["f1c41f48654ec39d4614a0e924b2a6b96fa9f32e"],
    "last_observation_time": "2024-04-25T15:39:38.389Z",
    "last_observation_job": "1234-abcd-5678-sqs",
    "last_observation_job_time": "2024-04-25T16:00:00.000000Z",
}


task_404_on_third_request = {
    "last_alert_hashes": ["9bceab49bf5441923e8fe8345195d5ec4d270193"],
    "last_alert_time": "2024-04-25T15:50:38.389Z",
    "last_observation_hashes": ["f1c41f48654ec39d4614a0e924b2a6b96fa9f32e"],
    "last_observation_time": "2024-04-25T15:39:38.389Z",
}

observation_job_exceeded = {
    "last_observation_job_time": "2024-04-01T13:34:03.626Z",
    "last_observation_time": "2024-04-01T15:39:00.000000Z",  # job created 20 minutes ago
    "last_observation_job": "example-job-id",
}

observation_job_not_finished_but_parsed = {
    "last_alert_hashes": ["b78568edeb07d22535d7b06454a4ce89a6589768"],
    "last_alert_time": "2024-04-25T15:38:38.389Z",
    "last_observation_hashes": ["f1c41f48654ec39d4614a0e924b2a6b96fa9f32e"],
    "last_observation_time": "2024-04-25T15:39:38.389Z",
}

# the same values for observations and hashes from the input as we don't get any new values, but add the
# new observation job details.
task_404_on_second_request = task_first_run_output.copy()
task_404_on_second_request["last_observation_job"] = "1234-abcd-5678-sqs"
task_404_on_second_request["last_observation_job_time"] = "2024-04-25T16:00:00.000000Z"

from requests import request, HTTPError
from komand.exceptions import ConnectionTestException
from komand.helper import clean
from json import JSONDecodeError


class HippocampeAPI:
    def __init__(self, instance_url, logger):
        self.logger = logger

        if not instance_url.endswith('/'):
            instance_url += '/'
        instance_url += 'hippocampe/api/v1.0/'
        self.instance_url = instance_url

    def distinct(self, intelligence_types):
        return self._call_api('POST', 'distinct', json={
            'field': intelligence_types
        })

    def freshness(self):
        raw_freshness = self._call_api('GET', 'freshness')

        freshness_statuses = []

        for feed, value in raw_freshness.items():
            value['feed'] = feed
            freshness_statuses.append(value)

        return freshness_statuses

    def hipposched(self, time):
        return self._call_api('POST', 'hipposched', json={'time': time})

    def hipposcore(self, observables):
        parsed_observables = {}

        for observable in observables:
            value = observable['value']
            type_ = observable['type']
            parsed_observables[value] = {'type': type_}

        raw_scores = self._call_api(
            'POST', 'hipposcore', json=parsed_observables
        )
        scores = []

        for observable, value in raw_scores.items():
            value['observable'] = observable
            value['hipposcore'] = float(value['hipposcore'])
            scores.append(value)

        return scores

    def jobs(self):
        raw_jobs = self._call_api('GET', 'jobs')
        jobs = []

        for job_id, job_dict in raw_jobs.items():
            job = {'id': job_id}
            if 'report' in job_dict:
                reports = []
                for filename, report_dict in job_dict['report'].items():
                    report = {'filename': filename}
                    report.update(report_dict)
                    reports.append(report)
                job_dict['reports'] = reports
                del job_dict['report']
            job.update(job_dict)
            jobs.append(job)

        return jobs

    def last_query(self):
        raw_last_queries = self._call_api('GET', 'lastQuery')
        last_queries = []

        for source, value in raw_last_queries.items():
            last_query = {'source': source}
            last_query['lastQuery'] = value['lastQuery']
            last_queries.append(last_query)

        return last_queries

    def last_status(self):
        raw_last_statuses = self._call_api('GET', 'lastStatus')
        last_statuses = []

        for source, value in raw_last_statuses.items():
            last_status = {'source': source}
            last_status['lastStatus'] = value['lastStatus']
            last_statuses.append(last_status)

        return last_statuses

    def monitor_sources(self):
        raw_monitor_results = self._call_api('GET', 'monitorSources')
        monitor_results = []

        for source, values in raw_monitor_results.items():
            monitor_result = {'source': source}
            monitor_result.update(values)
            monitor_results.append(monitor_result)

        return monitor_results

    def more(self, observables):
        parsed_observables = {}

        for observable in observables:
            value = observable['value']
            type_ = observable['type']
            parsed_observables[value] = {'type': type_}

        raw_results = self._call_api(
            'POST', 'more', json=parsed_observables
        )
        results = []

        for observable, values in raw_results.items():
            result = {'observable': observable}
            records = []
            for value in values:
                if 'hipposcore' in value:
                    value['hipposcore'] = float(
                        value['hipposcore']['hipposcore']
                    )
                records.append(value)
            result['records'] = records
            results.append(result)

        return results

    def new(self):
        raw_new_elements = self._call_api('GET', 'new')
        new_elements = []

        for id_, value in raw_new_elements.items():
            value['id'] = id_
            new_elements.append(value)

        return new_elements

    def sched_report(self):
        raw_launched_indexations = self._call_api('GET', 'schedReport')
        launched_indexations = []

        for source, value in raw_launched_indexations.items():
            value['source'] = source
            launched_indexations.append(value)

        return launched_indexations

    def shadowbook(self):
        raw_job = self._call_api('GET', 'shadowbook')
        source, status = next(iter(raw_job.items()))

        job = {
            'source': source,
            'status': status
        }

        return job

    def size_by_source(self):
        raw_sizes = self._call_api('GET', 'sizeBySources')
        sizes = []

        for source, value in raw_sizes.items():
            size = {'name': source, 'size': value['size']}
            sizes.append(size)

        return sizes

    def size_by_type(self):
        raw_sizes = self._call_api('GET', 'sizeByType')
        sizes = []

        for type_, value in raw_sizes.items():
            size = {'name': type_, 'size': value['size']}
            sizes.append(size)

        return sizes

    def sources(self):
        raw_sources = self._call_api('GET', 'sources')
        sources = []

        for source, value in raw_sources.items():
            value['source'] = source
            sources.append(value)

        return sources

    def type(self):
        types = self._call_api('GET', 'type')

        return types['type']

    def _call_api(self, method, url, data=None, json=None, params=None):
        api_url = self.instance_url + url

        kwargs = {'params': params, 'json': json, 'data': data}
        kwargs = clean(kwargs)

        self.logger.info('HippocampeAPI: Trying to reach endpoint: ' + api_url)

        response = request(method, api_url, **kwargs)

        try:
            response.raise_for_status()
        except HTTPError:
            if response.status_code == 401:
                raise ConnectionTestException(
                    preset=ConnectionTestException.Preset.API_KEY
                )
            elif response.status_code == 404:
                raise ConnectionTestException(
                    preset=ConnectionTestException.Preset.NOT_FOUND
                )
            else:
                cause = None

                try:
                    response_json = response.json()
                    # Only error returned, no actual data
                    if set(response_json.keys()) == {'error'}:
                        cause = response_json['error']
                except JSONDecodeError:
                    # Not a JSON response
                    cause = response.content.decode()

                if cause:
                    raise ConnectionTestException(
                        cause=cause,
                        assistance=(
                            'If the issue persists please contact support.'
                        )
                    )

        response = response.json()
        if response is None:
            self.logger.warn('HippocampeAPI: Received empty response')
            response = {}
        elif 'error' in response:
            error = response['error']
            self.logger.warn(
                'HippocampeAPI: An error occurred, but some '
                'data was returned successfully: ' + error
            )
            del response['error']
        self.logger.info('HippocampeAPI: API call successful')

        return response

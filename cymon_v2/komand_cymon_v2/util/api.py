from requests import request
import komand


class CymonV2:
    def __init__(self, username, password, logger):
        self.logger = logger
        self.token = None
        self.base_url = 'https://api.cymon.io/v2/'

        if username is None or password is None:
            logger.warn(
                'Cymon API V2 credentials were not provided (anonymous), '
                'some actions will not be available'
            )
        else:
            try:
                auth_info = self._call_api(
                    'POST', 'auth/login', json={
                        'username': username, 'password': password
                    }
                )
                self.token = auth_info['jwt']
                logger.info('Cymon API V2 authentication successful')
            except Exception as e:
                logger.warn('Failed to get auth token: {}'.format(e))

    def search(self, search_by, value, start_date, end_date):
        url = 'ioc/search/{}/{}'.format(search_by, value)

        return self._call_api('GET', url, 'hits', params={
            'start_date': start_date,
            'end_date': end_date,
        })

    def list_all_feeds(self, privacy):
        url = 'feeds'

        if privacy == 'all':
            privacy = None

        return self._call_api('GET', url, 'feeds', params={
            'privacy': privacy,
        })

    def list_user_feeds(self):
        url = 'feeds/me'

        return self._call_api('GET', url, 'feeds')

    def get_feed(self, feed_id):
        url = 'feeds/{}'.format(feed_id)

        return self._call_api('GET', url)

    def get_report(self, feed_id, report_id):
        url = 'feeds/{}/{}'.format(feed_id, report_id)

        return self._call_api('GET', url)

    def create_feed(
        self, name, description, link, tos, logo, privacy, tags, admins,
        members, guests
    ):
        url = 'feeds'

        json = {
            'name': name,
            'description': description,
            'link': link,
            'tos': tos,
            'logo': logo,
            'privacy': privacy,
            'tags': tags,
            'admins': admins,
            'members': members,
            'guests': guests,
        }
        json = komand.helper.clean(json)

        response = self._call_api('POST', url, json=json)
        message = response.get('message')
        if message == 'feed created':
            return response.get('feed')
        else:
            raise Exception('Could not create a feed; {}'.format(message))

    def update_feed(
        self, feed_id, description, link, tos, logo, privacy, tags, admins,
        members, guests
    ):
        url = 'feeds/{}'.format(feed_id)

        json = {
            'description': description,
            'link': link,
            'tos': tos,
            'logo': logo,
            'privacy': privacy,
            'tags': tags,
            'admins': admins,
            'members': members,
            'guests': guests,
        }
        json = komand.helper.clean(json)

        response = self._call_api('PUT', url, json=json)

        message = response.get('message')
        if message == 'feed updated':
            return response.get('feed')
        else:
            raise Exception('Could not update a feed; {}'.format(message))

    def submit_report(self, report):
        url = 'ioc/submit'

        report = komand.helper.clean(report)

        response = self._call_api('POST', url, json=report)
        message = response.get('message')
        if message == 'object created':
            return response.get('report')
        else:
            raise Exception('Could not create a report; {}'.format(message))

    def bulk_submit_reports(self, reports):
        url = 'ioc/submit/bulk'

        reports = komand.helper.clean(reports)

        response = self._call_api('POST', url, json=reports)
        message = response.get('message')
        if message == 'objects created':
            reports = response.get('reports')
            if not isinstance(reports, list):
                reports = [reports]
            return reports
        else:
            raise Exception('Could not create reports; {}'.format(message))

    def _call_api(
        self, method, url, multiple_results_field=None, params=None, json=None
    ):
        if params is None:
            params = {}

        api_url = self.base_url + url

        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        } if self.token else None

        try:
            if multiple_results_field:
                hits = []
                from_ = 0
                size = 100 if self.token else 10
                params['from'] = from_
                params['size'] = size

                while True:
                    response = request(
                        method, api_url, params=params, headers=headers
                    )
                    response.raise_for_status()

                    json_response = komand.helper.clean(response.json())
                    total = json_response.get('total', 0)
                    hits.extend(json_response[multiple_results_field])

                    if len(hits) >= total:
                        return hits
                    else:
                        params['from'] = params['from'] + size
            else:
                response = request(
                    method, api_url, params=params, json=json, headers=headers
                )
                response.raise_for_status()
                return komand.helper.clean(response.json())
        except Exception as e:
            raise Exception(
                'Failed to get a response from API endpoint {}: {}'.format(
                    api_url, e
                )
            )

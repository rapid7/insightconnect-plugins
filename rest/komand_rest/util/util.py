import requests


class Common:
    """Merge 2 dictionaries"""

    @staticmethod
    def merge_dicts(x, y):
        """Given two dicts, merge them into a new dict as a shallow copy."""
        z = x.copy()
        z.update(y)
        return z

    @staticmethod
    def copy_dict(x):
        """Copy the case insensitive headers dict to a normal one"""
        d = {}
        for key in x:
            d[key] = x[key]
        return d

    @staticmethod
    def send_request(method, route, headers, default_headers, base_url, ssl_verify, body=None, data=None):
        req_headers = Common.merge_dicts(default_headers, headers)
        url = requests.compat.urljoin(base_url, route)
        method_to_call = getattr(requests, method)
        response = method_to_call(url, headers=req_headers, json=body, verify=ssl_verify, data=data)
        body_object = {}
        try:
            body_object = response.json()
        except ValueError:
            """ Nothing? We don't care if it fails, that could be normal """

        resp_headers = Common.copy_dict(response.headers)
        return {
            'body_object': body_object,
            'response_text': response.text,
            'status_code': response.status_code,
            'resp_headers': resp_headers,
        }

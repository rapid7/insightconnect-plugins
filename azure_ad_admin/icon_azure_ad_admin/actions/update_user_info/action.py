import komand
from .schema import UpdateUserInfoInput, UpdateUserInfoOutput, Input, Output, Component
# Custom imports below
import requests
from komand.exceptions import PluginException


class UpdateUserInfo(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="update_user_info",
                description=Component.DESCRIPTION,
                input=UpdateUserInfoInput(),
                output=UpdateUserInfoOutput())

    def run(self, params={}):
        city = params.get(Input.CITY)
        country = params.get(Input.COUNTRY)
        dept = params.get(Input.DEPARTMENT)
        job_title = params.get(Input.JOB_TITLE)
        state = params.get(Input.STATE)
        user_id = params.get(Input.USER_ID)
        user_type = params.get(Input.USER_TYPE)
        payload = {}
        # only add value if its filled out so we dont null out an existing feild
        if city:
            payload["city"] = city
        if country:
            payload["country"] = country
        if country:
            payload["department"] = dept
        if job_title:
            payload["jobTitle"] = job_title
        if state:
            payload["state"] = state
        if user_type:
            payload["userType"] = user_type

        
        self.logger.info(f"Updating info for user: {user_id}")
        headers = self.connection.get_headers(self.connection.get_auth_token())
        endpoint = f"https://graph.microsoft.com/v1.0/users/{user_id}"
        result = requests.patch(endpoint, json=payload, headers=headers)

        if result.status_code not in range(200,209):
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=result.text)
            return {Output.SUCCESS: False}
        return {Output.SUCCESS: True}

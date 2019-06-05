import komand
from .schema import PostInput, PostOutput
# Custom imports below
import json
import urllib
import datetime
import ssl
import os
from ...util import utils
import requests


class Post(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="post",
                description="Post to pastebin",
                input=PostInput(),
                output=PostOutput())

    def run(self, params={}):
        r = requests.session()
        req_params = {"api_dev_key": self.connection.dev_key,
                      "api_option": "paste",
                      "api_paste_code": params.get("text")
                      }
        paste_private = params.get("paste_private", None)
        paste_expire_date = params.get("paste_expire_date", None)
        paste_name = params.get("paste_name", None)
        paste_format = params.get("paste_format", None)

        if paste_private is not None:
            req_params["api_paste_private"] = utils.privacy_dict.get(paste_private)
        if paste_expire_date is not None:
            req_params["api_paste_expire_date"] = utils.expire_dict.get(paste_expire_date)
        if paste_name is not None:
            req_params["api_paste_name"] = paste_name
        if paste_format is not None:
            req_params["api_paste_format"] = utils.format_dict.get(paste_format)

        try:
            request = r.post(self.connection.post_url, data=req_params)
        except Exception as e:
            self.logger.error("An error occurred while posting ", e)
            raise

        return_dict = dict()
        return_dict["url"] = request.content.decode()
        timestamp = datetime.datetime.utcnow()
        return_dict["timestamp"] = timestamp.isoformat("T") + "Z" # Time given in UTC
        return return_dict

    def test(self):
        if self.connection.user_key:
            return {"success": True}
        else:
            return {"success": False}

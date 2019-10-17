import komand
from .schema import MemberListInput, MemberListOutput
# Custom imports below
import json
import urllib
import urllib2
import requests_oauthlib
import requests


class MemberList(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='member_list',
                description='List members of organization',
                input=MemberListInput(),
                output=MemberListOutput())

    def run(self, params={}):
        try:
          self.logger.info('Params run: ',params)
          server  = self.connection.server
          api_key = self.connection.api_key
          token   = self.connection.token

          # Check and add parameter in dictionnary
          data = {}
          if params.get('actions', ""):
            data["actions"] = params.get('actions')
          
          if params.get('actions_entities', "") is not None:
            data["actions_entities"] = str(params.get('actions_entities')).lower()

          if params.get('actions_display', "") is not None:
            data["actions_display"] = str(params.get('actions_display')).lower()

          if params.get('actions_limit', "") and params.get('actions_limit') > 1000:
            data["actions_limit"] = 1000
          else:
            data["actions_limit"] = params.get('actions_limit')

          if params.get('action_fields', ""):
            data["action_fields"] = params.get('action_fields')

          if params.get('memberships', ""):
            data["memberships"] = params.get('memberships')

          if params.get('memberships_member', "") is not None:
            data["memberships_member"] = str(params.get('memberships_member')).lower()

          if params.get('memberships_member_fields', ""):
            data["memberships_member_fields"] = params.get('memberships_member_fields')

          if params.get('members', ""):
            data["members"] = params.get('members')

          if params.get('member_fields', ""):
            data["member_fields"] = params.get('member_fields')

          if params.get('member_activity', "") is not None:
            data["member_activity"] = str(params.get('member_activity')).lower()

          if params.get('membersInvited', ""):
            data["membersInvited"] = params.get('membersInvited')

          if params.get('membersInvited_fields', ""):
            data["membersInvited_fields"] = params.get('membersInvited_fields')

          if params.get('pluginData', "") is not None:
            data["pluginData"] = str(params.get('pluginData')).lower()

          if params.get('boards', ""):
            data["boards"] = params.get('boards')

          if params.get('board_fields', ""):
            data["board_fields"] = params.get('board_fields')

          if params.get('board_actions', ""):
            data["board_actions"] = params.get('board_actions')

          if params.get('board_actions_entities', "") is not None:
            data["board_actions_entities"] = str(params.get('board_actions_entities')).lower()

          if params.get('board_actions_display', "") is not None:
            data["board_actions_display"] = str(params.get('board_actions_display')).lower()

          if params.get('board_actions_format', ""):
            data["board_actions_format"] = params.get('board_actions_format')

          if params.get('board_actions_since', ""):
            data["board_actions_since"] = params.get('board_actions_since')

          if params.get('board_actions_limit', "") and params.get('board_actions_limit') > 1000:
            data["board_actions_limit"] =  1000
          else:
            data["board_actions_limit"] = params.get('board_actions_limit')

          if params.get('board_action_fields', ""):
            data["board_action_fields"] = params.get('board_action_fields')

          if params.get('board_lists', ""):
            data["board_lists"] = params.get('board_lists')

          if params.get('board_pluginData', "") is not None:
            data["board_pluginData"] = str(params.get('board_pluginData')).lower()

          if params.get('paid_account', "") is not None:
            data["paid_account"] = str(params.get('paid_account')).lower()

          if params.get('fields', ""):
            data["fields"] = params.get('fields')

          # add api key and token in query string

          data["key"] = api_key
          if token:
            data["token"] = token

          # encode data
          url_values = urllib.urlencode(data)
          url = server + '/organizations/' + params.get("id_or_name") + '?' + url_values
          resp = urllib2.urlopen(url)
          
          # handle decoding json
          try:
            result_dic = json.loads(resp.read())
          except ValueError as e:
            self.logger.error('Decoding JSON Errors:  %s', e)
            raise('Decoding JSON Errors')

          return result_dic
        # handle exception
        except urllib2.HTTPError as e:
          self.logger.error('HTTPError: %s for %s', str(e.code), url)
        except urllib2.URLError as e:
          self.logger.error('URLError: %s for %s', str(e.reason), url)
        except Exception:
          import traceback
          self.logger.error('Generic Exception: %s', traceback.format_exc())
        raise Exception('URL Request Failed')

    def test(self):
        http_method = "GET"
        id_or_name = "586e017aed11e154f287d464"
        api_key = '35cc663206a549a44b12a196e8e17554'
        token = '8342ebeaf475ca337bae562abaf68582ebb18f469659440e4199020d108bd46d'

        #  url test authentication
        url = 'https://api.trello.com/1/organizations/' + id_or_name

        # OAuth1 authentication
        oauth = requests_oauthlib.OAuth1(api_key, client_secret=None,
                              resource_owner_key=token, resource_owner_secret=None)

        # perform the HTTP requests, if possible uses OAuth authentication
        response = requests.request(http_method, url,
                                    headers={
                                        'Content-Type': 'application/json'},
                                    auth=oauth)

        if response.status_code == 401:
            raise Exception('Unauthorized: %s (HTTP status: %s)' % (response.text, response.status_code))
        if response.status_code != 200:
            raise Exception('%s (HTTP status: %s)' % (response.text, response.status_code))

        return {'status_code': response.status_code}

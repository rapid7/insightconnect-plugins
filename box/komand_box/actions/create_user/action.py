import komand
from .schema import CreateUserInput, CreateUserOutput
# Custom imports below


class CreateUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_user',
                description='Create user account',
                input=CreateUserInput(),
                output=CreateUserOutput())

    def run(self, params={}):
    
      client = self.connection.box_connection

      user_attributes = {}
      # (params_key, api_key)
      keys = [
          ('role', 'role'), ('sync', 'is_sync_enabled'), 
          ('phone', 'phone'), ('address', 'address'),
          ('space_amount', 'space_amount'), ('timezone', 'timezone'),
          ('two_factor', 'is_exempt_from_login_verification'),
          ('exempt_device', 'is_exempt_from_device_limits'), ('job_title', 'job_title')]

      for param_obj in keys:
        if params.get(param_obj[0]):
          user_attributes[param_obj[1]] = params.get(param_obj[0])
      self.logger.info(user_attributes)
      new_user = client.create_user(params.get('name'), login=params.get('login'), **user_attributes)
      self.logger.info(new_user._response_object)
      user_id = new_user._response_object.get('id')
      user_obj = {
          "address": new_user._response_object.get('address'),
          "avatar_url": new_user._response_object.get('avatar_url'),
          "exempt_device": params.get('exempt_device'),
          "id": new_user._response_object.get('id'),
          "job_title": new_user._response_object.get('job_title'),
          "login": new_user._response_object.get('login'),
          "name": new_user._response_object.get('name'),
          "phone": new_user._response_object.get('phone'),
          "space_amount": new_user._response_object.get('space_amount'),
          "sync": params.get('sync'),
          "timezone": new_user._response_object.get('timezone'),
          "two-factor": params.get('two_factor')
          }
      return user_obj
    
    def test(self):
      try:
        client = self.connection.box_connection
        return {'status': True }
      except:
        raise

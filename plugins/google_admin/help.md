# Description

[Gsuite](https://gsuite.google.com/) administrative functions allow you to manage users. The InsightConnect plugin can retrieve existing user details and suspend users as part of containment or deprovisioning workflows.

# Key Features

* Retrieve Gsuite user information
* Disable Gsuite users

# Requirements

* A JWT with administrative permissions
* API access to Gsuite administrative functions enabled

# Documentation

## Setup

To authenticate to Google admin, you will need to create a service account on your Google apps domain that is capable of delegation. See [https://developers.google.com/admin-sdk/directory/v1/guides/delegation](https://developers.google.com/admin-sdk/directory/v1/guides/delegation)

You will also need to modify Google apps security settings to allow for the following scopes on your service credentials:

* `https://www.googleapis.com/auth/admin.directory.user`
* `https://www.googleapis.com/auth/admin.directory.group`

To add these settings, from the Admin Home page navigate to Security > Advanced Settings > Manage API client access.
You'll need to provide the client ID and the above URL, comma separated.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|admin_user|string|None|True|Admin user to impersonate|None|admin@domain.com|
|auth_provider_x509_cert_url|string|https://www.googleapis.com/oauth2/v1/certs|True|OAUTH2 Auth Provider x509 Cert URL|None|https://www.googleapis.com/oauth2/v1/certs|
|auth_uri|string|https://accounts.google.com/o/oauth2/auth|True|OAUTH2 Auth URI|None|https://accounts.google.com/o/oauth2/auth|
|client_email|string|None|True|Client email from service credentials|None|user@example.com|
|client_id|string|None|True|Client ID|None|C03x4xfakeU4|
|client_x509_cert_url|string|None|True|x509 cert URL from service credentials|None|https://example.com|
|private_key|credential_asymmetric_key|None|True|Private Key from service credentials. This information is included with in the JSON file created when a new key is created|None|-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAjGnoUtfPHqvX3PIU6N9FKmwQ3Zl+NoaWb4yMLhudkdEBJ3Au +I8QdlqDKBm656UeOCh3r/i9e0ULKxkXDFfKmc3p2Wv+0lVOYGvxZFKUwKH0riAL A4imyYuL/fweOSGSnQlgYKr99HciTBIdL15SZ32TjYb+PDZBl+6zQsw2HYNJcqMj iciC7CAj6gB9SO8x1vMsRkU+rqKuc2r8Uk+qhECw8zR4K66wFuYM17sGUMXUq/pH WdiEvO3q/mdK47Nrx5i2baC7o5RXspKHYy6Xer4Vbnipl4DgAKkaNOL02a+Zv38Q l+xy9wdmWqUIbMiqSbj/k6xxDiPQkTR+/032eQIDAQABAoIBAEkPzpBUtPQbrJ3N 5S1rB71UL85u0OqkS2DNvB89xVabb0NLL1Wsc39yB271PHjORRQpkmWhQ08CFRae 3oxQnh47s+OrOxPMyZSIdjmicr5tRzjXeYOkNk0G7JgC+OL3YieOOnTyZGQxHUqB 3mfIZ45sHDv3MxC3lpfs35/xTHM8E/gW/gTfvU3QboQaL1q/taRQYEHvgiutwdZ0 sEFtJ8eAwOBABXiV3QPxnAQgIpwYpbicl3AK15gs5ENK4Rngi2bI7hdmMwDWa6t/ g0CP0TityFq05JUmnaz4wekXxD5EBm776EYNSoxTCaSzTMYwZCITrqXl6Y4/ogeT uVSm9ZECgYEA7G8CyyDKDTBYoIyEknJVKSwuelOA2edxmVyKL8hLoPiq1QoSH/N1 30nN/GVcvD7QED4p/u0XaMuPm2HVhuXwxu/t9j11DVlKP7QsH9u4pJKziw6NmV5N /9+mcjdWAH5BqaJtmpF0uoZsWk41JVe0fA7a3FCrXp1U/GD9BKSAD00CgYEAmAio ChEh7+pD7vutF85u+FqbdjY+KmyFeTPd2717P6i5V6C6lVpcnM7voZlGy0fjoald e9ntm0VU8FZkUIihKPzW9/LSAV8BgO+vSQrN/IMEmDqol959IxxI/6yzkY5JwYRP mlwoNzU0ekcHzg0eu7DA1uzRfv4F1NUW+QylRd0CgYEAzr07OhdP1jyCItD8U3n6 EWh6s6g0sVV5tdp/UszXpMgLyQFnW9ztIvRMU/jmIAzkrm9NFYaHw7DLv9jKd4y0 /59o+ro+kg+TpySKuMjOKcnFiUCOfJ9DoQwVZSYR45iDHivTnya1ZSyJrmVYf3Cz dw8ePSukzbTRTWYZmGenOrkCgYEAhoO6MdYAweXzH0J8XsDePEzmmcvaauzDl35F gIOAxc1B1381NqnRoUgSi1czZO6BP+q69LbX3PaV9WNqtDp+5OX4ST8FggMOMIdg /m5Z3F4LtajIvD41V9hR2i1yX4mWRmsLh1acmmQvvzSTekLvez8jD8ZOgV69yBaV kdsXa90CgYEAk+6ghpXNku12UANf9MH8loN+35/iPeeoqf0MY5FMVRYx10ZA91Lh ieAczVhiqzxCtHWhLA4SxE962eg+ji/awkS4kXLCMuZIESE+jFc7ptUmJjlsOWjv 8/dqUH5yjRKs2qxkBWG4HmT3Nx6A8sYIrUYxyqVLBpG8yKngbnaYPV4= -----END RSA PRIVATE KEY-----|
|private_key_id|string|None|True|Private Key ID from service credentials. This information is included with in the JSON file created when a new key is created|None|c2520f8c7df508adeca758313dd36b16507e3216|
|project_id|string|None|True|Project ID from service credentials. This is included with the JSON file|None|testing-api-189016|
|token_uri|string|https://accounts.google.com/o/oauth2/token|True|OAUTH2 Token URI|None|https://accounts.google.com/o/oauth2/token|
  
Example input:

```
{
  "admin_user": "admin@domain.com",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "client_email": "user@example.com",
  "client_id": "C03x4xfakeU4",
  "client_x509_cert_url": "https://example.com",
  "private_key": "-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAjGnoUtfPHqvX3PIU6N9FKmwQ3Zl+NoaWb4yMLhudkdEBJ3Au +I8QdlqDKBm656UeOCh3r/i9e0ULKxkXDFfKmc3p2Wv+0lVOYGvxZFKUwKH0riAL A4imyYuL/fweOSGSnQlgYKr99HciTBIdL15SZ32TjYb+PDZBl+6zQsw2HYNJcqMj iciC7CAj6gB9SO8x1vMsRkU+rqKuc2r8Uk+qhECw8zR4K66wFuYM17sGUMXUq/pH WdiEvO3q/mdK47Nrx5i2baC7o5RXspKHYy6Xer4Vbnipl4DgAKkaNOL02a+Zv38Q l+xy9wdmWqUIbMiqSbj/k6xxDiPQkTR+/032eQIDAQABAoIBAEkPzpBUtPQbrJ3N 5S1rB71UL85u0OqkS2DNvB89xVabb0NLL1Wsc39yB271PHjORRQpkmWhQ08CFRae 3oxQnh47s+OrOxPMyZSIdjmicr5tRzjXeYOkNk0G7JgC+OL3YieOOnTyZGQxHUqB 3mfIZ45sHDv3MxC3lpfs35/xTHM8E/gW/gTfvU3QboQaL1q/taRQYEHvgiutwdZ0 sEFtJ8eAwOBABXiV3QPxnAQgIpwYpbicl3AK15gs5ENK4Rngi2bI7hdmMwDWa6t/ g0CP0TityFq05JUmnaz4wekXxD5EBm776EYNSoxTCaSzTMYwZCITrqXl6Y4/ogeT uVSm9ZECgYEA7G8CyyDKDTBYoIyEknJVKSwuelOA2edxmVyKL8hLoPiq1QoSH/N1 30nN/GVcvD7QED4p/u0XaMuPm2HVhuXwxu/t9j11DVlKP7QsH9u4pJKziw6NmV5N /9+mcjdWAH5BqaJtmpF0uoZsWk41JVe0fA7a3FCrXp1U/GD9BKSAD00CgYEAmAio ChEh7+pD7vutF85u+FqbdjY+KmyFeTPd2717P6i5V6C6lVpcnM7voZlGy0fjoald e9ntm0VU8FZkUIihKPzW9/LSAV8BgO+vSQrN/IMEmDqol959IxxI/6yzkY5JwYRP mlwoNzU0ekcHzg0eu7DA1uzRfv4F1NUW+QylRd0CgYEAzr07OhdP1jyCItD8U3n6 EWh6s6g0sVV5tdp/UszXpMgLyQFnW9ztIvRMU/jmIAzkrm9NFYaHw7DLv9jKd4y0 /59o+ro+kg+TpySKuMjOKcnFiUCOfJ9DoQwVZSYR45iDHivTnya1ZSyJrmVYf3Cz dw8ePSukzbTRTWYZmGenOrkCgYEAhoO6MdYAweXzH0J8XsDePEzmmcvaauzDl35F gIOAxc1B1381NqnRoUgSi1czZO6BP+q69LbX3PaV9WNqtDp+5OX4ST8FggMOMIdg /m5Z3F4LtajIvD41V9hR2i1yX4mWRmsLh1acmmQvvzSTekLvez8jD8ZOgV69yBaV kdsXa90CgYEAk+6ghpXNku12UANf9MH8loN+35/iPeeoqf0MY5FMVRYx10ZA91Lh ieAczVhiqzxCtHWhLA4SxE962eg+ji/awkS4kXLCMuZIESE+jFc7ptUmJjlsOWjv 8/dqUH5yjRKs2qxkBWG4HmT3Nx6A8sYIrUYxyqVLBpG8yKngbnaYPV4= -----END RSA PRIVATE KEY-----",
  "private_key_id": "c2520f8c7df508adeca758313dd36b16507e3216",
  "project_id": "testing-api-189016",
  "token_uri": "https://accounts.google.com/o/oauth2/token"
}
```

## Technical Details

### Actions


#### Get User

This action is used to retrieve information about a user by their primary email address, unique ID, or alias email.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|user|string|None|True|The user's primary email address, unique ID, or alias email|None|user@example.com|
  
Example input:

```
{
  "user": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|found|boolean|False|True if found|True|
|user|user|False|User Response Returned|{'user': {'id': 'C03x4xfakeU4', 'customerId': 'C03x4xfakeU4', 'name': {'givenName': 'Example', 'familyName': 'User', 'fullName': 'Example User'}, 'isAdmin': True, 'isDelegatedAdmin': True, 'suspended': True, 'suspensionReason': '', 'emails': [{'address': 'user1@example.com', 'primary': True}, {'address': 'user2@example.com', 'primary': True}], 'alias': ['alias'], 'changePasswordAtNextLogin': False, 'ipWhitelisted': True, 'agreedToTerms': True, 'lastLoginTime': '03/10/2023', 'creationTime': '03/10/2020'}}|
  
Example output:

```
{
  "found": true,
  "user": {
    "user": {
      "agreedToTerms": true,
      "alias": [
        "alias"
      ],
      "changePasswordAtNextLogin": false,
      "creationTime": "03/10/2020",
      "customerId": "C03x4xfakeU4",
      "emails": [
        {
          "address": "user1@example.com",
          "primary": true
        },
        {
          "address": "user2@example.com",
          "primary": true
        }
      ],
      "id": "C03x4xfakeU4",
      "ipWhitelisted": true,
      "isAdmin": true,
      "isDelegatedAdmin": true,
      "lastLoginTime": "03/10/2023",
      "name": {
        "familyName": "User",
        "fullName": "Example User",
        "givenName": "Example"
      },
      "suspended": true,
      "suspensionReason": ""
    }
  }
}
```

#### Suspend User
  
Suspend a User

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|user|string|None|True|The user's primary email address, unique ID, or alias email|None|user@example.com|
  
Example input:

```
{
  "user": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|user|user|False|User Response Returned|{'user': {'id': 'C03x4xfakeU4', 'customerId': 'C03x4xfakeU4', 'name': {'givenName': 'Example', 'familyName': 'User', 'fullName': 'Example User'}, 'isAdmin': True, 'isDelegatedAdmin': True, 'suspended': True, 'suspensionReason': '', 'emails': [{'address': 'user1@example.com', 'primary': True}, {'address': 'user2@example.com', 'primary': True}], 'alias': ['alias'], 'changePasswordAtNextLogin': False, 'ipWhitelisted': True, 'agreedToTerms': True, 'lastLoginTime': '03/10/2023', 'creationTime': '03/10/2020'}}|
  
Example output:

```
{
  "user": {
    "user": {
      "agreedToTerms": true,
      "alias": [
        "alias"
      ],
      "changePasswordAtNextLogin": false,
      "creationTime": "03/10/2020",
      "customerId": "C03x4xfakeU4",
      "emails": [
        {
          "address": "user1@example.com",
          "primary": true
        },
        {
          "address": "user2@example.com",
          "primary": true
        }
      ],
      "id": "C03x4xfakeU4",
      "ipWhitelisted": true,
      "isAdmin": true,
      "isDelegatedAdmin": true,
      "lastLoginTime": "03/10/2023",
      "name": {
        "familyName": "User",
        "fullName": "Example User",
        "givenName": "Example"
      },
      "suspended": true,
      "suspensionReason": ""
    }
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*

### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**email**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Address|string|None|None|Email address|user@example.com|
|Primary|boolean|None|None|True if primary email|True|
  
**name**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Family Name|string|None|None|family name|User|
|Full Name|string|None|None|Full name|Example User|
|Given Name|string|None|None|given name|Example|
  
**user**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Agreed to Terms of Service|boolean|None|None|true if agreed to tos|None|
|Aliases|[]string|None|None|aliases|['alias']|
|Change Password at Next Login|boolean|None|None|True if must change password at login|False|
|Creation Time|date|None|None|creation time|03/10/2020|
|Customer ID|string|None|None|customer id|C03x4xfakeU4|
|Emails|[]email|None|None|emails|[{'user1@example.com': None, True: None}, {'user2@example.com': None, False: None}]|
|ID|string|None|None|user id|C03x4xfakeU4|
|IP Whitelisted|boolean|None|None|true if ip whitelisted|None|
|Is Admin|boolean|None|None|true if admin|True|
|Is Delegated Admin|boolean|None|None|true if delegated admin|True|
|Last Login Time|date|None|None|last login time|03/10/2023|
|Name|name|None|None|name|{'givenName': 'Example', 'familyName': 'User', 'fullName': 'Example User'}|
|Suspended|boolean|None|None|true if suspended|False|
|Suspension Reason|string|None|None|suspension reason|None|


## Troubleshooting
  
*There is no troubleshooting for this plugin.*

# Version History

* 1.0.4 - Updated `httplib2` to version `0.19.0` | Added examples to help.md
* 1.0.3 - New spec and help.md format for the Extension Library
* 1.0.2 - Fix typo in plugin spec
* 1.0.1 - Update to connection and troubleshooting documentation
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links


## References

* [Google Admin API](https://developers.google.com/admin-sdk)

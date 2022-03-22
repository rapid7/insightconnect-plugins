# Description

Google Directory lets you perform administrative operations on users, groups, organizational units, and devices in your account.
The Google Directory plugin allows you to list all users, suspend and unsuspend users.

# Key Features

* Suspend and unsuspend users
* List all users

# Requirements

* A JWT with administrative permissions
* Admin SDK API must be enabled

# Supported Product Versions

_There are no supported product versions listed._

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|admin_user|string|None|True|Admin user to impersonate|None|user@example.com|
|auth_provider_x509_cert_url|string|https://www.googleapis.com/oauth2/v1/certs|True|OAUTH2 Auth Provider x509 Cert URL|None|https://www.googleapis.com/oauth2/v1/certs|
|auth_uri|string|https://accounts.google.com/o/oauth2/auth|True|OAUTH2 Auth URI|None|https://accounts.google.com/o/oauth2/auth|
|client_email|string|None|True|Client email from service credentials|None|user@example.com|
|client_id|string|None|True|Client ID|None|102790495738029996994|
|client_x509_cert_url|string|None|True|x509 cert URL from service credentials|None|https://www.googleapis.com/robot/v1/metadata/x509/user@example.com|
|oauth_scope|string|https://www.googleapis.com/auth/admin.directory.user|True|Google Admin Directory OAuth scope to use for the connection, note that read only will result in some actions not working.|['https://www.googleapis.com/auth/admin.directory.user', 'https://www.googleapis.com/auth/admin.directory.user.readonly']|https://www.googleapis.com/auth/admin.directory.user|
|private_key|credential_asymmetric_key|None|True|Private Key from service credentials|None|-----BEGIN PRIVATE KEY-----\nMIIEpQIBAAKCAQEAjGnoUtfPHqvX3PIU6N9FKmwQ3Zl+NoaWb4yMLhudkdEBJ3Au\n+I8QdlqDKBm656UeOCh3r/i9e0ULKxkXDFfKmc3p2Wv+0lVOYGvxZFKUwKH0riAL\nA4imyYuL/fweOSGSnQlgYKr99HciTBIdL15SZ32TjYb+PDZBl+6zQsw2HYNJcqMj\niciC7CAj6gB9SO8x1vMsRkU+rqKuc2r8Uk+qhECw8zR4K66wFuYM17sGUMXUq/pH\nWdiEvO3q/mdK47Nrx5i2baC7o5RXspKHYy6Xer4Vbnipl4DgAKkaNOL02a+Zv38Q\nl+xy9wdmWqUIbMiqSbj/k6xxDiPQkTR+/032eQIDAQABAoIBAEkPzpBUtPQbrJ3N\n5S1rB71UL85u0OqkS2DNvB89xVabb0NLL1Wsc39yB271PHjORRQpkmWhQ08CFRae\n3oxQnh47s+OrOxPMyZSIdjmicr5tRzjXeYOkNk0G7JgC+OL3YieOOnTyZGQxHUqB\n3mfIZ45sHDv3MxC3lpfs35/xTHM8E/gW/gTfvU3QboQaL1q/taRQYEHvgiutwdZ0\nsEFtJ8eAwOBABXiV3QPxnAQgIpwYpbicl3AK15gs5ENK4Rngi2bI7hdmMwDWa6t/\ng0CP0TityFq05JUmnaz4wekXxD5EBm776EYNSoxTCaSzTMYwZCITrqXl6Y4/ogeT\nuVSm9ZECgYEA7G8CyyDKDTBYoIyEknJVKSwuelOA2edxmVyKL8hLoPiq1QoSH/N1\n30nN/GVcvD7QED4p/u0XaMuPm2HVhuXwxu/t9j11DVlKP7QsH9u4pJKziw6NmV5N\n/9+mcjdWAH5BqaJtmpF0uoZsWk41JVe0fA7a3FCrXp1U/GD9BKSAD00CgYEAmAio\nChEh7+pD7vutF85u+FqbdjY+KmyFeTPd2717P6i5V6C6lVpcnM7voZlGy0fjoald\ne9ntm0VU8FZkUIihKPzW9/LSAV8BgO+vSQrN/IMEmDqol959IxxI/6yzkY5JwYRP\nmlwoNzU0ekcHzg0eu7DA1uzRfv4F1NUW+QylRd0CgYEAzr07OhdP1jyCItD8U3n6\nEWh6s6g0sVV5tdp/UszXpMgLyQFnW9ztIvRMU/jmIAzkrm9NFYaHw7DLv9jKd4y0\n/59o+ro+kg+TpySKuMjOKcnFiUCOfJ9DoQwVZSYR45iDHivTnya1ZSyJrmVYfCz\ndw8ePSukzbTRTWYZmGenOrkCgYEAhoO6MdYAweXzH0J8XsDePEzmmcvaauzDl35F\ngIOAxc1B1381NqnRoUgSi1czZO6BP+q69LbX3PaV9WNqtDp+5OX4ST8FggMOMIdg\n/m5Z3F4LtajIvD41V9hR2i1yX4mWRmsLh1acmmQvvzSTekLvez8jD8ZOgV69yBaV\nkdsXa90CgYEAk+6ghpXNku12UANf9MH8loN+35/iPeeoqf0MY5FMVRYx10ZA91Lh\nieAczVhiqzxCtHWhLA4SxE962eg+ji/awkS4kXLCMuZIESE+jFc7ptUmJjlsOWjv\n8/dqUH5yjRKs2qxkBWG4HmT3Nx6A8sYIrUYxyqVLBpG8yKngbnaYPV4=\n-----END PRIVATE KEY-----
|
|private_key_id|string|None|True|Private Key ID from service credentials|None|02699626f388ed830012e5b787640e71c56d42d8|
|project_id|string|None|True|Project ID from service credentials|None|test_project|
|token_uri|string|https://oauth2.googleapis.com/token|True|OAUTH2 Token URI|None|https://oauth2.googleapis.com/token|

Example input:

```
{
  "admin_user": "user@example.com",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "client_email": "user@example.com",
  "client_id": 102790495738030000000,
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/user@example.com",
  "oauth_scope": "https://www.googleapis.com/auth/admin.directory.user",
  "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEpQIBAAKCAQEAjGnoUtfPHqvX3PIU6N9FKmwQ3Zl+NoaWb4yMLhudkdEBJ3Au\\n+I8QdlqDKBm656UeOCh3r/i9e0ULKxkXDFfKmc3p2Wv+0lVOYGvxZFKUwKH0riAL\\nA4imyYuL/fweOSGSnQlgYKr99HciTBIdL15SZ32TjYb+PDZBl+6zQsw2HYNJcqMj\\niciC7CAj6gB9SO8x1vMsRkU+rqKuc2r8Uk+qhECw8zR4K66wFuYM17sGUMXUq/pH\\nWdiEvO3q/mdK47Nrx5i2baC7o5RXspKHYy6Xer4Vbnipl4DgAKkaNOL02a+Zv38Q\\nl+xy9wdmWqUIbMiqSbj/k6xxDiPQkTR+/032eQIDAQABAoIBAEkPzpBUtPQbrJ3N\\n5S1rB71UL85u0OqkS2DNvB89xVabb0NLL1Wsc39yB271PHjORRQpkmWhQ08CFRae\\n3oxQnh47s+OrOxPMyZSIdjmicr5tRzjXeYOkNk0G7JgC+OL3YieOOnTyZGQxHUqB\\n3mfIZ45sHDv3MxC3lpfs35/xTHM8E/gW/gTfvU3QboQaL1q/taRQYEHvgiutwdZ0\\nsEFtJ8eAwOBABXiV3QPxnAQgIpwYpbicl3AK15gs5ENK4Rngi2bI7hdmMwDWa6t/\\ng0CP0TityFq05JUmnaz4wekXxD5EBm776EYNSoxTCaSzTMYwZCITrqXl6Y4/ogeT\\nuVSm9ZECgYEA7G8CyyDKDTBYoIyEknJVKSwuelOA2edxmVyKL8hLoPiq1QoSH/N1\\n30nN/GVcvD7QED4p/u0XaMuPm2HVhuXwxu/t9j11DVlKP7QsH9u4pJKziw6NmV5N\\n/9+mcjdWAH5BqaJtmpF0uoZsWk41JVe0fA7a3FCrXp1U/GD9BKSAD00CgYEAmAio\\nChEh7+pD7vutF85u+FqbdjY+KmyFeTPd2717P6i5V6C6lVpcnM7voZlGy0fjoald\\ne9ntm0VU8FZkUIihKPzW9/LSAV8BgO+vSQrN/IMEmDqol959IxxI/6yzkY5JwYRP\\nmlwoNzU0ekcHzg0eu7DA1uzRfv4F1NUW+QylRd0CgYEAzr07OhdP1jyCItD8U3n6\\nEWh6s6g0sVV5tdp/UszXpMgLyQFnW9ztIvRMU/jmIAzkrm9NFYaHw7DLv9jKd4y0\\n/59o+ro+kg+TpySKuMjOKcnFiUCOfJ9DoQwVZSYR45iDHivTnya1ZSyJrmVYfCz\\ndw8ePSukzbTRTWYZmGenOrkCgYEAhoO6MdYAweXzH0J8XsDePEzmmcvaauzDl35F\\ngIOAxc1B1381NqnRoUgSi1czZO6BP+q69LbX3PaV9WNqtDp+5OX4ST8FggMOMIdg\\n/m5Z3F4LtajIvD41V9hR2i1yX4mWRmsLh1acmmQvvzSTekLvez8jD8ZOgV69yBaV\\nkdsXa90CgYEAk+6ghpXNku12UANf9MH8loN+35/iPeeoqf0MY5FMVRYx10ZA91Lh\\nieAczVhiqzxCtHWhLA4SxE962eg+ji/awkS4kXLCMuZIESE+jFc7ptUmJjlsOWjv\\n8/dqUH5yjRKs2qxkBWG4HmT3Nx6A8sYIrUYxyqVLBpG8yKngbnaYPV4=\\n-----END PRIVATE KEY-----\n",
  "private_key_id": "3395856ce81f2b7382dee72602f798b642f14140",
  "project_id": "test_project",
  "token_uri": "https://oauth2.googleapis.com/token"
}
```

## Technical Details

### Actions

#### Get All Domain Users

This action is used to get all domain users.

Requires the following OAuth scope:

* https://www.googleapis.com/auth/admin.directory.user

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|domain|string|None|True|Domain to retrieve users from|None|example.com|

Example input:

```
{
  "domain": "example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|users|[]user|True|Users in the domain|

Example output:

```

{
  "users": [{
      "email": "user@example.com",
      "name": "Joe Tester"
  }, {
      "email": "user@example.com",
      "name": "Bob Testerson"
  }]
}

```

#### Suspend User

This action is used to suspend a user account.

Requires the following OAuth scope:

* https://www.googleapis.com/auth/admin.directory.user

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|email|string|None|True|Email of user to suspend|None|user@example.com|

Example input:

```
{
  "email": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Whether or not the suspend was successful|

Example output:

```

{
  "success": true
}

```

#### Unsuspend User

This action is used to unsuspend a user account.

Requires the following OAuth scope:

* https://www.googleapis.com/auth/admin.directory.user

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|email|string|None|True|Email of user to unsuspend|None|user@example.com|

Example input:

```
{
  "email": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Whether or not the unsuspend was successful|

Example output:

```

{
  "success": true
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.0.2 - Add required OAuth scope for actions in help.md | Code refactor | Add input examples
* 2.0.1 - New spec and help.md format for the Extension Library
* 2.0.0 - Update connection to add support for the read-only Google Admin Directory OAuth scope
* 1.2.1 - Fix typo in plugin spec
* 1.2.0 - Add pagination to Get All Domain Users actions to support domains with 500+ users
* 1.1.0 - Add actions: suspend user, unsuspend user
* 1.0.0 - Initial plugin

# Links

## References

* [Directory API](https://developers.google.com/admin-sdk/directory/)


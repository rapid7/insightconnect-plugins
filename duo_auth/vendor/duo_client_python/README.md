# Overview

[![Build Status](https://travis-ci.org/duosecurity/duo_client_python.svg?branch=master)](https://travis-ci.org/duosecurity/duo_client_python)

**Auth** - https://www.duosecurity.com/docs/authapi

**Admin** - https://www.duosecurity.com/docs/adminapi

**Accounts** - https://www.duosecurity.com/docs/accountsapi

# Installing

Development:

```
$ git clone https://github.com/duosecurity/duo_client_python.git
$ cd duo_client_python
$ pip install --requirement requirements.txt
$ pip install --requirement requirements-dev.txt
```

System:

```
$ pip install duo_client
```

# Using

See the `examples` folder for how to use this library.

# Testing

```
$ nose2
```

# Linting

```
$ flake8 --ignore=E501 duo_client/ tests/
```

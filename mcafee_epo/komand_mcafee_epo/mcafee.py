# Copyright (C) 2009-2013 McAfee, Inc.  All Rights Reserved.
import httplib
import json
import logging
import mimetools, mimetypes
import socket
import ssl
import sys
import urllib, urllib2
from urllib2 import HTTPError, URLError, Request
from urlquote import quote

#
# CREATE_LOG_FILE is a flag to determine whether or not to create a log file
# The default is False.  For debugging purposes it may be helpful to
# set CREATE_LOG_FILE = True and set the appropriate LOGGING_LEVEL.
#
CREATE_LOG_FILE = False

#
# LOG_FILE specifies the name of the generated log file
#
LOG_FILE = 'pyclient.log'

#
# LOGGING_LEVEL is a global setting controlling the verbosity of 
# logging messages.
# You can choose to set it one of the logging levels:
#
#   logging.CRITICAL
#   logging.ERROR
#   logging.WARN
#   logging.INFO
#   logging.DEBUG
#
# The default is logging.INFO.
#
# The following describes what is output from this script for each of
# the logging levels.
#
# CRITICAL messages are currently not generated from this script.
#
# ERROR messages include all of the lower level log messages and generate
# additional messages if there is a significant error, ie unable to 
# connect to the server or passing invalid arguments to a command.
#
# WARN messages include all of the lower level log messages, plus messages
# generated messages if for instance there was a call to a non-existent
# command.  It would also log an attempt to invalidly use the client object (ie, 
# call a _PyFeature as a function, that is client.core() ). 
#
# INFO messages include all of the lower level log messages, plus log the 
# requests sent to the server, that is the full request URL plus any POSTed
# data.  The security token retrieved from the server is logged.
#
# DEBUG messages include all of the lower level log messages, plus the raw server
# response for each request. It also includes requests for core.get securityToken.
# This has the potential to generate large log files.
#
# Basic auth credentials (user/pass) are never logged at any logging level.
#
LOGGING_LEVEL = logging.INFO


# Create logger (and hence a log file) ONLY if specifically requested.
# 
# We need to guard the creation of a logger/log file with a flag. Without 
# this guard, a log file will be created whether there are 
# log messages generated or not. We don't want to leave log files
# laying around when we don't want them.
logger = None
if CREATE_LOG_FILE:
    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=LOGGING_LEVEL,
                    format=FORMAT,
                    filename=LOG_FILE)
    logger = logging.getLogger('pyclient')


def log(log_level, msg):
    "Helper function to log message(s) if logging is enabled"
    if logger is not None: logger.log(log_level, msg)

def log_and_raise_error(log_level, msg, code=0):
    "Helper function to log and raise error"
    log(log_level, msg)
    raise CommandInvokerError(code, msg)


_UTF8='utf-8'

# We have to build the multi-part/file upload from scratch
# since python doesn't have it built in.
_ENCODE_TEMPLATE= """--%(boundary)s
Content-Disposition: form-data; name="%(name)s"

%(value)s
""".replace('\n','\r\n')

_ENCODE_TEMPLATE_FILE = """--%(boundary)s
Content-Disposition: form-data; name="%(name)s"; filename="%(filename)s"
Content-Type: %(contenttype)s

%(value)s
""".replace('\n','\r\n')

def _get_content_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'

def _encode_multipart_formdata(fields):
    """
    Given a dictionary field parameters, returns the HTTP request body and the
    content_type (which includes the boundary string), to be used with an
    httplib-like call.

    Normal key/value items are treated as regular parameters, but key/tuple
    items are treated as files, where a value tuple is a (filename, data) tuple.

    For example:

    fields = {
        'foo': 'bar',
        'foofile': ('foofile.txt', 'contents of foofile'),
    }

    body, content_type = _encode_multipart_formdata(fields)
    """

    BOUNDARY = '--' + mimetools.choose_boundary()

    body = ''

    for key, value in fields.iteritems():
        if isinstance(value, tuple):
            filename = value[0]
            content = value[1]
            body += _ENCODE_TEMPLATE_FILE % {
                        'boundary': BOUNDARY,
                        'name': str(key),
                        'value': str(content),
                        'filename': str(filename),
                        'contenttype': str(_get_content_type(filename))
                    }
        else:
            body += _ENCODE_TEMPLATE % {
                        'boundary': BOUNDARY,
                        'name': str(key),
                        'value': str(value)
                    }

    body += '--%s--\n\r' % BOUNDARY
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY

    return body, content_type

class ExHTTPSConnection(httplib.HTTPSConnection):
    def __init__(self, *args, **kwargs):
        httplib.HTTPSConnection.__init__(self, *args, **kwargs)

    # Override httplib.HTTPSConnection.connect()
    def connect(self):
        sock = socket.create_connection((self.host, self.port),
            self.timeout, self.source_address)
        if self._tunnel_host:
            self.sock = sock
            self._tunnel()
        self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, ciphers='DEFAULT:!DH')

"""
Using a custom handler to exclude some ciphers. Python 2.x does not always handle
these correctly and may result in a connection error similar to the following:

    CommandInvokerError: Failed to reach the server servername:8443. Error/reason:
    <urlopen error [Errno 1] _ssl.c:480: error:14094410:SSL routines:SSL3_READ_BYTES:
    sslv3 alert handshake failure>

This has been fixed in Python 3.3: http://bugs.python.org/issue13626
"""
class ExHTTPSHandler(urllib2.HTTPSHandler):
    def https_open(self, req):
        return self.do_open(ExHTTPSConnection, req)

"""
We create our own exception and override __str__ so we can use a unicode string
Python 2.6 can't handle unicode strings in Exceptions

See http://bugs.python.org/issue2517
"""
class CommandInvokerError(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

    def __str__(self):
        return self.msg


class _CommandInvoker(object):
    """Handles processing of a remote command request.
    This class is only intended for use inside this script (private)
    """

    def __init__(self, host, port, username, password, protocol, output, display):
        """
        Initializes the invoker by setting up basic authentication with given parameters.
        
        @param host - the servers name (string)
        @param port - the port to connect to on host (string)
        @param username - the username (string)
        @param password - the username's password (string)
        @param protocol - the protocol to use ('http','https')
        @param output - the requested output type from the server: one of ('terse','verbose','json','xml')
        the default is 'json'.  terse and verbose outputs are in a human readable form.
        @param display - when output is 'terse' or 'verbose', determines what happens with the response
        returned from the server.  If display is False only return the value or if display is True 'print' the value.
        """
        #The following should be tuples not lists, because they
        #are constants, however jython does not have an index method
        #on a tuple (python does), hence they are lists to be compatible
        #with both
        self.outputs = ['terse', 'verbose', 'json', 'xml']
        self.protocols = ['https', 'http']
        self.host = host
        self.port = str(port)

        #sanity checks
        try:
            self.protocols.index(protocol)
            self.protocol = protocol
        except:
            log_and_raise_error(logging.ERROR, 'Unsupported protocol: ' + protocol)

        try:
            self.outputs.index(output)
            self.output = output
        except:
            log_and_raise_error(logging.ERROR, 'Unsupported output: ' + output)

        if(display != None):
            self.display = display
        else: self.display = True

        self.baseurl = '%s://%s:%s/remote' % (protocol, self.host, self.port)

        #Setup a handler to pass credentials for BASIC auth
        passmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passmgr.add_password(None, self.baseurl, username.encode(_UTF8), password.encode(_UTF8))
        authhandler = urllib2.HTTPBasicAuthHandler(passmgr)
        if sys.version_info < (2, 7):
            self.opener = urllib2.build_opener(authhandler, urllib2.HTTPCookieProcessor())
        else: # version is 2.7 or above
            self.opener = urllib2.build_opener(ExHTTPSHandler(), authhandler, urllib2.HTTPCookieProcessor())

    def save_token(self):
        """
        Gets and saves the security token for this instance of CommandInvoker by calling
        the core.getSecurityToken command with no arguments.  Custom implementations will
        also need to request a security token, save it, and then submit it with each
        subsequent request to the server.
        Throws on error.
        """
        url = self.build_url_request('core.getSecurityToken', {})
        response = self.get_response(url)
        self.token = self.parse_response(response)

    def invoke(self, command, args={}):
        """
        Submits the requested command to the server, returning the results
        of the command's invocation according to the output type specified on 
        class creation, however, the output type can be overridden for this 
        invocation by passing in the argument ':output'.  It must be one of the
        supported protocols: terse, verbose, xml, or json.
        
        @param command - the name of the command (i.e., prefix.commandName.do)
        @param args - a dictionary of named arguments
        @returns the results of invoking the command as a json object
        @throws CommandInvokerException on error
        """
        argscopy = args
        output = None  # the output type for this invocation
        try:
            argscopy[':output'] = args[':output']
        except KeyError, e:
            #no overriding output type was specified so we use the default
            argscopy[':output'] = self.output
        output = argscopy[':output']
        if output != self.output:
            log(logging.INFO, "Invocation of '%s' requests '%s' output rather than default '%s'" % (command,output,self.output))

        #We get the token for each invocation of a command so that we don't generate excessive
        #login/logout messages when the token expires.
        self.save_token()

        #Extract the file upload arguments, put them in data
        fileargs = {}
        deletekeys = []
        for key in argscopy:
            arg = argscopy[key]
            if type(arg) != type('') and type(arg) != type(u''): continue #skip non-strings
            if arg[:8] == 'file:///':
                filename = arg[8:]
                content = self.get_file_contents(filename)
                fileargs[key] = (filename, content)
                deletekeys.append(key)
        for key in deletekeys:
            del argscopy[key]

        argscopy['orion.user.security.token'] = self.token
        url = self.build_url_request(command, argscopy)
        response = self.get_response(url, fileargs)
        content = self.parse_response(response)

        if output == 'json':
            try:
                return json.loads(content)
            except ValueError, e:
                log_and_raise_error(logging.ERROR, 'Error parsing JSON result: ' + str(e))
        elif output == 'xml':
             return content
        elif output == 'terse' or output == 'verbose':
            if self.display: print content
            elif not self.display: return content

    def get_response(self, url, fileargs={}):
        try:
            sock = self.create_socket(url, fileargs)
            resultStr = sock.read().decode(_UTF8)
            sock.close()
            log(logging.DEBUG, 'Response: ' + resultStr)
            return resultStr
        except HTTPError, e:
            log_and_raise_error(logging.ERROR, 'The server %s:%s could not fulfill the request. %s' % (self.host,self.port,str(e)))
        except URLError, e:
            log_and_raise_error(logging.ERROR, 'Failed to reach the server %s:%s. Error/reason: %s' % (self.host,self.port,str(e)))

    def parse_response(self, response):
        """
        Parses the raw response returned from a remote command invocation, returning
        its content, which is trimmed of leading and trailing whitespace.
        The input will look like the following:
        
        OK:\r\ntrue                                ---->  returns "true"
        
        or in the error case, 
        
        "Error # :\r\nSome error string goes here  ---->  throws CommandInvokerError(#, "Some error string goes here")
        
        where # is the integer representing the error code returned.  
            
        @param s - the raw response from the server
        @throws CommandInvokerError if the response from the server indicates an Error state
        @returns response from the server stripped of the protocol
        
        """
        d = {}
        code = 0
        try:
            status = response[:response.index(':')].split(' ')[0]
            result = response[response.index(':')+1:].strip()
            if status == 'Error': code = int(response[:response.index(':')].split(' ')[1])
            else: code = 0
            d = {'status':status, 'code':code, 'result':result}
        except: #for thoroughness, in case there's no colon in the output or something else
            #Or there was an error parsing the returned result from the server
            d = {'status':'Error', 'code':code, 'result':'Unable to parse the server\'s response'}
        if d["status"] == 'OK':
            pass
        elif d["status"] == 'Error':
            log_and_raise_error(logging.ERROR, d['result'], d['code'])
        else:
            log_and_raise_error(logging.ERROR, 'Unknown error occurred.  Status: (%s) Result: %s' % (d["status"], d["result"]))
        return d['result']


    def build_url_request(self, command, args):
        """
        Helper function to construct and return the url that will be requested from the server
        
        @param command - the command name (i.e., prefix.commandName)
        @param args - dictionary of the arguments to pass
        @returns the url to fetch (i.e, http://servername:8080/remote/prefix.commandName.do?arg=value)
        """
        url = '%s/%s.do' % (self.baseurl, command)
        query_string = "&".join(["%s=%s" % (quote(str(k)), quote(unicode(v))) for k, v in args.items()])
        if not query_string:
            return url
        return '%s?%s' % (url, query_string)

    def create_socket(self, url, args):
        """
        Helper function to encapsulate getting a socket
            
        @param url - the url to fetch (query string already appended)
        @param args - the file arguments as a tuple (filename, contents)
        @returns the socket object
        """
        log(logging.INFO, 'Request: ' + url)
        if( len(args) == 0):
            return self.opener.open(url)
        else:
            body, content_type = _encode_multipart_formdata(args)
            data = 'Content-Type: ' + content_type + '\r\n'
            data += 'Content-Length: ' + str(len(body)) + '\r\n\r\n'
            data += body
            log(logging.DEBUG, 'postdata:\r\n' + data)
            headers = {'Content-Type':content_type}
            req = Request(url, data, headers)
            return self.opener.open(req)

    def get_file_contents(self, filename):
        readmode = 'r'  #assume text file
        type = _get_content_type(filename)
        if(type[:3] != 'text'):
            readmode = 'rb'  #binary file
        f = open(filename, readmode)
        content = f.read()
        f.close()
        return content



def _get_command_names(invoker, feature=None):
    """
    Returns a list of command names using core.help
    This will only return the name of the command after
    the feature name...so if you call _get_command_names
    """
    #We only want json output here
    if feature == None:
        result = invoker.invoke('core.help', {':output':'json'})
    else:
        result = invoker.invoke('core.help', {'prefix':feature,':output':'json'})

    cmds = []
    for help in result:
        #need to use str() to convert fullName from unicode to ascii
        #otherwise it wont get appended to __members__
        fullName = str(help[:help.index(' ')])
        if feature != None:
            #get only the name of the command minus the prefix
            fullName = fullName[fullName.index('.')+1:]
        cmds.append(fullName)
    return cmds

def _get_command_prefixes(invoker):
    "Returns a list of all the defined command prefixes"
    cmds={}
    #cmds will be something like
    # {
    #  "core":["help","listUsers"],
    #  "tasklog":["listMessages","anotherCommand"]
    # }
    for fullName in _get_command_names(invoker):
        prefix = fullName[:fullName.index('.')]
        try:
            cmds[prefix].append('') #value appended is unimportant
        except:
            cmds[prefix] = []
    return cmds.keys()

class _PyCommand(object):
    "Represents an instance of a Python remote command"

    def __init__(self, invoker, prefix, name):
        self.invoker = invoker
        self.prefix = prefix
        self.name = name

    def __call__(self, *args, **kwargs):
        argmap = {}
        if len(list(args)) != 0:
            for index, value in enumerate(args):
                argmap['param' + str(index+1)] = value
        if len(list(kwargs)) != 0:
            for key in kwargs.keys():
                argmap[key] = kwargs[key]
        try:
            return self.invoker.invoke(self.prefix + '.' + self.name, argmap)
        except CommandInvokerError, e:
            if e.code == 1:
                msg = "'" + self.prefix + "' has no attribute '" + self.name + "' (make sure the command exists and that mcafee.client(...) was called prior to invoking the command)"
                log(logging.WARN, msg)
                raise AttributeError(msg)
            else:
                log(logging.ERROR, e.msg)
                raise e


class _PyFeature(object):
    """
    _PyFeature represents an object in the 'client' class scope
    corresponding to the feature in a remote command (e.g., core, tasklog)
    
    @param name - the name of the command
    """

    def __init__(self, invoker, name):
        self._module = name
        self._invoker = invoker

    def __getattr__(self, attr):
        """
        When the caller requests attributes that are not available, assume
        the caller wants to create a _PyCommand.  Also catch calls that dir()
        makes so we can return a list of commands
        """
        cmd = attr # for clarity...this is the command name, ie, listUsers

        #We must catch accessing __members__,__repr__, and __str__ attributes
        #otherwise it will attempt to create a PyCommand and hence hit the server
        #which we don't want.
        if cmd == '__members__':
            return # there are no members of a PyClient, only methods
        if cmd == '__methods__':
            return _get_command_names(self._invoker, self._module)
        if cmd == '__repr__':
            return # should anything be returned here?
        if cmd == '__str__':
            return # should anything be returned here?
        if cmd == '__call__':
            msg = "'" + self._module + "' object is not callable"
            log(logging.WARN, msg)
            raise TypeError(msg)
        pc = _PyCommand(self._invoker, self._module, cmd)
        return pc

class client(object):
    """
    The mcafee client object provides the bindings to remote commands.
    In general it allows accessing an unknown, undefined attribute 'attr'
    in this object.  Instantiating an instance of this class will provide
    access to mcafee commands.
    """

    def __init__(self, host, port, username, password, protocol='https', output='json', display=True):
        """
        Instantiates an instance of this class provides access to McAfee commands.
        
            @param host - the host name
            @param port - the port name
            @param username - the username
            @param password - the password
            @param protocol - the protocol to use for the connection (default 'https')
            @param output - the requested format from the server (default 'json')
            @param display - indicates whether to print the response or return it  (default True) 
            
            Example:
            
            >>> import mcafee
            >>> mc = mcafee.client('host','port','usr','pwd')
            >>> mc.core.commandName()
            
        
            >>> import mcafee
            >>> mc = mcafee.client('host','port','usr','pwd',output='xml',display=False)
            >>> mc.core.commandName()
        """
        log(logging.INFO, "Creating client to '%s:%s' using '%s' requesting '%s' output (display=%d)" % (host,str(port),protocol,output,display))
        self._invoker = _CommandInvoker(host, port, username, password, protocol, output, display)
        #hit the server so we can verify server and credentials will throw on error
        self._invoker.save_token()

    def __getattr__(self, attr):
        """
        When the caller requests attributes that are not available, assume
        the caller wants to create a _PyFeature, otherwise return the attribute"""
        feature = attr #for clarity
        #The following is to overcome http://bugs.python.org/issue5370
        #If we use getattr(self, attr) we get infinite recursion
        if 'attrs' in self.__dict__ and name in self.attrs:
            return self.attrs[name]
        else:
            if attr == '__members__':
                return _get_command_prefixes(self._invoker)
            return _PyFeature(self._invoker, feature)

    def help(self, command=None):
        """
        Prints help for all commands or a specified command
        Use this command to get help on mcafee commands rather than python's
        built-in help().
        
        @param command - the command name
        
        Example:
        
        >>> import mcafee
        >>> mc = mcafee.client('host','port','usr','pwd')
        >>> mc.help('core.help')
        
        """
        #Override the default output type so the output is human readable
        if (command != None):
            self._invoker.invoke("core.help", {'command':command,':output':'terse'})
        else:
            self._invoker.invoke("core.help", {':output':'terse'})

    def run(self, *args, **kwargs):
        """
        Runs an arbitrary command with positional and/or named arguments
        Expects the first positional argument to be the command name
        
        For example,
            >>> import mcafee
            >>> c = mcafee.client(host,port,usr,pwd)
            >>> c.run('core.addUser','testUser','testUser')
            True
            >>>
        """
        argmap = {}
        cmdName = None
        if (len(list(args)) < 1):
            raise Exception('run requires at least one positional argument and it must be the command name')
        if len(list(args)) != 0:
            for index, value in enumerate(args):
                if(index == 0):
                    cmdName = value
                else:
                    argmap['param' + str(index)] = value
        if len(list(kwargs)) != 0:
            for key in kwargs.keys():
                argmap[key] = kwargs[key]
        try:
            return self._invoker.invoke(cmdName, argmap)
        except CommandInvokerError, e:
            if e.code == 1:
                msg = "'" + self.prefix + "' has no attribute '" + self.name + "' (make sure the command exists and that mcafee.client(...) was called prior to invoking the command)"
                raise AttributeError(msg)
            else:
                raise e


    def _run(self, command, args={}):
        """
        Runs an arbitrary command, useful for passing system parameters that start with a colon (:)
        and hence are unable to be passed to the client.run() method because they are invalid
        identifiers.
        
        @param command - the command name
        @param args - dictionary of arguments to the command
        
        """

        return self._invoker.invoke(command, args)                

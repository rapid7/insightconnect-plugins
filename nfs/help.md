
# NFS

## About

The NFS plugin allows access to files on an [NFS](https://en.wikipedia.org/wiki/Network_File_System) 3 server.
Specifically, it offers read and write actions and a File Changed trigger.

This plugin utilizes the Go NFS library.

UNIX experts can think of this plugin as an NFS 3 client that packages up requests to portmap, mountd, and nfsd in one convenient place.

## Actions

### Read

This action is used to read the named file via NFS.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_pathname|string|None|True|File pathname starting with NFS mount point (path separator is /)|None|
|lines_to_read|integer|None|False|Number of lines to read (unsupplied or -1 means read all lines)|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|lines_read|[]string|False|Lines read from the NFS-mounted file|

### Write

This action is used to write to the named file via NFS.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_pathname|string|None|True|File pathname starting with NFS mount point (path separator is /)|None|
|lines_to_write|[]string|None|True|Lines to write to the named file|None|
|create_if_missing|boolean|True|False|Create the named file before beginning write|None|
|remove_if_present|boolean|None|False|Remove then re-create an empty file of the same name before beginning write|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|write_successful|boolean|False|The NFS write operation succeeded|

## Triggers

### File Changed

This trigger is used to reports any file changes within the given interval.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_pathname|string|None|True|File pathname starting with NFS mount point (path separator is /)|None|
|interval|integer|60|False|How often to detect file changes (in seconds)|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|changed_attributes|object|False|None|

## Connection

The NFS mount point need not have been established to use this plugin. It automatically performs a mount operation before reading,
writing, or scanning for file changes.  (Caveat: The NFS server's /etc/exports file must be configured to allow access by the client
process - i.e. it must contain an entry matching the "Export file hostname" parameter of this plugin.)

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|client_external_ip|string|None|True|External IP that the client machine uses to contact the NFS server|None|
|exports_file_hostname|string|None|True|Hostname of the client machine in the NFS server's /etc/exports file|None|
|client_machine_name|string|None|True|Network name of client machine (not the external DNS name)|None|
|timeout|integer|None|False|Assume the NFS server is down after this many seconds (0 means no timeout)|None|
|mount_pathname|string|None|True|Full pathname of the mount point on the NFS server (path separator is /)|None|

More details on the parameters used to establish the initial NFS mount point.

* Mount pathname:
  Full pathname of the mount point on the NFS server. (The path separator is / regardless of operating system.)

* Client machine name:
  This is the name on the local network of the machine on which the NFS client runs, as known to the NFS server. It is NOT the public name of the
  client machine as provided by DNS. It is used in the authentication data sent with the NFS request.

* Export file hostname:
  This is same as the hostname specifying the NFS client in the relevant entry in the /etc/exports file on the NFS server (see the man page "exports").

* Client external IP:
  This is the external IP address (e.g. of the router used by the client machine). The NFS server uses the client's external IP to
  help verify that incoming NFS request is coming from a reserved port (i.e. one that only superuser can access).

The above parameters can be determined by using a network sniffer (e.g. Wireshark) to eavesdrop on a pre-existing successful NFS file
operation from the command line (e.g. cat'ing a file whose directory was mount_nfs'd).

## Troubleshooting

This plugin does not currently support the NFS 4 protocol. Furthermore, it uses TCP transport exclusively to communicate
with the NFS server (i.e. it does not currently support UDF).

This plugin assumes the NFS server is down after the connection Timeout interval (in seconds). It defaults to 10.
Note that the mount timeout is separate from read and or write.  In other words, each read and write operation resets
the timeout clock to zero.

The line separator that this plugin uses in read and write operations is the UTF-8 newline code point. Hence this plugin expects to read
and write files that are in UTF-8 format, or that can be interpreted as being in UTF-8 (such as pure ASCII files).

The following details are specific to the write action. The create_if_missing flag defaults to true. The remove_if_present flas
defaults to false. If the file exists and remove_if_present is false or unsupplied, this plugin will append to the end of the file.
If the file exists and remove_if_present is true, this plugin will replace it with an empty file, regardless of the value of create_if_missing.
As an edge case, if the file does not exist and create_if_missing is false, this plugin will fail.

## Workflows

Examples:

* Obtain or monitor files

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - Undocumented bug fix
* 1.0.0 - Update to v2 architecture | Support web server mode
* 1.0.1 - Regenerate with latest Go SDK to solve bug with triggers
* 1.0.2 - Fix vendoring

## References

* [NFS](https://en.wikipedia.org/wiki/Network_File_System)

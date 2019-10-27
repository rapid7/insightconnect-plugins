package implementation

// all props to davecheney nfs client impl example/ismount/main.go
// in Dave's code, the NFS client requests the NFS server to mount a volume
// we'll need to tweak it to get LOOPUP, READ, etc

// INITIAL DESIGN
/*
minimal happy path:
- Use NFS version 3 (as opposed to 4)
- For testing, NFS client on guest Vagrant machine accesses nfsd on
  host machine
- NFS client runs as root
- Use TCP transport (UDP problematic)
- Assume TCP is big-endian per RFC 1700
- MOUNT RPC uses port mapping
- All other RPCs use port 2049 per RFC 1813

MOUNT RPC
- This is where we get the top-level NFS filehandle to pass to the
  other RPCs
- Request issued to mountd, needs port mapping
- Input: dir path string (e.g. "../../nfs"), UNIX credentials
- Output: nfs_fh3 struct, nil or nil, error

LOOKUP RPC:
- Walks through the path components to get the handle of the desired
  file object
- Request issued to nfsd on well-known port 2049
- Input: valid nfs_fh3 filehandle, components
  (e.g. ["read", "test_log01.log"] )
- Output: nfs_fh3 struct, nil or nil, error

READ RPC:
- Request issued to nfsd on well-known port 2049
- Input: valid nfs_fh3 filehandle, number of lines
- Output: array of one byte array per line, nil or nil, error

WRITE RPC:
- Request issued to nfsd on well-known port 2049
- Input: valid nfs_fh3 filehandle, array of one byte array per line
- Output: nil or error

TODO: detect change in file - can we "just" notice a change in the
"opaque" sequence of filehandle bytes?  This seems to work on Mac OSX
at least.
*/

// DEV SETUP
/*
The NFS server runs on my Mac (OsX Sierra 10.12.2).
My Mac is the host for the normal Komand Vagrant guest VM.
The NFS client (this code) runs on the Vagrant guest.

Basically, we configure the client on the guest to use DHCP, and we
configure the server on the host to accept NFS requests from the
guest.  We then configure both the host to forward ports
appropriately.

*** NFS CLIENT/GUEST CONFIG

Vagrant 1.8.6

# We'll use vagrant-triggers to forward ports at up/reload time
vagrant plugin install vagrant-triggers

# Vagrantfile edits:

  # Temporary experiment - if Vagrant can do this then we can too
  #config.vm.synced_folder "../../nfs/", "/nfs", type: "nfs"
  # (here's what VAGRANT_LOG="debug" tells me Vagrant is doing)
  #mkdir -p /nfs
  #mount -o vers=3,udp 172.28.128.1:/Users/jhodgkinson/Komand/nfs /nfs

  # virtualbox (as opposed to VMware) requires a private network for NFS to work
  config.vm.network "private_network", type: "dhcp"

  # Need to forward portmap and nfsd ports on the guest machine
  config.vm.network "forwarded_port", guest: 111, host: 1119, protocol: "tcp"
  config.vm.network "forwarded_port", guest: 2049, host: 20499, protocol: "tcp"

  # Also needed to "reverse forward" portmap and nfsd ports on the host machine
  # host machine (props to Dan Purdy!)
  config.trigger.after [:provision, :up, :reload] do
    system('echo "
      rdr pass on lo0 inet proto tcp from any to 127.0.0.1 port 111 -> 127.0.0.1 port 1119
      rdr pass on lo0 inet proto tcp from any to 127.0.0.1 port 2049 -> 127.0.0.1 port 20499
    " | sudo pfctl -ef - > /dev/null 2>&1; echo "==> Fowarding Ports: 111 -> 1119, 2049 -> 20499 & Enabling pf"')
  end
  config.trigger.after [:halt, :destroy] do
    system("sudo pfctl -df /etc/pf.conf > /dev/null 2>&1; echo '==> Removing Port Forwarding & Disabling pf'")
  end

*** NFS SERVER HOST CONFIG

# Run the "experiment" in the above Vagrantfie edits and see what
# Vagrant writes into /etc/exports.  Then "just" use the same entry.
# This is what it wrote for me:

  "/Users/jhodgkinson/Komand/nfs" 172.28.128.3 -alldirs -mapall=501:20
*/

// NOTE: this code does not use Vagrant to set up its NFS mount
// points, we are only patterning after what Vagrant does.  See the
// "SETUP" section in nfs.go for further details.

// NFSConfig encompasses the parameters needed to perform all required
// actions and triggers of the NFS plugin.
type NFSConfig struct {
	// ClientMachineName is the name of the machine on which the NFS
	// client runs.
	ClientMachineName string

	// ExportIP on the NFS client is the same as the hostname entry in
	// the /etc/exports file on the NFS server.  This is the entry that
	// sets up the NFS mount point that the client wants to access.
	ExportIP string

	// ClientExternalIP on the NFS client is the external IP address
	// (e.g. of a router). The NFS server uses to verify that incoming
	// NFS request is coming from a reserved port (i.e. one that only
	// superuser can access).  This is fairly crummy security, but it is
	// the NFS3 way.
	ClientExternalIP string

	// MountExternalIP is usually the same as ClientExternalIP, but is
	// provided for flexibility for those systems that may have added
	// extra security to the mount daemon.
	MountExternalIP string

	// ReadChunkSize is for simple flow control
	ReadChunkSize uint32

	// WriteChunkSize is for simple flow control
	WriteChunkSize uint32

	// ReadDelimiter is the byte or bytes the implementation uses
	// to split NFS file data into "lines".
	ReadDelimiter []byte

	// WriteDelimiter is the byte or bytes the caller uses to separate
	// lines.
	WriteDelimiter []byte
}

// DefaultReadChunkSize provides simple flow control for the read
// operation.
var DefaultReadChunkSize = uint32(100)

// DefaultWriteChunkSize provides simple flow control for the write
// operation.
var DefaultWriteChunkSize = uint32(100)

// DefaultReadDelimiter is the line separator used when reading from
// an NFS-mounted file.  Read delimiters more than one byte in length
// are not currently by this code.  (We'd need to look backwards by
// the delimiter length to see if the previous chunk terminated before
// a complete newline - not worth it for now.)
var DefaultReadDelimiter = []byte("\n")

// DefaultWriteDelimiter is the line separator used when writing to an
// NFS-mounted file.  Write delimiters more than one byte in length
// are coded, but not currently supported.
var DefaultWriteDelimiter = []byte("\n")

// NewConfig is a convenience function to create an NFSConfig instance
// starting with the usual defauls.
func NewConfig(client string, exportIP string, clientIP string, moreIPs ...string) NFSConfig {
	mountIP := clientIP
	if len(moreIPs) > 0 {
		mountIP = moreIPs[0]
	}
	config := NFSConfig{
		ClientMachineName: client,
		ExportIP:          exportIP,
		ClientExternalIP:  clientIP,
		MountExternalIP:   mountIP,
		ReadChunkSize:     DefaultReadChunkSize,
		WriteChunkSize:    DefaultWriteChunkSize,
		ReadDelimiter:     DefaultReadDelimiter,
		WriteDelimiter:    DefaultWriteDelimiter,
	}
	return config
}

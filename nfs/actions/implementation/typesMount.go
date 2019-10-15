package implementation

// Adapted from davecheney's golang NFS client (thanks!)

// The Portmapper struct contains the TCP/IP transport layer necessary
// to contact the portmap daemon.
type Portmapper struct {
	// jh, 1/18/17.  I couldn't get UDP to work, but hopefully the
	// Minimal Viable Product only needs TCP
	*TCPtransporter
}

// PmapPort holds the well-known address of the portmap daemon.
const PmapPort = 111

// The Mapping struct contains the RPC frame for a getport request and
// response.
type Mapping struct {
	Prog uint32
	Vers uint32
	Prot uint32
	Port uint32
}

// The MountTransport struct contains the TCP/IP transport layer
// necessary to contact the mount daemon.
type MountTransport struct {
	*TCPtransporter
}

// PmapProg and the other PmapXXX constants populate the Header of a
// getport request
const (
	PmapProg        = 100000
	PmapVers        = 2
	PmapprocGetport = 3
)

// MountProg and the other MountXXX constants populate the header of a
// mount request
const (
	MountProg     = 100005
	MountVers     = 3
	Mountproc3Mnt = 1
)

// IpprotoTCP populates the Mapping frame of an RPC into the port daemon
const (
	IpprotoTCP = 6
	//IpprotoUDP = 17 // Not used as of 1/18/17
)

// Mnt3OK signifies a successfult NFS mount operation.  The Mnt3errXXX
// constants specify which sort of failure occurred.
const (
	Mnt3OK             = 0  // no error
	Mnt3errPerm        = 1  // Not owner
	Mnt3errNoent       = 2  // No such file or directory
	Mnt3errIO          = 5  // I/O error
	Mnt3errEmpty       = 10 // result is empty // jh added
	Mnt3errAcces       = 13 // Permission denied
	Mnt3errNotdir      = 20 // Not a directory
	Mnt3errNametoolong = 63 // Filename too long
)

// The MountError struct represents an error that occurs during an NFS
// mount operation.
type MountError struct {
	ErrorString string
}

func (err *MountError) Error() string { return err.ErrorString }

package implementation

import "encoding/binary"
import "io"
import "fmt"

// a jh extension of davecheney's golang NFS client (thanks!)

// NFSPort is the well-known TCP/IP port to which the NFS daemon
// listens
const NFSPort = 2049

// DialNFS sets up a TCP/IP connection to the NFS daemon.
func DialNFS(net, host string) (*NFSd, error) {
	client, err := DialTCP(net, host, NFSPort)
	if err != nil {
		return nil, err
	}
	return &NFSd{client}, nil
}

// The NFSd struct contains the TCP/IP transport layer necessary
// to contact the NFS daemon.
type NFSd struct {
	*TCPtransporter
}

// The Header struct serves as the RPC header of an NFS-related
// request (whether to nfsd itself, or to the portmap or mount
// daemons)
type Header struct {
	Rpcvers uint32
	Prog    uint32
	Vers    uint32
	Proc    uint32
	Cred    Auth
	Verf    Auth
}

// The Volume struct contains information about a file: its opaque NFS file handle,
// its attributes and the file handle of its parent directory.
type Volume struct {
	Name        string
	FH          []byte
	Attrs       *Fattr3
	ParentFH    []byte
	Nonexistent bool // nonexistent, but with an existing parent directory
}

// The INFSError interface encapsulates an error that occurs while
// servicing a request to the NFS daemon
type INFSError interface {
	error
	Code() NFSstat3
}

// The NFSError struct implements INFSError
type NFSError struct {
	ErrorString string
	ErrorCode   NFSstat3
}

func (err *NFSError) Error() string { return err.ErrorString }

// Code called on a NFSError instance returns the numeric error
// code as documented in RFC 1813.
func (err *NFSError) Code() NFSstat3 { return err.ErrorCode }

// SpecializeNFSError takes the result of an RPC operation into the
// NFS daemon and returns an object representing the specfic error
func SpecializeNFSError(errCode NFSstat3, op string) INFSError {
	mark := func(errMsg string) string {
		return fmt.Sprintf("%v: %v", op, errMsg)
	}
	switch errCode {
	case NFS3ErrPerm:
		return &NFSError{mark("NFS3ErrPerm"), errCode}
	case NFS3ErrNoent:
		return &NFSError{mark("NFS3ErrNoent"), errCode}
	case NFS3ErrIO:
		return &NFSError{mark("NFS3ErrIO"), errCode}
	case NFS3ErrNxIO:
		return &NFSError{mark("NFS3ErrNxIO"), errCode}
	case NFS3ErrAcces:
		return &NFSError{mark("NFS3ErrAcces"), errCode}
	case NFS3ErrExist:
		return &NFSError{mark("NFS3ErrExist"), errCode}
	case NFS3ErrXdev:
		return &NFSError{mark("NFS3ErrXdev"), errCode}
	case NFS3ErrNodev:
		return &NFSError{mark("NFS3ErrNodev"), errCode}
	case NFS3ErrNotdir:
		return &NFSError{mark("NFS3ErrNotdir"), errCode}
	case NFS3ErrIsdir:
		return &NFSError{mark("NFS3ErrIsdir"), errCode}
	case NFS3ErrInval:
		return &NFSError{mark("NFS3ErrInval"), errCode}
	case NFS3ErrFbig:
		return &NFSError{mark("NFS3ErrFbig"), errCode}
	case NFS3ErrNospc:
		return &NFSError{mark("NFS3ErrNospc"), errCode}
	case NFS3ErrRofs:
		return &NFSError{mark("NFS3ErrRofs"), errCode}
	case NFS3ErrMlink:
		return &NFSError{mark("NFS3ErrMlink"), errCode}
	case NFS3ErrNametoolong:
		return &NFSError{mark("NFS3ErrNametoolong"), errCode}
	case NFS3ErrNotempty:
		return &NFSError{mark("NFS3ErrNotempty"), errCode}
	case NFS3ErrDquot:
		return &NFSError{mark("NFS3ErrDquot"), errCode}
	case NFS3ErrStale:
		return &NFSError{mark("NFS3ErrStale"), errCode}
	case NFS3ErrRemote:
		return &NFSError{mark("NFS3ErrRemote"), errCode}
	case NFS3ErrBadhandle:
		return &NFSError{mark("NFS3ErrBadhandle"), errCode}
	}
	return &NFSError{mark(fmt.Sprintf("unknown NFS stat: %d", errCode)), errCode}
}

// ReceiveHandle assumes the RPC buffer holds an hanldeFollows
// element.  IOW don't use this func simply to read a handle -
// XdrOpaque is fine for that.
func ReceiveHandle(drdr io.Reader, which string) ([]byte, INFSError) {
	var handle []byte
	handleFollows := uint32(0)
	binary.Read(drdr, binary.BigEndian, &handleFollows)
	if handleFollows == 1 {
		handleLen := uint32(0)
		binary.Read(drdr, binary.BigEndian, &handleLen)
		handle = make([]byte, handleLen)
		n, err := drdr.Read(handle)
		if err != nil {
			ctl := which + " handle read error: %v"
			return nil, &NFSError{fmt.Sprintf(ctl, err), NFS3ErrElsewhere}
		}
		if uint32(n) != handleLen {
			ctl := which + " handle length mismatch, RPC: %v, io.Read: %v"
			return nil, &NFSError{fmt.Sprintf(ctl, handleLen, n), NFS3ErrElsewhere}
		}
	}
	if handle == nil {
		return nil, &NFSError{"no " + which + " handle produced", NFS3ErrElsewhere}
	}
	return handle, nil
}

// ReceiveAttributes assumes the RPC buffer holds an attrsFollow
// element.  IOW don't use this func simply to read attributes.
func ReceiveAttributes(drdr io.Reader, which string) (*Fattr3, INFSError) {
	attrs := Fattr3{}
	attrsFollow := uint32(0)
	binary.Read(drdr, binary.BigEndian, &attrsFollow)
	if attrsFollow == 1 {
		err := XdrRead(drdr, &attrs)
		if err != nil {
			ctl := which + " attributes read error: %v"
			return nil, &NFSError{fmt.Sprintf(ctl, err), NFS3ErrElsewhere}
		}
	}
	return &attrs, nil
}

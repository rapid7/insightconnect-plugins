package implementation

// Adapted from davecheney's golang NFS client (thanks!)

import "fmt"
import "encoding/binary"
import "bytes"

// DialNfs opens a TCP/IP connection to the nfs daemon
func DialNfs() { /* NYI, pattern after DialPortMapper */ }

type message struct {
	Xid     uint32
	Msgtype uint32
	Body    interface{}
}

// MsgAccepted indicates the RPC call was well-formed and
// well-credentialed.  MsgDenied, not so much.
const (
	MsgAccepted = iota
	MsgDenied
)

// Success indicates the ROC returned normally.  The other ProgXXX
// constants, not so much.
const (
	Success = 0

	// The remote program is not available on the remote system.
	ProgUnavail = 1

	// The remote program does not support the requested version
	// number. The lowest and highest supported remote program
	// version numbers are returned.
	ProgMismatch = 2

	// The requested procedure number does not exist.  (This is
	// usually a client side protocol or programming error.)
	ProcUnavail = 3

	// The parameters to the remote procedure appear to be garbage
	// from the server's point of view.  (As with ProcUnavail,
	// this is usually caused by a disagreement about the protocol
	// between client and service.)
	GarbageArgs = 4
)

// RPCMismatch indicates the RPC being called is not properly
// specified.
const RPCMismatch = 0

// AuthError indicates a security problem that caused the rpc call to
// be rejected
const AuthError = 1

// RFC 1057 - RPCs
const (
	// A possible cause of AuthBadcred is a malformed Auth structure
	// (e.g. a padding issue, see "BAD DOG" bugfix in rpcargs.go).  You
	// can isolate problems like this with Wireshark.  Neither Mr Google
	// nor I have any idea what "seal broken" means.
	AuthBadcred      = 1 // bad credentials (seal broken)
	AuthRejectedcred = 2 // client must begin new session
	AuthBadverf      = 3 // bad verifier (seal broken)
	AuthRejectedverf = 4 // verifier expired or replayed
	// Possible causes of AuthTooweak:
	// - use of an internal LAN IP vs an external IP (e.g. HostLanIP vs
	//   NfsRouterIP in nfs_test.go)
	// - use of an unreserved port (NFS security setups require requests
	//   to originate from reserved ports, because only superusers can
	//   access them)
	AuthTooweak = 5 // rejected for security reasons
)

// RPCCallTCP invokes the given RPC over a TCP/IP connection and
// returns its result as a buffer of bytes.
func (t *TCPtransporter) RPCCallTCP(call interface{}) ([]byte, error) {
	msg := &message{
		Xid:     0xcafebabe,
		Msgtype: 0,
		Body:    call,
	}
	w := new(bytes.Buffer)
	if err := XdrWrite(w, msg); err != nil {
		return nil, fmt.Errorf("XdrWrite", err)
	}
	if err := t.transport.SendTCP(w.Bytes()); err != nil {
		return nil, fmt.Errorf("SendTCP", err)
	}
	buf, err := t.transport.RecvTCP()
	if err != nil {
		return nil, fmt.Errorf("RecvTCP", err)
	}
	return rpcCallTail(call, msg, buf)
}

func rpcCallTail(call interface{}, msg *message, buf []byte) ([]byte, error) {
	xid, buf := XdrUint32(buf)
	if xid != msg.Xid {
		return nil, fmt.Errorf("xid did not match, expected: %x, received: %x", msg.Xid, xid)
	}
	mtype, buf := XdrUint32(buf)
	if mtype != 1 {
		return nil, fmt.Errorf("message as not a reply: %d", mtype)
	}
	replyStat, buf := XdrUint32(buf)
	switch replyStat {
	case MsgAccepted:
		_, buf = XdrUint32(buf)
		opaqueLen, buf := XdrUint32(buf)
		_ = buf[0:int(opaqueLen)]
		buf = buf[opaqueLen:]
		acceptStat, buf := XdrUint32(buf)
		switch acceptStat {
		case Success:
			return buf, nil
		case ProgUnavail:
			return nil, fmt.Errorf("ProgUnavail")
		case ProgMismatch:
			return nil, fmt.Errorf("rpc: ProgMismatch")
		case ProcUnavail:
			return nil, fmt.Errorf("ProcUnavail")
		case GarbageArgs:
			return nil, fmt.Errorf("rpc: GarbageArgs")
		default:
			return nil, fmt.Errorf("rpc: unknown stat %d", acceptStat)
		}
	case MsgDenied:
		rejectedStat, buf := XdrUint32(buf)
		switch rejectedStat {
		case RPCMismatch:
			return nil, fmt.Errorf("RPCMismatch")

		// jh enhancement to Dave's code
		case AuthError:
			authStat, _ := XdrUint32(buf)
			authErr := "AuthError: "
			switch authStat {
			case AuthBadcred:
				authErr = authErr + "BADCRED"
			case AuthRejectedcred:
				authErr = authErr + "REJECTEDCRED"
			case AuthBadverf:
				authErr = authErr + "BADVERF"
			case AuthRejectedverf:
				authErr = authErr + "REJECTEDVERF"
			case AuthTooweak:
				authErr = authErr + "TOOWEAK"
			default:
				authErr = fmt.Sprintf("authStat was not valid: %d", authStat)
			}
			return nil, fmt.Errorf(authErr)

		default:
			return nil, fmt.Errorf("rejectedStat was not valid: %d", rejectedStat)
		}
	default:
		return nil, fmt.Errorf("replyStat was not valid: %d", replyStat)
	}
	panic("unreachable")
}

// XdrUint32 takes as arg a slice of bytes.  It returns two values:
// (1) the first 4 bytes converted into a big-endian unsigned int32
// (2) the remaining bytes in the arg.
func XdrUint32(b []byte) (uint32, []byte) {
	return binary.BigEndian.Uint32(b[0:4]), b[4:]
}

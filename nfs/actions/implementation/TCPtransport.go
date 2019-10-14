package implementation

// Adapted from davecheney's golang NFS client (thanks!)

import "encoding/binary"
import "io"
import "sync"
import "bufio"
import "net"
import "fmt"

// DialTCP opens a TCP connection to the given host and port.  It
// returns a TCPtransporter struct.  Its network arg must be the
// string "tcp" (this is an appendage for when we implement UDP).
func DialTCP(network, host string, port int) (*TCPtransporter, error) {
	if network != "tcp" {
		panic(fmt.Sprintf("DialTCP expected network to be tcp not %v", network))
	}
	addr := fmt.Sprintf("%v:%d", host, port)
	a, err := net.ResolveTCPAddr(network, addr)
	if err != nil {
		return nil, err
	}
	conn, err := net.DialTCP(a.Network(), nil, a)
	if err != nil {
		return nil, err
	}
	t := &tcpTransport{
		Reader:      bufio.NewReader(conn),
		WriteCloser: conn,
	}
	return &TCPtransporter{t}, nil
}

// TCPtransporter contains the TCP/IP layer
type TCPtransporter struct {
	transport *tcpTransport
}

type tcpTransport struct {
	io.Reader
	io.WriteCloser
	rlock, wlock sync.Mutex
}

// Method RecvTCP reads TCP/IP traffic from a tcpTransport instance.
func (u *tcpTransport) RecvTCP() ([]byte, error) {
	u.rlock.Lock()
	defer u.rlock.Unlock()
	var hdr uint32
	// TCP is BigEndian per RFC 1700
	if err := binary.Read(u, binary.BigEndian, &hdr); err != nil {
		return nil, err
	}

	// Why hdr&0x7fffffff ?
	// See the section entitled RECORD MARKING STANDARD in RFC 1057
	buf := make([]byte, hdr&0x7fffffff)

	if _, err := io.ReadFull(u, buf); err != nil {
		return nil, err
	}
	return buf, nil
}

// Method SendTCP writes TCP/IP traffic to a tcpTransport instance.
func (u *tcpTransport) SendTCP(buf []byte) error {
	u.wlock.Lock()
	defer u.wlock.Unlock()
	var hdr = uint32(len(buf)) | 0x80000000
	b := make([]byte, 4)
	binary.BigEndian.PutUint32(b, hdr)
	_, err := u.WriteCloser.Write(append(b, buf...))
	return err
}

type dialError struct {
	errorString string
}

func (err *dialError) Error() string {
	return err.errorString
}

// This function is a jh extension of Dave's code.
func dialOneReservedTCP(exportIP string, routerIP string, localport int, mountport int) (*TCPtransporter, error) {
	eaddr := fmt.Sprintf("%v:%d", exportIP, localport)
	exportAddr, err := net.ResolveTCPAddr("tcp", eaddr)
	if err != nil {
		return nil, err
	}
	raddr := fmt.Sprintf("%v:%d", routerIP, mountport)
	routerAddr, err := net.ResolveTCPAddr("tcp", raddr)
	if err != nil {
		return nil, err
	}
	conn, err := net.DialTCP(exportAddr.Network(), exportAddr, routerAddr)
	if err != nil {
		return nil, err
	}
	t := &tcpTransport{
		Reader:      bufio.NewReader(conn),
		WriteCloser: conn,
	}
	return &TCPtransporter{t}, nil
}

// DialReservedTCP opens a TCP connection using first available "reserved" port.
// Typical NFS server setups require this as a security measure,
// because only the client's super-user is authorized to open reserved
// ports.  This function is a jh extension of Dave's code.
func DialReservedTCP(network, exportIP string, routerIP string, mountport int) (*TCPtransporter, error) {
	if network != "tcp" {
		panic(fmt.Sprintf("DialTCP expected network to be tcp not %v", network))
	}
	localport := 1023
	for localport > 0 {
		localport--
		trans, err := dialOneReservedTCP(exportIP, routerIP, localport, mountport)
		if err == nil {
			return trans, nil
		}
	}
	msg := "no reserved ports available"
	msg += fmt.Sprintf("\n- expIP: %v, routIP: %v, lport: %v, mport: %v", exportIP, routerIP, localport, mountport)
	return nil, &dialError{msg}
}

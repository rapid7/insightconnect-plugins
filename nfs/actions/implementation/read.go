package implementation

import "time"
import "strings"
import "fmt"

type routCh chan []string
type rerrCh chan error

// DefaultReadTimeoutInSec is the timeout we use for a read operation,
// unless otherwise specified.
const DefaultReadTimeoutInSec = 10

// NFSRead exposes the NFS read RPC to the Komand connection layer.
// It takes the mount path on the server, the file path starting at
// the mount point, the number of lines to read, timeout in seconds,
// and an NFSConfig instance.  It returns an array of strings, one per
// line read or an error if something went wrong.
func NFSRead(baseFH []byte,
	path string,
	numLines int,
	timeoutSecs int,
	c *NFSConfig) ([]string, error) {

	nfsOut := make(routCh)
	nfsErr := make(rerrCh)
	timeout := time.After(time.Duration(timeoutSecs) * time.Second)
	go func() { nfsRead1(baseFH, path, numLines, c, nfsOut, nfsErr) }()
	select {
	case readOut := <-nfsOut:
		return readOut, nil
	case err := <-nfsErr:
		return nil, err
	case <-timeout:
		msg := fmt.Sprintf("NFS read timed out after %v seconds", timeoutSecs)
		return nil, &ReadError{msg}
	}
}

func nfsRead1(baseFH []byte,
	path string,
	num int,
	c *NFSConfig,
	outC routCh,
	errC rerrCh) {

	components := strings.Split(path, "/")
	volume, err := Lookup(baseFH, components, c)
	if err == nil {
		if volume.Nonexistent {
			errC <- &NFSError{"read: NFS3ErrNoent", NFS3ErrNoent}
		}
		linesOfBytes, err := Read(volume.FH, num, c)
		if err == nil {
			lines := []string{}
			for i := 0; i < len(linesOfBytes); i++ {
				lines = append(lines, string(linesOfBytes[i]))
			}
			outC <- lines
		}
		errC <- &ReadError{fmt.Sprintf("Read, err: %v\n", err)}
	}
	errC <- &ReadError{fmt.Sprintf("Read > Lookup, err: %v\n", err)}
}

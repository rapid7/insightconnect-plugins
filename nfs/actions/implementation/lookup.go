package implementation

import "time"
import "strings"
import "fmt"

type loutCh chan *Volume
type lerrCh chan error

// DefaultLookupTimeoutInSec is the timeout we use for the NFS lookup
// operation, unless otherwise specified.
const DefaultLookupTimeoutInSec = 10

// NFSLookup will signal an error if the file does not exist (unlike
// Lookup, which needs to report the non-existence of a file to
// support the create_if_missing parameter of the write action.
func NFSLookup(baseFH []byte,
	path string,
	timeoutSecs int,
	c *NFSConfig) (*Volume, error) {

	nfsOut := make(loutCh)
	nfsErr := make(lerrCh)
	timeout := time.After(time.Duration(timeoutSecs) * time.Second)
	go func() { nfsLookup1(baseFH, path, c, nfsOut, nfsErr) }()
	select {
	case lookOut := <-nfsOut:
		return lookOut, nil
	case err := <-nfsErr:
		return nil, err
	case <-timeout:
		msg := fmt.Sprintf("NFS lookup timed out after %v seconds", timeoutSecs)
		return nil, &LookupError{msg}
	}
}

func nfsLookup1(baseFH []byte,
	path string,
	c *NFSConfig,
	outC loutCh,
	errC lerrCh) {

	components := strings.Split(path, "/")
	volume, err := Lookup(baseFH, components, c)
	if err == nil {
		outC <- volume
	}
	errC <- &LookupError{fmt.Sprintf("Lookup, err: %v\n", err)}
}

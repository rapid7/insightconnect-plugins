package implementation

import "time"
import "fmt"

type woutCh chan int
type werrCh chan error

// DefaultWriteTimeoutInSec is the timeout we use for a write operation,
// unless otherwise specified.
const DefaultWriteTimeoutInSec = 10

// NFSWrite exposes the NFS write RPC to the Komand connection layer.
// It takes the NFS mount point, an array of pathname components, a
// create_if_missing flag, a remove_if_present flag, an array of lines
// to write, a timeout in seconds, and an NFSConfig instance.  It
// returns an error if anything goes wrong.
func NFSWrite(baseFH []byte,
	components []string,
	createIf bool,
	removeIf bool,
	lines []string,
	timeoutSecs int,
	c *NFSConfig) error {

	nfsOut := make(woutCh)
	nfsErr := make(werrCh)
	timeout := time.After(time.Duration(timeoutSecs) * time.Second)
	go func() {
		nfsWrite1(baseFH, components, createIf, removeIf, lines, c, nfsOut, nfsErr)
	}()
	select {
	case <-nfsOut:
		return nil
	case err := <-nfsErr:
		return err
	case <-timeout:
		msg := fmt.Sprintf("NFS write timed out after %v seconds", timeoutSecs)
		return &WriteError{msg}
	}
}

func nfsWrite1(baseFH []byte,
	components []string,
	createIf bool,
	removeIf bool,
	lines []string,
	c *NFSConfig,
	outC woutCh,
	errC werrCh) {

	err := Write(baseFH, components, createIf, removeIf, lines, c)
	if err == nil {
		outC <- 1
	}
	errC <- &WriteError{fmt.Sprintf("Write, err: %v\n", err)}
}

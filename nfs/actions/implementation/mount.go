package implementation

import "time"
import "fmt"

type moutCh chan []byte
type merrCh chan error

// NFSMount exposes the mount RPC to the Komand connection layer
func NFSMount(mountPath string, timeoutSecs int, c *NFSConfig) ([]byte, error) {
	mountOut := make(moutCh)
	mountErr := make(merrCh)
	timeout := time.After(time.Duration(timeoutSecs) * time.Second)
	go func() { nfsMount1(mountPath, c, mountOut, mountErr) }()
	select {
	case baseFileHandle := <-mountOut:
		return baseFileHandle, nil
	case err := <-mountErr:
		return nil, err
	case <-timeout:
		msg := fmt.Sprintf("NFS mount timed out after %v seconds", timeoutSecs)
		return nil, &MountError{msg}
	}
}

func nfsMount1(mountPath string, c *NFSConfig, outC moutCh, errC merrCh) {
	baseFH, err := Mount(mountPath, c)
	if err == nil {
		outC <- baseFH
	}
	errC <- &MountError{fmt.Sprintf("MountRPC, err: %v\n", err)}
}

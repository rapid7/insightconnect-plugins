package implementation

import "fmt"

// NFSProc3Remove appears in the header of an NFS remove request
const NFSProc3Remove = 12

// Remove takes the file handle of the parent directory and a name of
// the file to be removed.  It returns an error if something went
// wrong.
func Remove(dirHandle []byte, doomedName string, c *NFSConfig) error {
	nfsd, err := DialNFS("tcp", c.ClientExternalIP)
	if err == nil {
		defer nfsd.transport.Close()
		auth := GetAuthUnix(c.ClientMachineName)
		return nfsd.removeTCP(dirHandle, doomedName, auth, c)
		if err == nil {
			return nil
		}
		ctl := "removeRPC > removeTCP(%v), err: %v\n"
		return &RemoveError{fmt.Sprintf(ctl, doomedName, err)}
	}
	ctl := "removeRPC > DialNFS(%v), err: %v\n"
	return &RemoveError{fmt.Sprintf(ctl, c.ClientExternalIP, err)}
}

func (rmvr *NFSd) removeTCP(dirHandle []byte, doomedName string, auth Auth, c *NFSConfig) error {
	/*
	   args per RFC 1813:
	   struct REMOVE3args {
	     struct diropargs3 {
	       nfs_fh3   dir;
	       filename3 name;
	     };
	     diropargs3  object;
	   };
	*/
	type remover struct {
		Header
		dirHandle  []byte
		doomedName string
	}
	req :=
		&remover{
			Header{
				Rpcvers: 2,
				Prog:    NFSProg,
				Vers:    NFSVers,
				Proc:    NFSProc3Remove,
				Cred:    auth,
				Verf:    AuthNull,
			},
			dirHandle,
			doomedName,
		}
	buf, err := rmvr.RPCCallTCP(req)
	if err != nil {
		return &RemoveError{fmt.Sprintf("RPCCallTCP: %v", err)}
	}
	nfsstat, buf := XdrUint32(buf)
	errCode := NFSstat3(nfsstat)
	if errCode == NFS3OK {
		/*
		   response per RFC 1813:
		   struct REMOVE3resok {
		     // we discard the weak cache constraint data
		     // (for now all we care about is a successful op)
		     wcc_data    dir_wcc;
		   };
		*/
		return nil
	}
	return SpecializeNFSError(errCode, "remove")
}

// The RemoveError struct represents an error that occurs during an NFS
// create operation, outside of shared NFS errors.
type RemoveError struct {
	ErrorString string
}

func (err *RemoveError) Error() string { return err.ErrorString }

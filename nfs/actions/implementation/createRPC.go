package implementation

import "fmt"
import "bytes"

// NFSProc3Create appears in the header of an NFS create request
const NFSProc3Create = 8

// CreateHow3Unchecked instructs the NFS server not to create the file
// if one of that name already exists.  The other "create how" modes
// (GUARDED and EXCLUSIVE) are not implemented in this plugin.
const CreateHow3Unchecked = 0

// Create takes the file handle of the parent directory and a name of
// the desired file.  It returns the file handle of the newly-created
// file, or an error if something went wrong.
func Create(parentFH []byte, newName string, c *NFSConfig) ([]byte, error) {
	nfsd, err := DialNFS("tcp", c.ClientExternalIP)
	if err == nil {
		defer nfsd.transport.Close()
		auth := GetAuthUnix(c.ClientMachineName)
		newHandle, err := nfsd.createTCP(parentFH, newName, auth, c)
		if err == nil {
			return newHandle, nil
		}
		ctl := "createRPC > createTCP(%v), err: %v\n"
		return nil, &CreateError{fmt.Sprintf(ctl, newName, err)}
	}
	ctl := "createRPC > DialNFS(%v), err: %v\n"
	return nil, &CreateError{fmt.Sprintf(ctl, c.ClientExternalIP, err)}
}

// Perm holds the desired permission bits for a newly-created file.
var Perm = ModeOwnRead | ModeOwnWrite | ModeGroupRead | ModeOtherRead

// SattrsForCreate is a dumbed-down sattr3 structure that onlhy lets
// us set the file permssions bits.  And as of 2/13/17, even that
// doesn't work : - (
type SattrsForCreate struct {
	SetMode3 uint32
	NewMode3 uint32
	SetUID3  uint32
	SetGID3  uint32
	SetSize3 uint32
	SetAtime uint32
	SetMtime uint32
}

func (crtr *NFSd) createTCP(parentFH []byte, newName string, auth Auth, c *NFSConfig) ([]byte, error) {
	/*
	   args per RFC 1813:
	   struct CREATE3args {
	     struct diropargs3 {
	       nfs_fh3   dir;
	       filename3 name;
	     };
	     diropargs3  where;
	     createhow3  how;
	     sattr3      obj_attributes;
	   };
	*/
	type creator struct {
		Header
		parentFH  []byte
		newName   string
		createHow uint32
		Sattrs    SattrsForCreate
	}
	req :=
		&creator{
			Header{
				Rpcvers: 2,
				Prog:    NFSProg,
				Vers:    NFSVers,
				Proc:    NFSProc3Create,
				Cred:    auth,
				Verf:    AuthNull,
			},
			parentFH,
			newName,
			CreateHow3Unchecked,

			// Setting NewMode3 to Perm doesn't work.  in
			// GUARDED MODE, the newly created file ends
			// up with no permissions.  In UNCHECKED MODE,
			// the file ends up as 755 whatever we specify
			// here.  TODO: fix by implementing SetAttributes
			SattrsForCreate{SetMode3: uint32(1), NewMode3: uint32(Perm)},
		}
	buf, err := crtr.RPCCallTCP(req)
	if err != nil {
		return nil, &CreateError{fmt.Sprintf("RPCCallTCP: %v", err)}
	}
	nfsstat, buf := XdrUint32(buf)
	errCode := NFSstat3(nfsstat)
	if errCode == NFS3OK {
		if len(buf) == 0 {
			msg := "successful CREATE response, but NFS3ErrEmpty"
			return nil, &CreateError{msg}
		}
		newHandle, err := crtr.createSuccess(buf)
		if err == nil {
			return newHandle, nil
		}
		return nil, err
	}
	return nil, SpecializeNFSError(errCode, "create")
}

func (crtr *NFSd) createSuccess(buf []byte) ([]byte, error) {
	/*
			   response per RFC 1813:
		           struct CREATE3resok {
		             post_op_fh3   obj;
		             post_op_attr  obj_attributes;
		             // we discard the weak cache constraint data (for now)
		             wcc_data      dir_wcc;
		          };
	*/
	drdr := bytes.NewReader(buf)
	var fileHandle []byte
	var errIfAny error
Receiver:
	switch true {
	case true:
		fileHandle, errIfAny = ReceiveHandle(drdr, "create")
		if errIfAny != nil {
			break Receiver
		}
		// we discard the new file's attributes (but may need them someday)
		_, errIfAny = ReceiveAttributes(drdr, "create")
		if errIfAny != nil {
			break Receiver
		}
	}
	if errIfAny != nil {
		return nil, errIfAny
	}
	return fileHandle, nil
}

// The CreateError struct represents an error that occurs during an NFS
// create operation, outside of shared NFS errors.
type CreateError struct {
	ErrorString string
}

func (err *CreateError) Error() string { return err.ErrorString }

package implementation

import "bytes"
import "encoding/binary"
import "fmt"

// NFSProc3Lookup appears in the header of an NFS lookup request
const NFSProc3Lookup = 3

// Lookup takes a slice of strings and applies the NFS lookup
// operation to each in sequence.  If lookup fails for any string in
// the sequence, Lookup returns an error.  Otherwise, Lookup returns a
// Volume struct containing the final file handle.  If the file does
// not exist, but its parent dircetory does, Lookup returns a Volume
// containing the handle of the parent dir, and whose Nonexistent
// property is true.
func Lookup(baseFH []byte, components []string, c *NFSConfig) (*Volume, error) {
	nfsd, err := DialNFS("tcp", c.ClientExternalIP)
	if err == nil {
		defer nfsd.transport.Close()
		auth := GetAuthUnix(c.ClientMachineName)
		volume, err := nfsd.lookupTCP(baseFH, components, auth)
		if err == nil {
			return volume, nil
		}
		ctl := "lookupRPC > lookupTCP(%v), err: %v\n"
		return nil, &LookupError{fmt.Sprintf(ctl, components, err)}
	}
	ctl := "LookupRPC > DialNFS(%v), err: %v\n"
	return nil, &LookupError{fmt.Sprintf(ctl, c.ClientExternalIP, err)}
}

func (look *NFSd) lookupTCP(baseFH []byte, components []string, auth Auth) (*Volume, error) {
	parentFH := []byte{}
	resFH := baseFH
	attrs := &Fattr3{}
	filename := ""
	for i := 0; i < len(components); i++ {
		curFH, curAttrs, nfsErr := look.lookupTCP1(resFH, components[i], auth)
		if nfsErr == nil {
			parentFH = resFH
			resFH = curFH
			attrs = curAttrs
			filename = components[i]
		} else if nfsErr.Code() == NFS3ErrNoent && i == len(components)-1 {
			// for the benefit of "create if missing" parameter in write action
			return &Volume{Name: components[i], ParentFH: resFH, Nonexistent: true}, nil
		} else {
			return nil, nfsErr
		}
	}
	return &Volume{Name: filename, FH: resFH, Attrs: attrs, ParentFH: parentFH}, nil
}

func (look *NFSd) lookupTCP1(curFH []byte, component string, auth Auth) ([]byte, *Fattr3, INFSError) {
	/*
	  args per RFC 1813:
	  struct LOOKUP3args {
	    struct diropargs3 {
	      nfs_fh3   dir;
	      filename3 name;
	    };
	  };
	*/
	type looker struct {
		Header
		FH        []byte
		component string
	}
	req :=
		&looker{
			Header{
				Rpcvers: 2,
				Prog:    NFSProg,
				Vers:    NFSVers,
				Proc:    NFSProc3Lookup,
				Cred:    auth,
				Verf:    AuthNull,
			},
			curFH,
			component,
		}
	buf, err := look.RPCCallTCP(req)
	if err != nil {
		return nil, nil, &NFSError{err.Error(), NFS3ErrElsewhere}
	}
	nfsstat, buf := XdrUint32(buf)
	errCode := NFSstat3(nfsstat)
	if errCode == NFS3OK {
		if len(buf) == 0 {
			return nil, nil, &NFSError{"NFS3ErrEmpty", NFS3ErrEmpty}
		}
		fh, attrs := look.lookupSuccess(buf)
		return fh, attrs, nil
	}
	return nil, nil, SpecializeNFSError(errCode, "lookup")
}

func (look *NFSd) lookupSuccess(buf []byte) ([]byte, *Fattr3) {
	/*
	  response per RFC 1813:
	  struct LOOKUP3resok {
	    nfs_fh3      object;
	    post_op_attr obj_attributes;
	    post_op_attr dir_attributes;
	  };
	*/
	// read the file handle
	fh, buf := XdrOpaque(buf)
	attrs := Fattr3{}
	attrsFollow, buf := XdrUint32(buf)
	if attrsFollow == 1 {
		// read the file attributes (a.k.a. "object attributes")
		rdr := bytes.NewReader(buf)
		XdrRead(rdr, &attrs)
		binary.Read(rdr, binary.BigEndian, &attrsFollow)
		if attrsFollow == 1 {
			// we discard the dir attributes (but may need them someday)
			XdrRead(rdr, &Fattr3{})
		}
	}
	return fh, &attrs
}

// The LookupError struct represents an error that occurs during an NFS
// lookup operation, outside of shared NFS errors.
type LookupError struct {
	ErrorString string
}

func (err *LookupError) Error() string { return err.ErrorString }

package implementation

import "fmt"

// NFSProc3Write appears in the header of an NFS write request
const NFSProc3Write = 7

type writeState struct {
	baseFH          []byte
	fileHandle      []byte
	offset          uint64
	components      []string
	createIfMissing bool
	removeIfPresent bool
	lines           []string
	auth            Auth
	config          *NFSConfig
}

// Write takes the NFS mount point, an array of pathname components, a
// create_if_missing flag, a remove_if_present flag, and an array of
// lines to write.  It returns an error if anything goes wrong.
func Write(baseFH []byte, components []string, createIf bool, removeIf bool, lines []string, c *NFSConfig) error {
	nfsd, err := DialNFS("tcp", c.ClientExternalIP)
	if err == nil {
		defer nfsd.transport.Close()
		auth := GetAuthUnix(c.ClientMachineName)
		state := writeState{
			baseFH:          baseFH,
			components:      components,
			createIfMissing: createIf,
			removeIfPresent: removeIf,
			lines:           lines,
			auth:            auth,
			config:          c,
		}
		err := heedExistenceLogic(&state)
		if err != nil {
			ctl := "writeRPC > heedExistenceLogic(), err: %v\n"
			return &WriteError{fmt.Sprintf(ctl, err)}
		}
		err = nfsd.writeTCP(&state)
		if err == nil {
			return nil
		}
		firstLine := "no data"
		if len(state.lines) > 0 {
			firstLine = state.lines[0]
			if len(firstLine) > 20 {
				firstLine = firstLine[:20] + "..."
			}
		}
		ctl := "writeRPC > writeTCP(%v), err: %v\n"
		return &WriteError{fmt.Sprintf(ctl, firstLine, err)}
	}
	ctl := "writeRPC > DialNFS(%v), err: %v\n"
	return &WriteError{fmt.Sprintf(ctl, c.ClientExternalIP, err)}
}

func heedExistenceLogic(s *writeState) error {
	volume, err := Lookup(s.baseFH, s.components, s.config)
	if err != nil {
		ctl := "Lookup, err: %v"
		return &WriteError{fmt.Sprintf(ctl, err)}
	}
	if volume.Nonexistent {
		if s.createIfMissing {
			newFH, err := Create(volume.ParentFH, volume.Name, s.config)
			if err != nil {
				ctl := "create_if_missing: could not create new file for write (%v), err: %v"
				return &WriteError{fmt.Sprintf(ctl, volume.Name, err)}
			}
			s.fileHandle = newFH
		} else {
			ctl := "file for write (%v) unexpectedly does not exist"
			return &WriteError{fmt.Sprintf(ctl, volume.Name)}
		}
	} else {
		if s.removeIfPresent {
			err := Remove(volume.ParentFH, volume.Name, s.config)
			if err != nil {
				ctl := "could not remove file (%v) before write, err: %v"
				return &WriteError{fmt.Sprintf(ctl, volume.Name, err)}
			}
			newFH, err := Create(volume.ParentFH, volume.Name, s.config)
			if err != nil {
				ctl := "remove_if_present: could not create zero-length file for write (%v), err: %v"
				return &WriteError{fmt.Sprintf(ctl, volume.Name, err)}
			}
			s.fileHandle = newFH
		} else {
			s.offset = uint64(volume.Attrs.Size)
			s.fileHandle = volume.FH
		}
	}
	return nil
}

func (wtr *NFSd) writeTCP(s *writeState) error {
	buf := []byte{}
	for _, line := range s.lines {
		for len(line) > 0 {
			left := s.config.WriteChunkSize - uint32(len(buf))
			if uint32(len(line)) >= left {
				buf = append(buf, line[:left]...)
				err := wtr.writeTCP1(buf, s)
				if err != nil {
					ctl := "writeTCP1(full), %v"
					return &WriteError{fmt.Sprintf(ctl, err)}
				}
				buf = []byte{}
				line = line[left:]
			} else {
				buf = append(buf, line...)
				line = ""
			}
		}
		left := s.config.WriteChunkSize - uint32(len(buf))
		delimLen := uint32(len(s.config.WriteDelimiter))
		if left >= delimLen {
			buf = append(buf, s.config.WriteDelimiter...)
		} else {
			buf = append(buf, s.config.WriteDelimiter[:left]...)
			err := wtr.writeTCP1(buf, s)
			if err != nil {
				ctl := "writeTCP1(newline), %v"
				return &WriteError{fmt.Sprintf(ctl, err)}
			}
			buf = []byte{}
			buf = append(buf, s.config.WriteDelimiter[left:]...)
		}
	}
	if len(buf) > 0 {
		err := wtr.writeTCP1(buf, s)
		if err != nil {
			ctl := "writeTCP1(extra), %v"
			return &WriteError{fmt.Sprintf(ctl, err)}
		}
	}
	return nil
}

func (wtr *NFSd) writeTCP1(buf []byte, s *writeState) error {
	/*
	   args per RFC 1813:
	   struct WRITE3args {
	     nfs_fh3     file;
	     offset3     offset;
	     count3      count;
	     stable_how  stable;
	     opaque      data<>;
	   };
	*/
	type writer struct {
		Header
		fileHandle []byte
		offset     uint64
		count      uint32
		stableHow  uint32
		data       []byte
	}
	req :=
		&writer{
			Header{
				Rpcvers: 2,
				Prog:    NFSProg,
				Vers:    NFSVers,
				Proc:    NFSProc3Write,
				Cred:    s.auth,
				Verf:    AuthNull,
			},
			s.fileHandle,
			s.offset,
			uint32(len(buf)),
			UnstableResponse,
			buf,
		}
	resp, err := wtr.RPCCallTCP(req)
	if err != nil {
		return &WriteError{fmt.Sprintf("RPCCallTCP: %v", err)}
	}
	nfsstat, resp := XdrUint32(resp)
	errCode := NFSstat3(nfsstat)
	if errCode == NFS3OK {
		/*
		   response per RFC 1813:
		   struct WRITE3resok {
		     wcc_data    file_wcc;
		     count3      count;
		     stable_how  committed;
		     writeverf3  verf;
		   };
		*/
		// we discard the response values
		// (for now all we care about is a successful op)
		s.offset += uint64(len(buf))
		return nil
	}
	return SpecializeNFSError(errCode, "write")
}

// The WriteError struct represents an error that occurs during an NFS
// write operation, outside of shared NFS errors.
type WriteError struct {
	ErrorString string
}

func (err *WriteError) Error() string { return err.ErrorString }

package implementation

import "bytes"
import "io"
import "encoding/binary"
import "fmt"

// NFSProc3Read appears in the header of an NFS read request
const NFSProc3Read = 6

type readState struct {
	fileHandle []byte
	numLines   int
	auth       Auth
	config     *NFSConfig
}

// Read takes an NFS filehandle and reads numLines lines, returning an
// array of byte arrays, one per line.  If numLines is -1, it reads
// the entire file.
func Read(fh []byte, numLines int, c *NFSConfig) ([][]byte, error) {
	nfsd, err := DialNFS("tcp", c.ClientExternalIP)
	if err == nil {
		defer nfsd.transport.Close()
		auth := GetAuthUnix(c.ClientMachineName)
		state := readState{
			fileHandle: fh,
			numLines:   numLines,
			auth:       auth,
			config:     c,
		}
		lines, err := nfsd.readTCP(&state)
		if err == nil {
			return lines, nil
		}
		ctl := "readRPC > readTCP(%v), err: %v\n"
		return nil, &ReadError{fmt.Sprintf(ctl, numLines, err)}
	}
	ctl := "readRPC > DialNFS(%v), err: %v\n"
	return nil, &ReadError{fmt.Sprintf(ctl, c.ClientExternalIP, err)}
}

func (rdr *NFSd) readTCP(r *readState) ([][]byte, error) {
	res := [][]byte{}
	lineIndex := 0
	offset := uint64(0)
	allLines := r.numLines == -1
	extra := []byte{}
scanFile:
	for allLines || lineIndex < r.numLines {
		chunk := make([]byte, r.config.ReadChunkSize)
		numBytes, eof, err := rdr.readTCP1(chunk, offset, r)
		if err != nil {
			return nil, &ReadError{fmt.Sprintf("readTCP1: %v", err)}
		}
		if numBytes > 0 { // 0 when, e.g., server is overloaded
			offset += uint64(numBytes)
			chunk = append(extra, chunk[0:numBytes]...)
			lines := bytes.Split(chunk, r.config.ReadDelimiter)
			for i := 0; i < len(lines)-1; i++ {
				res = append(res, lines[i])
				lineIndex++
				if !allLines && lineIndex >= r.numLines {
					extra = []byte{}
					break scanFile
				}
			}
			extra = lines[len(lines)-1]
			if eof {
				break scanFile
			}
		}
	}
	if len(extra) > 0 {
		res = append(res, extra)
	}
	return res, nil
}

func (rdr *NFSd) readTCP1(chunk []byte, offset uint64, r *readState) (uint32, bool, error) {
	/*
	  args per RFC 1813:
	  struct READ3args {
	    nfs_fh3  file;
	    offset3  offset;
	    count3   count;
	  };
	*/
	type reader struct {
		Header
		FH     []byte
		offset uint64
		count  uint32
	}
	req :=
		&reader{
			Header{
				Rpcvers: 2,
				Prog:    NFSProg,
				Vers:    NFSVers,
				Proc:    NFSProc3Read,
				Cred:    r.auth,
				Verf:    AuthNull,
			},
			r.fileHandle,
			offset,
			r.config.ReadChunkSize,
		}
	buf, err := rdr.RPCCallTCP(req)
	if err != nil {
		return 0, false, &ReadError{fmt.Sprintf("RPCCallTCP: %v", err)}
	}
	nfsstat, buf := XdrUint32(buf)
	errCode := NFSstat3(nfsstat)
	if errCode == NFS3OK {
		if len(buf) == 0 {
			msg := "successful READ response, but NFS3ErrEmpty"
			return 0, false, &ReadError{msg}
		}
		dcount, eof, err := rdr.readSuccess(buf, chunk)
		if err == nil {
			return dcount, eof, nil
		}
		ctl := "error processing successful response: %v"
		return 0, false, &ReadError{fmt.Sprintf(ctl, err)}
	}
	return 0, false, SpecializeNFSError(errCode, "read")
}

func (rdr *NFSd) readSuccess(buf []byte, chunk []byte) (uint32, bool, error) {
	/*
	  response per RFC 1813:
	  struct READ3resok {
	    post_op_attr   file_attributes;
	    count3         count;
	    bool           eof;
	    opaque         data<>;
	  };
	*/
	drdr := bytes.NewReader(buf)
	attrsFollow := uint32(0)
	binary.Read(drdr, binary.BigEndian, &attrsFollow)
	if attrsFollow == 1 {
		// read and discard the file attributes
		XdrRead(drdr, &Fattr3{})
	}
	// read the count of data bytes provided
	dcount := uint32(0)
	binary.Read(drdr, binary.BigEndian, &dcount)
	// read the end-of-file flag
	eofFlag := uint32(0)
	binary.Read(drdr, binary.BigEndian, &eofFlag)
	// read the length of the opaque data array
	dataLen := uint32(0)
	binary.Read(drdr, binary.BigEndian, &dataLen)
	if dcount != dataLen {
		ctl := "count mismatch, dcount: %v bytes, dataLen: %v bytes\n"
		return 0, false, &ReadError{fmt.Sprintf(ctl, dcount, dataLen)}
	}
	// read the data into the chunk buffer
	_, err := drdr.Read(chunk)
	if err != nil && err != io.EOF {
		return 0, false, &ReadError{fmt.Sprintf("io.Read: %v", err)}
	}
	return dcount, eofFlag == 1, nil
}

// The ReadError struct represents an error that occurs during an NFS
// read operation, outside of shared NFS errors.
type ReadError struct {
	ErrorString string
}

func (err *ReadError) Error() string { return err.ErrorString }

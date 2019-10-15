package implementation

// Adapted from davecheney's golang NFS client (thanks!)

// Not used in MOUNT RPCs, but wil be in NFS RPCs.

import "encoding/binary"
import "io"
import "reflect"
import "fmt"

// XdrOpaque takes as arg a slice of bytes.  It interprets the first
// four bytes of the arg as a big-endian unsigned int32 serving as
// length, and returns two values:
// (1) an opaque slice of byes of that length and
// (2) the remaining bytes in the arg.
// E.g.:
// fh, restOfBuf := XdrOpaque(buf)
// handle := nfsFh3{opaque: fh}
func XdrOpaque(b []byte) ([]byte, []byte) {
	l, b := XdrUint32(b)
	return b[:l], b[l:]
}

// XdrUint32List takes as arg a slice of bytes.  It interprets the first
// four bytes of the arg as a big-endian unsigned int32 serving as
// length, and returns two values:
// (1) a slice of big-endian uint32 values of that length (grouping
//     the buffer by 4) and
// (2) the remaining bytes in the arg.
// This is used, e.g., to get the opaque file handle from a successful
// mount operation.
func XdrUint32List(b []byte) ([]uint32, []byte) {
	l, b := XdrUint32(b)
	v := make([]uint32, l)
	for i := 0; i < int(l); i++ {
		v[i], b = XdrUint32(b)
	}
	return v, b
}

// XdrRead takes as argument an io.Reader and an object.  It expects
// to read a tree of structs whose leaves are all uint32 or uint64,
// and marshal these values into the object.  It panics if it cannot
// do so.
func XdrRead(r io.Reader, val interface{}) error {
	if err := xdrRead(r, reflect.ValueOf(val)); err != nil {
		if err == io.EOF {
			return nil
		}
		return err
	}
	return nil
}

func xdrRead(r io.Reader, v reflect.Value) error {
	if v.Kind() == reflect.Ptr {
		v = v.Elem()
	}
	switch t := v.Type(); t.Kind() {
	case reflect.Struct:
		for i := 0; i < v.NumField(); i++ {
			if err := xdrRead(r, v.Field(i)); err != nil {
				return err
			}
		}
	case reflect.Uint32:
		var val uint32
		if err := binary.Read(r, binary.BigEndian, &val); err != nil {
			return err
		}
		v.SetUint(uint64(val))
	case reflect.Uint64:
		var val uint64
		if err := binary.Read(r, binary.BigEndian, &val); err != nil {
			return err
		}
		v.SetUint(uint64(val))
	default:
		return fmt.Errorf("rpc.read: invalid type: %v ", t.String())
	}
	return nil
}

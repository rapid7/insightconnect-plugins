package implementation

// Adapted from dave cheney's golang NFS client (thanks!)

import "reflect"
import "encoding/binary"
import "fmt"
import "io"
import "bytes"

// XdrWrite marshals val into XDR format and writes to the given buffer.
func XdrWrite(b *bytes.Buffer, val interface{}) error {
	w := io.Writer(b)
	v := reflect.ValueOf(val)
	switch v.Kind() {
	case reflect.Ptr:
		v = v.Elem()
	case reflect.Struct:
		v = v
	default:
		return fmt.Errorf("rpc.Write: invalid type: %v ", v.Type().String())
	}
	for i := 0; i < v.NumField(); i++ {
		field := v.Field(i)
		switch t := field.Type(); t.Kind() {
		case reflect.Uint32:
			binary.Write(w, binary.BigEndian, uint32(field.Uint()))
		case reflect.Uint64:
			binary.Write(w, binary.BigEndian, uint64(field.Uint()))
		case reflect.Struct, reflect.Interface:
			if err := XdrWrite(b, field.Interface()); err != nil {
				return err
			}
		case reflect.String:
			l := field.Len()
			binary.Write(w, binary.BigEndian, uint32(l))
			bb := []byte(field.String())

			// pad with opaque data so the frame gets complete uint32s
			//bb = append(bb, make([]byte, l % 4)...) // BUG!  BAD DOG!
			residue := 4 - l%4
			bb = append(bb, make([]byte, residue)...)
			w.Write(bb)
		case reflect.Slice:
			switch t.Elem().Kind() {
			case reflect.Uint8:
				buf := field.Bytes()
				binary.Write(w, binary.BigEndian, uint32(len(buf)))
				w.Write(buf)

			// To suport Gids field in AUTH_UNIX (not in Dave Cheney's code)
			case reflect.Uint32:
				l := field.Len()
				binary.Write(w, binary.BigEndian, uint32(l))
				for j := 0; j < l; j++ {
					elem := uint32(field.Index(j).Uint())
					binary.Write(w, binary.BigEndian, elem)
				}
			default:
				panic("slice of unknown type " + t.Elem().Kind().String())
			}
		default:
			panic("field of unknown type " + t.Kind().String())
		}
	}
	return nil
}

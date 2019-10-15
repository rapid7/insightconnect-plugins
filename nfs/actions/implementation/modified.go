package implementation

import "reflect"
import "time"
import "strings"
import "fmt"

type coutCh chan DiffsMap
type cerrCh chan error

// DefaultModifiedTimeoutInSec is the timeout we use for the NFS
// operations supporting file_changed, unless otherwise specified.
const DefaultModifiedTimeoutInSec = 10

// NFSModified takes a file's previous attributes and returns a map of
// any that have changed.
func NFSModified(baseFH []byte,
	path string,
	prevAttrs *Fattr3,
	timeoutSecs int,
	c *NFSConfig) (DiffsMap, error) {

	nfsOut := make(coutCh)
	nfsErr := make(cerrCh)
	timeout := time.After(time.Duration(timeoutSecs) * time.Second)
	go func() { nfsModified1(baseFH, path, prevAttrs, c, nfsOut, nfsErr) }()
	select {
	case diffsOut := <-nfsOut:
		return diffsOut, nil
	case err := <-nfsErr:
		return nil, err
	case <-timeout:
		msg := fmt.Sprintf("NFS file_changed timed out after %v seconds", timeoutSecs)
		return nil, &ModifiedError{msg}
	}
}

func nfsModified1(baseFH []byte,
	path string,
	prevAttrs *Fattr3,
	c *NFSConfig,
	outC coutCh,
	errC cerrCh) {

	components := strings.Split(path, "/")
	volume, err := Lookup(baseFH, components, c)
	if err == nil {
		if volume.Nonexistent {
			errC <- &NFSError{"read: NFS3ErrNoent", NFS3ErrNoent}
		}
		outC <- CompareAttributes(prevAttrs, volume.Attrs)
	}
	errC <- &ModifiedError{fmt.Sprintf("Modified > Lookup, err: %v\n", err)}
}

type comparer struct {
	diff func(interface{}, interface{}) bool
	key  string
	post func(interface{}) interface{}
}

func noop(thing interface{}) interface{} { return thing }

func rfc3339(thing interface{}) interface{} {
	sec := int64(thing.(NFStime3).Seconds)
	nsec := int64(thing.(NFStime3).Nseconds)
	return time.Unix(sec, nsec).Format(time.RFC3339)
}

// compareUint takes into account one level of aliasing (e.g.
// implementation.Ftype3 > uint32).  Not sure if this is a bug in the
// reflect package or in my understanding of it.
func compareUint(thing1 interface{}, thing2 interface{}) bool {
	oldV := reflect.ValueOf(thing1).Uint()
	newV := reflect.ValueOf(thing2).Uint()
	same := oldV == newV
	return !same
}

func compareSpecdata(thing1 interface{}, thing2 interface{}) bool {
	one := thing1.(Specdata3)
	two := thing2.(Specdata3)
	res := one.Specdata1 == two.Specdata1
	same := res && one.Specdata2 == two.Specdata2
	return !same
}

func compareNFStime(thing1 interface{}, thing2 interface{}) bool {
	one := thing1.(NFStime3)
	two := thing2.(NFStime3)
	res := one.Seconds == two.Seconds
	same := res && one.Nseconds == two.Nseconds
	return !same
}

var comparers = map[string]comparer{
	"Ftype":  comparer{compareUint, "Type", noop},
	"Mode":   comparer{compareUint, "Permissions", noop},
	"Nlink":  comparer{compareUint, "Link Count", noop},
	"UID":    comparer{compareUint, "User ID", noop},
	"GID":    comparer{compareUint, "Group ID", noop},
	"Size":   comparer{compareUint, "Size In Bytes", noop},
	"Used":   comparer{compareUint, "Used On Disk", noop},
	"Rdev":   comparer{compareSpecdata, "Device Type", noop},
	"Fsid":   comparer{compareUint, "File System ID", noop},
	"Fileid": comparer{compareUint, "File ID", noop},

	"Atime": comparer{compareNFStime, "Access Time", rfc3339},
	"Mtime": comparer{compareNFStime, "Modify Time", rfc3339},
	"Ctime": comparer{compareNFStime, "Time Of Any Change", rfc3339},
}

// DiffsMap is the object type that represents differences between
// fields in two sets of file attributes.
type DiffsMap map[string]map[string]interface{}

// DiffEntry returns a map of a single difference in file attributes.
func DiffEntry(thing1 interface{}, thing2 interface{}) map[string]interface{} {
	return map[string]interface{}{"Old": thing1, "New": thing2}
}

// diffEntry1 does post-processing on a single difference in file
// attributes (e.g. converts Nfstime3 struct to a string)
func diffEntry1(thing1 interface{}, thing2 interface{},
	post func(interface{}) interface{}) map[string]interface{} {
	return map[string]interface{}{"Old": post(thing1), "New": post(thing2)}
}

// CompareAttributes returns a map of all differences between the two
// attributes
func CompareAttributes(oldAttrs *Fattr3, newAttrs *Fattr3) DiffsMap {
	diffs := DiffsMap{}
	oldFields := reflect.ValueOf(oldAttrs).Elem()
	newFields := reflect.ValueOf(newAttrs).Elem()
	for i := 0; i < oldFields.NumField(); i++ {
		oldF := oldFields.Field(i)
		n := oldFields.Type().Field(i).Name
		newF := newFields.FieldByName(n)
		if comparers[n].diff(oldF.Interface(), newF.Interface()) {
			diffs[comparers[n].key] = diffEntry1(oldF.Interface(), newF.Interface(), comparers[n].post)
		}
	}
	return diffs
}

// The ModifiedError struct represents an error that occurs during the
// NFS operations supporting file_changed (outside of shared NFS
// errors)
type ModifiedError struct {
	ErrorString string
}

func (err *ModifiedError) Error() string { return err.ErrorString }

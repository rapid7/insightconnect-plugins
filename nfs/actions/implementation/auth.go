package implementation

// Adapted from davecheney's golang NFS client (thanks!)

import "bytes"

// The Auth struct contains authorization to be used in an NFS
// request.  Its layout is given in RFC 1057.
type Auth struct {
	Flavor uint32
	Body   []byte
}

// AuthNull is an Auth struct that represents empty credentials.
// It is useful for performance tuning.
var AuthNull = Auth{
	0,
	[]byte{},
}

// The AuthUNIX struct represents UNIX user and group credentials.
// We write it into an Auth structure when we make an NFS request.
type AuthUNIX struct {
	Stamp             uint32
	ClientMachineName string
	UID               uint32
	Gid               uint32
	Gids              []uint32 // per RFC 1057 but not in Dave's code
}

// Auth converts an AuthUNIX instance into an Auth struct.
func (a AuthUNIX) Auth() Auth {
	w := new(bytes.Buffer)
	XdrWrite(w, a)
	bs := w.Bytes()
	auth := Auth{
		1,
		bs,
	}
	return auth
}

// GetAuthUnix returns an opaque Auth struct of flavor AuthUNIX that
// specifies the roor user.
func GetAuthUnix(client string) Auth {
	root := uint32(0)   // defensive
	group0 := uint32(0) // defensive
	auth := AuthUNIX{
		Stamp: 1,
		// We know Vagrant can mount NFS.  Wireshark listening on the
		// vboxnet0 adapter shows the following are the field values
		// Vagrant uses.  Listening on loopback verifies we are using the
		// same values when we call the golang code
		ClientMachineName: client,
		UID:               root,
		Gid:               group0,
		Gids:              []uint32{group0},
	}
	return auth.Auth()
}

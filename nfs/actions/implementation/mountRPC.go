package implementation

// Adapted from davecheney's golang NFS client (thanks!)

import "fmt"

/*
MOUNT is the first RPC we invoke.  Unlike the RPCs submitted to nfsd
(such as LOOKUP or READ), this is a "conceptual RPC" that actually
consists of two remote calls, neither of which are sent to nfsd:

(1) Get the port number of the mount service from the portmap daemon

(2) Call the mount service with a dir string to get an opaque
    filehandle representing the NFS mount point
*/

// Mount establishes an NFS mount given an NFS configuration.  It
// returns the opaque file handle of that mount point or an error.
func Mount(dirpath string, c *NFSConfig) ([]byte, error) {
	portmapper, err := DialPortmapper("tcp", c.MountExternalIP, PmapPort)
	if err == nil {
		defer portmapper.transport.Close()
		m := Mapping{Prog: MountProg, Vers: MountVers, Prot: IpprotoTCP}
		mountPort, err := portmapper.Getport(m)
		if err == nil {
			extIP := c.ClientExternalIP
			mount, err := DialMount("tcp", extIP, mountPort)
			if err == nil {
				defer mount.transport.Close()
				auth := GetAuthUnix(c.ClientMachineName)
				fh, err := mount.mountTCP(dirpath, auth)
				if err == nil {
					return fh, nil
				}
				ctl := "mountRPC > mountTCP(%v), err: %v\n"
				return nil, &MountError{fmt.Sprintf(ctl, dirpath, err)}
			}
			ctl := "mountRPC > DialMount(%v, %v), err: %v\n"
			return nil, &MountError{fmt.Sprintf(ctl, extIP, mountPort, err)}
		}
		ctl := "MountRPC > GetPort, err: %v\n"
		return nil, &MountError{fmt.Sprintf(ctl, err)}
	}
	ctl := "MountRPC > DialPortmapper(%v, %v), err: %v\n"
	return nil, &MountError{fmt.Sprintf(ctl, c.MountExternalIP, PmapPort, err)}
}

func (m *MountTransport) mountTCP(dirpath string, auth Auth) ([]byte, error) {
	type mounter struct {
		Header
		Dirpath string
	}
	req :=
		&mounter{
			Header{
				Rpcvers: 2,
				Prog:    MountProg,
				Vers:    MountVers,
				Proc:    Mountproc3Mnt,
				Cred:    auth,
				Verf:    AuthNull,
			},
			dirpath,
		}
	buf, err := m.RPCCallTCP(req)
	if err != nil {
		return nil, err
	}
	mountstat3, buf := XdrUint32(buf)
	switch mountstat3 {
	case Mnt3OK:
		if len(buf) == 0 {
			msg := "successful MOUNT response, but NFS3ErrEmpty"
			return nil, &MountError{msg}
		}
		/*
		   From RFC 1813:
		   struct mountres3_ok {
		     fhandle3   fhandle;
		     int        auth_flavors<>;
		   };
		*/
		// read the file handle (that's all we really want)
		fh, buf := XdrOpaque(buf)
		// read and discard the auth flavors (sanity check)
		_, buf = XdrUint32List(buf)

		return fh, nil
	case Mnt3errPerm:
		return nil, &MountError{"Mnt3errPerm"}
	case Mnt3errNoent:
		return nil, &MountError{"Mnt3errNoent"}
	case Mnt3errIO:
		return nil, &MountError{"Mnt3errIO"}
	case Mnt3errAcces:
		return nil, &MountError{"Mnt3errAcces"}
	case Mnt3errNotdir:
		return nil, &MountError{"Mnt3errNotdir"}
	case Mnt3errNametoolong:
		return nil, &MountError{"Mnt3errNametoolong"}
	}
	return nil, fmt.Errorf("unknown mount stat: %d", mountstat3)
}

// DialPortmapper sets up a TCP/IP connection to the portmap daemon.
func DialPortmapper(net, host string, pmapPort int) (*Portmapper, error) {
	client, err := DialTCP(net, host, pmapPort)
	if err != nil {
		return nil, err
	}
	return &Portmapper{client}, nil
}

// DialMount returns a pointer to a Mount struct representing a TCP/IP
// connection to the mount daemon.
func DialMount(net, routerIP string, mountPort int) (*MountTransport, error) {
	return dialMountTCP(net, routerIP, mountPort)
}

func dialMountTCP(net, routerIP string, mountport int) (*MountTransport, error) {

	// Setting defaultIP to the ExportIP field in NFSConfig
	// instance also works, but only in the Vagrant VM.  It does NOT
	// work from within the Docker container.
	defaultIP := ""
	trans, err := DialReservedTCP(net, defaultIP, routerIP, mountport)

	if err != nil {
		return nil, err
	}
	return &MountTransport{trans}, nil
}

// Getport calls a Portmapper instance to get the port on which
// portmap daemon is running.
func (p *Portmapper) Getport(mapping Mapping) (int, error) {
	type getport struct {
		Header
		Mapping
	}
	req := &getport{
		Header{
			Rpcvers: 2,
			Prog:    PmapProg,
			Vers:    PmapVers,
			Proc:    PmapprocGetport,
			Cred:    AuthNull,
			Verf:    AuthNull,
		},
		mapping,
	}
	buf, err := p.RPCCallTCP(req)
	if err != nil {
		return 0, err
	}
	port, _ := XdrUint32(buf)
	return int(port), nil
}

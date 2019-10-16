package implementation

// RFC 1813:
// "nfs_fh3 is the variable-length opaque object returned by the
// server on LOOKUP, CREATE, SYMLINK, MKNOD, LINK, or READDIRPLUS
// operations"

// NFS3Fhsize is the maximum size of an opaque NFS3 file handle.
const NFS3Fhsize = 64

type nfsFh3 struct {
	opaque [NFS3Fhsize]byte
}

type offset3 uint64
type count3 uint32

// NFSstat3 is the type that represents the status code returned from
// an RPC
type NFSstat3 uint32

// NFS3OK indicates a successful NFS operation; the NFS3ErrXXX
// constants indicate the kind of failure.
const (
	NFS3OK NFSstat3 = 0

	// Not owner. The operation was not allowed because the caller
	// is either not a privileged user (root) or not the owner of
	// the target of the operation.
	NFS3ErrPerm NFSstat3 = 1

	// No such file or directory. The file or directory name
	// specified does not exist.
	NFS3ErrNoent NFSstat3 = 2

	// I/O error. A hard error (for example, a disk error)
	// occurred while processing the requested operation.
	NFS3ErrIO NFSstat3 = 5

	// I/O error. No such device or address.
	NFS3ErrNxIO NFSstat3 = 6

	// Permission denied. The caller does not have the correct
	// permission to perform the requested operation. Contrast
	// this with NFS3ERR_PERM, which restricts itself to owner or
	// privileged user permission failures.
	NFS3ErrAcces NFSstat3 = 13

	// File exists. The file specified already exists.
	NFS3ErrExist NFSstat3 = 17

	// Attempt to do a cross-device hard link.
	NFS3ErrXdev NFSstat3 = 18

	// No such device.
	NFS3ErrNodev NFSstat3 = 19

	// Not a directory. The caller specified a non-directory in a
	// directory operation.
	NFS3ErrNotdir NFSstat3 = 20

	// Is a directory. The caller specified a directory in a
	// non-directory operation.
	NFS3ErrIsdir NFSstat3 = 21

	// Invalid argument or unsupported argument for an
	// operation. Two examples are attempting a READLINK on an
	// object other than a symbolic link or attempting to SETATTR
	// a time field on a server that does not support this
	// operation.
	NFS3ErrInval NFSstat3 = 22

	// File too large. The operation would have caused a file to
	// grow beyond the server's limit.
	NFS3ErrFbig NFSstat3 = 27

	// No space left on device. The operation would have caused
	// the server's file system to exceed its limit.
	NFS3ErrNospc NFSstat3 = 28

	// Read-only file system. A modifying operation was attempted
	// on a read-only file system.
	NFS3ErrRofs NFSstat3 = 30

	// Too many hard links.
	NFS3ErrMlink NFSstat3 = 31

	// The filename in an operation was too long.
	NFS3ErrNametoolong NFSstat3 = 63

	// An attempt was made to remove a directory that was not
	// empty.
	NFS3ErrNotempty NFSstat3 = 66

	// Resource (quota) hard limit exceeded. The user's resource
	// limit on the server has been exceeded
	NFS3ErrDquot NFSstat3 = 69

	// Invalid file handle. The file handle given in the arguments
	// was invalid. The file referred to by that file handle no
	// longer exists or access to it has been revoked.
	NFS3ErrStale NFSstat3 = 70

	// Too many levels of remote in path. The file handle given in
	// the arguments referred to a file on a non-local file system
	// on the server.
	NFS3ErrRemote NFSstat3 = 71

	// result is empty (jh added)
	NFS3ErrEmpty NFSstat3 = 100

	// error from elsewhere in the stack (jh added)
	NFS3ErrElsewhere NFSstat3 = 101

	// Illegal NFS file handle. The file handle failed internal
	// consistency checks.
	NFS3ErrBadhandle NFSstat3 = 10001

	// Update synchronization mismatch was detected during a
	// SETATTR operation.
	NFS3ErrNotSync NFSstat3 = 10002

	// READDIR or READDIRPLUS cookie is stale.
	NFS3ErrBadCookie NFSstat3 = 10003

	// Operation is not supported.
	NFS3ErrNotsupp NFSstat3 = 10004

	// Buffer or request is too small.
	NFS3ErrToosmall NFSstat3 = 10005

	// An error occurred on the server which does not map to any
	// of the legal NFS version 3 protocol error values.  The
	// client should translate this into an appropriate
	// error. UNIX clients may choose to translate this to EIO
	NFS3ErrServerfault NFSstat3 = 10006

	// An attempt was made to create an object of a type not
	// supported by the server.
	NFS3ErrBadtype NFSstat3 = 10007

	// The server initiated the request, but was not able to
	// complete it in a timely fashion. The client should wait and
	// then try the request with a new RPC transaction ID. For
	// example, this error should be returned from a server that
	// supports hierarchical storage and receives a request to
	// process a file that has been migrated. In this case, the
	// server should start the immigration process and respond to
	// client with this error.
	NFS3ErrJukebox NFSstat3 = 10008
)

// Ftype3 represents an NFS 3 file type.
type Ftype3 uint32

// NFS3Reg and the other NFS3XXX constants indicate which type of file
// is being operated upon.
const (
	NFS3Reg  Ftype3 = 1
	NFS3Dir  Ftype3 = 2
	NFS3Blk  Ftype3 = 3
	NFS3Chr  Ftype3 = 4
	NFS3Lnk  Ftype3 = 5
	NFS3Sock Ftype3 = 6
	NFS3FIFO Ftype3 = 7
)

// Mode3 represents an NFS 3 file access mode.
type Mode3 uint32

// UID3 represents a UNIX-style NFS 3 user identifier.
type UID3 uint32

// GID3 represents a UNIX-style NFS 3 group identifier.
type GID3 uint32

// Size3 represents a UNIX-style NFS 3 file size.
type Size3 uint64

// Fileid3 represents a UNIX-style NFS 3 file identifier.
type Fileid3 uint64

// Specdata3 represents an NFS file specification.  For a UNIX block
// special (NF3BLK) or character special (NF3CHR) file, Specdata1 and
// Specdata2 are the major and minor device numbers, respectively.
type Specdata3 struct {
	Specdata1 uint32
	Specdata2 uint32
}

// NFStime3 represents a moment in time from the perspective of the
// NFS server.
type NFStime3 struct {
	Seconds  uint32
	Nseconds uint32
}

// Fattr3 contains file and dir attributes used by NFS3
type Fattr3 struct {

	// Ftype is the type of the file. (RFC 1813 names this field
	// "type" but that's a golang keyword.)
	Ftype Ftype3

	// Mode is the protection mode bits.
	Mode Mode3

	// Nlink is the number of hard links to the file - that is,
	// the number of different names for the same file.
	Nlink uint32

	// Uid is the user ID of the owner of the file.
	UID UID3

	// Gid is the group ID of the group of the file.
	GID GID3

	// Size is the size of the file in bytes.
	Size Size3

	// Used is the number of bytes of disk space that the file
	// actually uses (which can be smaller than the size because
	// the file may have holes or it may be larger due to
	// fragmentation).
	Used Size3

	// Rdev describes the device file if the file type is NF3CHR
	// or NF3BLK (even on a non-UNIX o/s)
	Rdev Specdata3

	// Fsid is the file system identifier for the file system.
	Fsid uint64

	// Fileid is a number which uniquely identifies the file
	// within its file system (on UNIX this would be the inumber).
	Fileid Fileid3

	// Atime is the time when the file data was last accessed.
	Atime NFStime3

	// Mtime is the time when the file data was last modified.
	Mtime NFStime3

	// Ctime is the time when the attributes of the file were last
	// changed. Writing to the file changes the ctime in addition
	// to the mtime.
	Ctime NFStime3
}

// A note on boolean XDR union switches, as used in attributesFollow
// and elsewhere.  The XDR bool type is an enum, which means a uint32.
// Per RFC 1014 the following two lines are equivalent:
// bool identifier;
// enum { FALSE = 0, TRUE = 1 } identifier;

type postOpAttr struct {
	attributesFollow bool
	attributes       Fattr3
}

type preOpAttr struct {
	attributesFollow bool
	attributes       wccAttr
}

type wccData struct {
	Before preOpAttr
	After  postOpAttr
}

type wccAttr struct {
	Size  Size3
	Mtime NFStime3
	Ctime NFStime3
}

type filename3 string

// Diropargs3 represents the arguments to an NFS operation that
// affects a directory.
type Diropargs3 struct {
	Dir  nfsFh3
	Name filename3
}

// ModeSetUID is the first of the file permission bits used by NFS.
const (
	ModeSetUID     = 0x00800 // Set user ID on execution.
	ModeSetGID     = 0x00400 // Set group ID on execution.
	ModeSwapped    = 0x00200 // Save swapped text (not defined in POSIX).
	ModeOwnRead    = 0x00100 // Read permission for owner.
	ModeOwnWrite   = 0x00080 // Write permission for owner.
	ModeOwnExec    = 0x00040 // Execute/lookup permission for owner on a file/dir
	ModeGroupRead  = 0x00020 // Read permission for group.
	ModeGroupWrite = 0x00010 // Write permission for group.
	ModeGroupExec  = 0x00008 // Execute/lookup permission for group on a file/dir
	ModeOtherRead  = 0x00004 // Read permission for others.
	ModeOtherWrite = 0x00002 // Write permission for others.
	ModeOtherExec  = 0x00001 // Execute/lookup permission for others on a file/dir
)

// Unstable and friends specify how "permanent" a write operation is
// (vs how promptly it completes).
const (
	// The server is free to commit any part of the data and the
	// metadata to stable storage, including all or none, before
	// returning a reply to the client.
	UnstableResponse = 0

	// The server must commit all of the data to stable storage
	// and enough of the metadata to retrieve the data before
	// returning.
	DataSyncResponse = 1

	// The server must commit the data written plus all file
	// system metadata to stable storage before returning results.
	FileSyncResponse = 2
)

// NFSProg and NFSVers "are the RPC constants needed to call the NFS
// Version 3 service" (per RFC 1813)
const (
	NFSProg = 100003
	NFSVers = 3
)

// Package cache abstracts away the notion of where plugins cache information into
// a set of simple function calls. Currently, the cache is a wrapper around the file
// system in /var/cache, however if you need to directly interact with the filesystem
// to more easily integrate with another library, you are free to do so. You can then
// consider this a reference for how to do so correctly.
package cache

import (
	"os"
	"strings"
	"time"

	"github.com/rapid7/komand-plugin-sdk-go2/utils"
)

const cacheDir = "/var/cache/"
const lockDir = "/var/cache/lock/"
const filePerms = 0600
const lockWaitBackoff = 1 * time.Millisecond

// InvalidCacheFileName is returned when a cache file has an invalid name
type InvalidCacheFileName string

// Error implements the error interface
func (e InvalidCacheFileName) Error() string {
	return string(e)
}

// OpenCacheFile will load the provided file from /var/cache/* and return a pointer to the
// file if found, or an error if not found / something went wrong when opening. the name
// argument should not begin with a slash, and should assume it will be appended to /var/cache
// The caller is responsible for closing the file. If they don't, there could be problems.
func OpenCacheFile(name string) (*os.File, error) {
	if err := isReservedName(name); err != nil {
		return nil, err
	}

	return openFile(cacheDir + stripLeftSlash(name))
}

// RemoveCacheFile will delete the provided file from /var/cache/* and an error if something went wrong
// the name argument should not begin with a slash, and should assume it will be appended to /var/cache
func RemoveCacheFile(name string) error {
	if err := isReservedName(name); err != nil {
		return err
	}

	return os.Remove(cacheDir + stripLeftSlash(name))
}

// CheckCacheFile checks if the file exists in the cache or not
func CheckCacheFile(name string) (bool, error) {
	return utils.DoesFileExist(cacheDir + stripLeftSlash(name))
}

// LockCacheFile will lock the provided file from /var/cache/lock/* and return a boolean if the operation
// was successful or not. In the event it was not, an error may or may not be returned (always check the value first
// to know if it worked)
// the name argument should not begin with a slash, and should assume it will be appended to /var/cache
func LockCacheFile(name string) (bool, error) {
	name = lockDir + stripLeftSlash(name)
	var ok bool
	var err error
	for {
		// Spin wait until something errors, or the file becomes free
		if ok, err = utils.DoesFileExist(name); err != nil {
			// If anything went wrong checking for the file, bail out
			return false, err
		}
		// If the file did exist, we want to try again until it doesn't
		if ok {
			// Let's give the thread a nap while we wait, instead of pegging the CPU
			time.Sleep(lockWaitBackoff) // TODO should this be configurable?
			continue                    // loop back to the top, try again
		}
		// attempt an exclusive lock - if something already grabbed the file out from under us, we simply go back to waiting
		var f *os.File
		if f, err = openExclusiveFile(name); err != nil {
			if os.IsExist(err) {
				continue // The error was that the file existed - so we just keep on a'rollin
			}
			// This was another error, some legitimate problem went wrong
			return false, err
		}
		_ = f.Close() // nolint: gas
		break         // if it ever actually gets to the end of the for loop, it means we got the exclusive lock
	}
	// If we got here, we got the lock
	return true, nil
}

// UnlockCacheFile will unlock the provided file from /var/cache/lock/* and return a boolean if the operation
// was successful or not. In the event it was not, an error may or may not be returned (always check the value first
// to know if it worked)
// the name argument should not begin with a slash, and should assume it will be appended to /var/cache
// the timeout is used to mimic rate limiting - you can put an artificial pause on the current thread before it unlocks
// this will also keep any invocations of the process from obtaining the lock until it expires.
func UnlockCacheFile(name string, timeout *time.Duration) (bool, error) {
	// If a timeout was provided, we'll sleep for that long before unlocking the file
	// this is a very rudimentary rate-limiting mechanism
	if timeout != nil {
		time.Sleep(*timeout)
	}
	if err := os.Remove(lockDir + stripLeftSlash(name)); err != nil {
		return false, err
	}
	return true, nil
}

// We told them not to, but just incase they did, strip any leading slashes from the name arguments
func stripLeftSlash(name string) string {
	return strings.TrimLeft(name, "/")
}

// Makes sure you don't use any reserved terms in a name, for example a file simply called "lock" in the /var/cache directory
func isReservedName(name string) error {
	if strings.HasSuffix(name, "/lock") {
		return InvalidCacheFileName("'lock' is a reserved name in the cache, please choose a different file name")
	}
	return nil
}

// Wrapper around utils.OpenFile to bake in the right perms/flags
func openFile(name string) (*os.File, error) {
	return utils.OpenFile(name, os.O_RDWR|os.O_CREATE, filePerms)
}

// Wrapper around utils.OpenFile to bake in the right perms/flags for exclusive file locks
func openExclusiveFile(name string) (*os.File, error) {
	return utils.OpenFile(name, os.O_RDWR|os.O_CREATE|os.O_EXCL, filePerms)
}

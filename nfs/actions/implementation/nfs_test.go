package implementation

import "testing"
import "bytes"
import "strings"
import "fmt"

var testNFSConfig = NewConfig(
	testClientMachineName, // ClientMachineName
	testNfsExportIP,       // ExportIP
	testNfsRouterIP,       // ClientExternalIP
	//testHostLanIP // use default (testNfsRouterIP)
)

// testClientMachineName is used by nfsd to verify that the the
// request is coming from superuser on a well-known port.  Since we're
// running on a VM, we use the network name of the host machine.
var testClientMachineName = "localhost.localdomain"

// testNfsExportIP is the same as that used by Vagrant for its NFS
// mount points.  It's in the entry that Vagrant generates for the
// /etc/exports file on the host when setting up an NFS mount point.
var testNfsExportIP = "172.28.128.3"

// testNfsRouterIP is the same as that used by Vagrant for its NFS
// mount points.  I determined it using Wireshark.  You could also set
// VAGRANT_LOG="debug" and wade through the transcript of "vagrant
// reload".  More generally, this is known as ClientExternalIP.
var testNfsRouterIP = "172.28.128.1"

// testHostLanIP on Mac OSX can be either the host LAN IP or the
// ClientExternalIP.  To obtain the host LAN IP, do:
//   System Preferences > Network > Airport
//var testHostLanIP = "10.0.0.2"
var testHostLanIP = testNfsRouterIP

// exact bytes are empirical - may change with mountd or nfsd releases
var wantMountFH = []byte{78, 88, 0, 0, 198, 152, 169, 238, 0, 0, 0, 1, 0, 0, 0, 8, 2, 8, 38, 147, 2, 8, 38, 147}

var testMountDirpath = "/Users/jhodgkinson/Komand/nfs"

func TestMountRPC(t *testing.T) {
	got, err := Mount(testMountDirpath, &testNFSConfig)
	if err == nil {
		if bytes.Compare(got, wantMountFH) != 0 {
			ctl := "Mount got:\n  %v\nbut wanted:\n  %v\n"
			t.Errorf(ctl, got, wantMountFH)
		}
	} else {
		t.Errorf("Mount, err: %v\n", err)
	}
}

// exact bytes are empirical - may change with nfsd releases or file mods
var wantLookupFH = []byte{78, 88, 0, 0, 198, 152, 169, 238, 0, 0, 0, 1, 0, 0, 0, 8, 2, 20, 156, 219, 2, 20, 156, 219}

var testSubdir = "subdir/"
var testFilePathname = testSubdir + "test_log01.log"
var testLookupComponents = strings.Split(testFilePathname, "/")

func TestNFSLookup(t *testing.T) { // integration test
	baseFH, err := Mount(testMountDirpath, &testNFSConfig)
	if err == nil {
		got, err := Lookup(baseFH, testLookupComponents, &testNFSConfig)
		if err == nil {
			if bytes.Compare(got.FH, wantLookupFH) != 0 {
				ctl := "Lookup got:\n  %v\nbut wanted:\n  %v\n"
				t.Errorf(ctl, got.FH, wantLookupFH)
			}
		} else {
			t.Errorf("Lookup, err: %v\n", err)
		}
	} else {
		t.Errorf("Lookup > Mount, err: %v\n", err)
	}
}

var wantReadFH1 = "2016 12 13 Tue 16:27:01 EST In order to limit ourselves to a reasonable scope,"
var wantReadFH2 = "2016 12 13 Tue 16:27:02 EST the nfs plugin is best thought of as a convenient"
var wantReadFH3 = "2016 12 13 Tue 16:27:03 EST way for SysOps to read and write logfiles"

type readCase struct {
	numLines int
	data     [][]byte
}

func TestRead(t *testing.T) {
	testReadCases(t)
}

func TestReadTinyBuffer(t *testing.T) {
	defer func() { testNFSConfig.ReadChunkSize = DefaultReadChunkSize }()
	testNFSConfig.ReadChunkSize = uint32(10)
	testReadCases(t)
}

func TestReadBigBuffer(t *testing.T) {
	defer func() { testNFSConfig.ReadChunkSize = DefaultReadChunkSize }()
	testNFSConfig.ReadChunkSize = uint32(10000)
	testReadCases(t)
}

var testNested = "nested1/nested2/nested3/nested4/nested5/"
var testNestedPathname = testNested + "test_deep.log"
var testNestedComponents = strings.Split(testNestedPathname, "/")

var nestedLines = []string{
	"from nested folder",
	"month after month then spring month",
	"a song bird takes flight",
}

var nestedBytes = convertLinesToBytes(nestedLines)

func TestReadNested(t *testing.T) {
	baseFH, err := Mount(testMountDirpath, &testNFSConfig)
	if err == nil {
		volume, err := Lookup(baseFH, testNestedComponents, &testNFSConfig)
		if err == nil {
			got, err := Read(volume.FH, -1, &testNFSConfig)
			if err == nil {
				compareReadOutput(got, nestedBytes, "nested", t)
			} else {
				msg := fmt.Sprintf("Read(nested), err: %v\n", err)
				t.Errorf(msg)
			}
		} else {
			t.Errorf("Read(nested) > Lookup, err: %v\n", err)
		}
	} else {
		t.Errorf("Read(nested) > Mount, err: %v\n", err)
	}
}

func testReadCases(t *testing.T) {
	cases := []readCase{
		readCase{1, [][]byte{[]byte(wantReadFH1)}},
		readCase{2, [][]byte{[]byte(wantReadFH1), []byte(wantReadFH2)}},
		readCase{3, [][]byte{[]byte(wantReadFH1), []byte(wantReadFH2), []byte(wantReadFH3)}},
		readCase{4, [][]byte{[]byte(wantReadFH1), []byte(wantReadFH2), []byte(wantReadFH3)}},
		readCase{-1, [][]byte{[]byte(wantReadFH1), []byte(wantReadFH2), []byte(wantReadFH3)}},
	}
	baseFH, err := Mount(testMountDirpath, &testNFSConfig)
	if err == nil {
		volume, err := Lookup(baseFH, testLookupComponents, &testNFSConfig)
		if err == nil {
			for _, c := range cases {
				testOneRead(volume.FH, c, t)
			}
		} else {
			t.Errorf("Read > Lookup, err: %v\n", err)
		}
	} else {
		t.Errorf("Read > Mount, err: %v\n", err)
	}
}

func testOneRead(fileHandle []byte, c readCase, t *testing.T) {
	which := fmt.Sprintf("case %v", c.numLines)
	got, err := Read(fileHandle, c.numLines, &testNFSConfig)
	if err == nil {
		compareReadOutput(got, c.data, which, t)
	} else {
		msg := fmt.Sprintf("Read, err: %v\n", err)
		t.Errorf(msg)
	}
}

func TestTimeout(t *testing.T) {
	_, err := NFSRead([]byte{}, testFilePathname, -1, 0, &testNFSConfig)
	if err == nil {
		t.Errorf("NFSRead(0 sec) expected to time out but didn't\n")
	} else {
		if err.Error() != "NFS read timed out after 0 seconds" {
			t.Errorf("NFSRead(0 sec), err: %v\n", err)
		}
	}
}

var testCreateFilename = "test_newfile.log"
var testCreatePathname = testSubdir + testCreateFilename
var testCreateComponents = strings.Split(testCreatePathname, "/")

// exact bytes are empirical - may change with nfsd releases or file mods
var wantCreateDirHandle = []byte{78, 88, 0, 0, 198, 152, 169, 238, 0, 0, 0, 1, 0, 0, 0, 8, 2, 19, 65, 34, 2, 19, 65, 34}

// We create and remove in the same func because the golang test
// harness makes no guarantees about running tests in any order.  (Nor
// should it, say the righteous dudes.)
func TestCreateAndRemove(t *testing.T) {
	baseFH, err := Mount(testMountDirpath, &testNFSConfig)
	if err != nil {
		t.Errorf("Create > Mount, err: %v\n", err)
	}
	volume, verr := Lookup(baseFH, testCreateComponents, &testNFSConfig)
	if verr != nil {
		t.Errorf("Create > Lookup, err: %v\n", err)
	}
	if !volume.Nonexistent {
		t.Errorf("test file %v unexpectedly exists\n", testCreatePathname)
	}
	if volume.ParentFH == nil {
		t.Errorf("Create > Lookup, bad volume")
	}
	if bytes.Compare(volume.ParentFH, wantCreateDirHandle) != 0 {
		ctl := "Create got dir handle:\n  %v\nbut expected:\n  %v\n"
		t.Errorf(ctl, volume.ParentFH, wantCreateDirHandle)
	}
	_, err = Create(volume.ParentFH, testCreateFilename, &testNFSConfig)
	if err != nil {
		t.Errorf("Create, err: %v\n", err)
	}
	volume, verr = Lookup(baseFH, testCreateComponents, &testNFSConfig)
	if verr == nil {
		if volume.Nonexistent {
			t.Errorf("test file not found after Create")
		} else {
			defer testRemove(baseFH, volume, t)
		}
	} else {
		t.Errorf("problem verifying Create: %v\n", verr)
	}
}

func testRemove(baseFH []byte, volume *Volume, t *testing.T) {
	err := Remove(volume.ParentFH, testCreateFilename, &testNFSConfig)
	if err != nil {
		t.Errorf("Remove, err: %v\n", err)
	}
	volume, err = Lookup(baseFH, testCreateComponents, &testNFSConfig)
	if err != nil {
		t.Errorf("error verifying Remove, err: %v\n", err)
	}
	if !volume.Nonexistent {
		t.Errorf("test file %v exists after remove\n", testCreatePathname)
	}
}

var testWriteFilename = "test_file_to_write.log"
var testWritePathname = testSubdir + testWriteFilename
var testWriteComponents = strings.Split(testWritePathname, "/")

var writeNewLines = []string{
	"this is line 1 of a new file",
	"this is line number two of the newly-created file",
	"this is the third line of the previously non-existent file",
}

var writeNewBytes = convertLinesToBytes(writeNewLines)

var writeAppendedLines = []string{
	"this is line 4 of an existing file",
	"this is line number five of the extant file",
	"this is the sixth line of the already-present file",
}

var writeOldAndNewBytes = convertLinesToBytes(append(writeNewLines, writeAppendedLines...))

func TestWriteLifecycle(t *testing.T) {
	testWriteLifecycle1(t)
}

func testWriteLifecycle1(t *testing.T) {
	baseFH, err := Mount(testMountDirpath, &testNFSConfig)
	if err != nil {
		t.Errorf("Write > Mount, err: %v\n", err)
	}
	defer testWriteCreateIfMissing(baseFH, t)
}

func testWriteCreateIfMissing(baseFH []byte, t *testing.T) {
	err := Write(baseFH, testWriteComponents, true, false, writeNewLines, &testNFSConfig)
	if err != nil {
		t.Errorf("Write(createIfMissing), err: %v\n", err)
	}
	verfyWriteTest(baseFH, writeNewBytes, "testWriteCreateIfMissing", t)
	defer testWriteAfterCreateIfMissing(baseFH, t)
}

func testWriteAfterCreateIfMissing(baseFH []byte, t *testing.T) {
	err := Write(baseFH, testWriteComponents, true, false, writeAppendedLines, &testNFSConfig)
	if err != nil {
		t.Errorf("(1) Write(default), err: %v\n", err)
	}
	verfyWriteTest(baseFH, writeOldAndNewBytes, "testWriteAfterCreateIfMissing", t)
	defer testWriteRemoveIfPresent(baseFH, t)
}

func testWriteRemoveIfPresent(baseFH []byte, t *testing.T) {
	err := Write(baseFH, testWriteComponents, true, true, writeNewLines, &testNFSConfig)
	if err != nil {
		t.Errorf("Write(removeIfPresent), err: %v\n", err)
	}
	verfyWriteTest(baseFH, writeNewBytes, "testWriteRemoveIfPresent", t)
	defer testWriteAfterRemoveIfPresent(baseFH, t)
}

func testWriteAfterRemoveIfPresent(baseFH []byte, t *testing.T) {
	err := Write(baseFH, testWriteComponents, true, false, writeAppendedLines, &testNFSConfig)
	if err != nil {
		t.Errorf("(2) Write(default), err: %v\n", err)
	}
	verfyWriteTest(baseFH, writeOldAndNewBytes, "testWriteAfterRemoveIfPresent", t)
	defer cleanUpAfterWriteLifecycleTest(baseFH, t)
}

func cleanUpAfterWriteLifecycleTest(baseFH []byte, t *testing.T) {
	volume, err := Lookup(baseFH, testWriteComponents, &testNFSConfig)
	if err != nil {
		t.Errorf("Write > Lookup, err: %v\n", err)
	}
	err = Remove(volume.ParentFH, testWriteFilename, &testNFSConfig)
	if err != nil {
		t.Errorf("Write > Remove, err: %v\n", err)
	}
}

func verfyWriteTest(baseFH []byte, wantBytes [][]byte, which string, t *testing.T) {
	volume, err := Lookup(baseFH, testWriteComponents, &testNFSConfig)
	if err != nil {
		t.Errorf("Write > Lookup, err: %v\n", err)
	}
	if volume.Nonexistent {
		t.Errorf("Write: file (%v) unexpectedly does not exist \n", volume.Name)
	}
	gotBytes, err := Read(volume.FH, -1, &testNFSConfig)
	if err != nil {
		t.Errorf("Write > Read, err: %v\n", err)
	}
	compareReadOutput(gotBytes, wantBytes, which, t)
}

func TestWriteTinyBuffer(t *testing.T) {
	defer func() { testNFSConfig.WriteChunkSize = DefaultWriteChunkSize }()
	testNFSConfig.WriteChunkSize = uint32(10)
	testWriteLifecycle1(t)
}

func TestWriteBigBuffer(t *testing.T) {
	defer func() { testNFSConfig.WriteChunkSize = DefaultWriteChunkSize }()
	testNFSConfig.WriteChunkSize = uint32(10000)
	testWriteLifecycle1(t)
}

func convertLinesToBytes(lines []string) [][]byte {
	wantBytes := [][]byte{}
	for _, line := range lines {
		wantBytes = append(wantBytes, []byte(line))
	}
	return wantBytes
}

func compareReadOutput(got [][]byte, data [][]byte, which string, t *testing.T) {
	if len(got) != len(data) {
		readableGot := ""
		for i := 0; i < len(got); i++ {
			readableGot += string(got[i]) + "\n"
		}
		gotLen := len(got)
		wantedLen := len(data)
		ctl := "%v: Read got %v lines but expected %v, got:\n%v\n"
		t.Errorf(ctl, which, gotLen, wantedLen, readableGot)
	} else {
		for i := 0; i < len(got); i++ {
			if bytes.Compare(got[i], data[i]) != 0 {
				got := string(got[i])
				wanted := string(data[i])
				ctl := "%v, line %v: Read got:\n  %v\nbut wanted:\n  %v\n"
				t.Errorf(ctl, which, i, got, wanted)
			}
		}
	}
}

var oldAttributesForTest = Fattr3{
	Mode:  0644,
	Nlink: 1,
	UID:   110,
	Size:  12345,
	Rdev:  Specdata3{0, 1},
	Atime: NFStime3{12345, 67890},
}

var newAttributesForTest = Fattr3{
	Mode:  0777,
	Nlink: 2,
	UID:   220,
	Size:  67890,
	Rdev:  Specdata3{0, 10},
	Atime: NFStime3{24680, 13579},
}

var diffsWantedFromTest = DiffsMap{
	"Permissions":   DiffEntry(Mode3(0644), Mode3(0777)),
	"Link Count":    DiffEntry(uint32(1), uint32(2)),
	"User ID":       DiffEntry(UID3(110), UID3(220)),
	"Size In Bytes": DiffEntry(Size3(12345), Size3(67890)),
	"Device Type":   DiffEntry(Specdata3{0, 1}, Specdata3{0, 10}),
	"Access Time":   DiffEntry("1970-01-01T03:25:45Z", "1970-01-01T06:51:20Z"),
}

func TestCompareAttributes(t *testing.T) {
	got := CompareAttributes(&oldAttributesForTest, &newAttributesForTest)
	if len(got) != len(diffsWantedFromTest) {
		ctl := "length mismatch, got: %v, wanted: %v"
		t.Errorf(ctl, len(got), len(diffsWantedFromTest))
	}
	verify := func(f string, ok bool) {
		if !ok {
			t.Errorf("value mismtach in field %v", f)
		}
	}
	diffs1 := []string{
		"Permissions",
		"Link Count",
		"User ID",
		"Size In Bytes",
		"Access Time",
	}
	for _, f := range diffs1 {
		ok := got[f]["Old"] == diffsWantedFromTest[f]["Old"]
		ok = ok && got[f]["New"] == diffsWantedFromTest[f]["New"]
		verify(f, ok)
	}

	f := "Device Type"
	diffs2 := func(which string) {
		gotspec := got[f][which].(Specdata3)
		wantspec := diffsWantedFromTest[f][which].(Specdata3)
		ok := gotspec.Specdata1 == wantspec.Specdata1
		ok = ok && gotspec.Specdata2 == wantspec.Specdata2
		verify(f, ok)
	}
	diffs2("Old")
	diffs2("New")
}

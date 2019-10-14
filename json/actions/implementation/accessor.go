package implementation

// Accessor retrieves a single item within a composite JSON structure
// (i.e. a map or an array) - think "union type"
type Accessor struct {
	Key    string
	Index  int
	Depth  int
	Filter string
	Prev   *Accessor
}

var badAccessorString = "--"
var badAccessorInt = -1

// NewMapAccessor supports a linked list of Accessors
func NewMapAccessor(key string, prev Accessor) Accessor {
	return Accessor{Key: key, Index: badAccessorInt, Depth: prev.Depth + 1, Prev: &prev}
}

// NewArrayAccessor supports a linked list of Accessors
func NewArrayAccessor(index int, prev Accessor) Accessor {
	return Accessor{Key: badAccessorString, Index: index, Depth: prev.Depth + 1, Prev: &prev}
}

// NoMoreAccessors terminates a linked list of Accessors
func NoMoreAccessors() Accessor {
	return Accessor{Key: badAccessorString, Index: badAccessorInt}
}

// IsMapAccessor allows run-time switching between different retreval syntax
func IsMapAccessor(acc Accessor) bool {
	return acc.Key != badAccessorString && acc.Index == badAccessorInt
}

// IsArrayAccessor allows run-time switching between different retreval syntax
func IsArrayAccessor(acc Accessor) bool {
	return acc.Key == badAccessorString && acc.Index != badAccessorInt
}

// *** testing

// NewMA is a convenient abbreviation
func NewMA(key string, depth int) Accessor {
	return Accessor{Key: key, Index: badAccessorInt, Depth: depth}
}

// NewAA is a convenient abbreviation
func NewAA(index int, depth int) Accessor {
	return Accessor{Key: badAccessorString, Index: index, Depth: depth}
}

// IsSameAccessor allows comparison of accessors that do the same
// thing but are not pointer-eq
func IsSameAccessor(acc1 Accessor, acc2 Accessor) bool {
	same := false
	switch {
	case IsMapAccessor(acc1):
		same = IsMapAccessor(acc2) && acc1.Key == acc2.Key
	case IsArrayAccessor(acc1):
		same = IsArrayAccessor(acc2) && acc1.Index == acc2.Index
	}
	return same
}

package implementation

// Same retruns true iff. Two objects in JSON format contain the same
// data, regardless of composite type
func Same(thing1 JSON, thing2 JSON) bool {
	same := false
	switch {
	case simpleSame(thing1, thing2):
		same = true
	case MapBranch(thing1):
		same = mapCompare(thing1, thing2, false)
	case ArrayBranch(thing1):
		same = arrayCompare(thing1, thing2, false)

	// need this because Inf2JSON embeds raw data into a JSONMap
	case RawMapBranch(thing1):
		same = mapCompare(thing1, thing2, true)
	case RawArrayBranch(thing1):
		same = arrayCompare(thing1, thing2, true)
	}
	return same
}

// RawSame is asymmetrical: thing1 is ALWAYS raw (i.e. uses
// interface{} based types), whereas thing2 is ALWAYS cooked (i.e. uses
// named JSON types).  We put up with this crock because we only use it
// for testing convenience.
func RawSame(thing1 interface{}, thing2 JSON) bool {
	same := false
	switch {
	case simpleSame(thing1, thing2):
		same = true
	case RawMapBranch(thing1):
		same = mapCompare(thing1, thing2, true)
	case RawArrayBranch(thing1):
		same = arrayCompare(thing1, thing2, true)
	}
	return same
}

func mapCompare(thing1 JSON, thing2 JSON, isRaw bool) bool {
	innersame := func() bool { _, ok := thing2.(JSONMap); return ok }()
	if innersame {
		if isRaw {
			json1 := thing1.(interface{})
			json2 := thing2.(JSONMap)
			innersame = allKeyValues(json1, json2, true)
			if innersame {
				innersame = noExcessKeyValues(json1, json2, true)
			}
		} else {
			json1 := thing1.(JSONMap)
			json2 := thing2.(JSONMap)
			innersame = allKeyValues(json1, json2, false)
			if innersame {
				innersame = noExcessKeyValues(json1, json2, false)
			}
		}
	}
	return innersame
}

func allKeyValues(j interface{}, json2 JSONMap, isRaw bool) bool {
	innersame := true
	if isRaw {
		json1 := j.(map[string]interface{})
	Scan12Raw:
		for k := range json1 {
			val2, keyed := json2[k]
			if keyed {
				if !RawSame(json1[k], val2) {
					innersame = false
					break Scan12Raw
				}
			} else {
				innersame = false
				break Scan12Raw
			}
		}
	} else {
		json1 := j.(JSONMap)
	Scan12:
		for k := range json1 {
			val2, keyed := json2[k]
			if keyed {
				if !Same(json1[k], val2) {
					innersame = false
					break Scan12
				}
			} else {
				innersame = false
				break Scan12
			}
		}
	}
	return innersame
}

func noExcessKeyValues(
	j interface{}, json2 JSONMap, isRaw bool) bool {
	innersame := true
	if isRaw {
		json1 := j.(map[string]interface{})
	Scan21Raw:
		for k := range json2 {
			_, keyed := json1[k]
			if !keyed {
				innersame = false
				break Scan21Raw
			}
		}
	} else {
		json1 := j.(JSONMap)
	Scan21:
		for k := range json2 {
			_, keyed := json1[k]
			if !keyed {
				innersame = false
				break Scan21
			}
		}
	}
	return innersame
}

func arrayCompare(thing1 JSON, thing2 JSON, isRaw bool) bool {
	innersame := func() bool { _, ok := thing2.(JSONArray); return ok }()
	if innersame {
		if isRaw {
			innersame = rawArrayCompare(thing1.([]interface{}), thing2)
		} else {
			innersame = cookedArrayCompare(thing1, thing2)
		}
	}
	return innersame
}

func cookedArrayCompare(thing1 JSON, thing2 JSON) bool {
	innersame := true
	array1 := thing1.(JSONArray)
	array2 := thing2.(JSONArray)
	if len(array1) != len(array2) {
		innersame = false
	} else {
	Scan:
		for i := 0; i < len(array1); i++ {
			if !Same(array1[i], array2[i]) {
				innersame = false
				break Scan
			}
		}
	}
	return innersame
}

func rawArrayCompare(thing1 []interface{}, thing2 JSON) bool {
	innersame := true
	array1 := thing1
	array2 := thing2.(JSONArray)
	if len(array1) != len(array2) {
		innersame = false
	} else {
	Scan:
		for i := 0; i < len(array1); i++ {
			if !RawSame(array1[i], array2[i]) {
				innersame = false
				break Scan
			}
		}
	}
	return innersame
}

func simpleSame(thing1 JSON, thing2 JSON) bool {
	simplesame := false
	switch {
	case (thing1 == nil):
		simplesame = (thing2 == nil)
	case BoolBranch(thing1):
		bool2, ok := thing2.(bool)
		simplesame = ok && (thing1.(bool) == bool2)

	// The following two cases are hairy because unmarshalled JSON only
	// provides float64s, even if the originating string had no decimal
	// point.  IOW, unmarshalling is somewhat un-go-like, I think.
	case IntBranch(thing1):
		int1 := thing1.(int)
		int2, ok := thing2.(int)
		if ok {
			simplesame = ok && (int1 == int2)
		} else {
			float2, ok := thing2.(float64)
			if ok {
				simplesame = (float64(int1) == float2)
			}
		}
	case Float64Branch(thing1):
		float1 := thing1.(float64)
		float2, ok := thing2.(float64)
		if ok {
			simplesame = ok && (float1 == float2)
		} else {
			int2, ok := thing2.(int)
			if ok {
				simplesame = (float1 == float64(int2))
			}
		}

	case StringBranch(thing1):
		string2, ok := thing2.(string)
		simplesame = ok && (thing1.(string) == string2)
	}
	return simplesame
}

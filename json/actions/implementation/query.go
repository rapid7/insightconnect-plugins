package implementation

import "regexp"

// Query retrieves an item within a nest of composite JSON structure
// (i.e. via a sequence of Accessors)
type Query []Accessor

// GetViaQuery takes JSON source and retrieves the nested item
// specified by a Query
func GetViaQuery(source JSON, query Query) JSON {
	res := source
Scan:
	for i := 0; i < len(query); i++ {
		switch {
		case IsMapAccessor(query[i]):
			if IsRaw(res) {
				if RawMapBranch(res) {
					res = accessRawMap(res, query[i])
				} else {
					res = JSON("")
					break Scan
				}
			} else {
				if MapBranch(res) {
					res = accessCookedMap(res, query[i])
				} else {
					res = JSON("")
					break Scan
				}
			}
		case IsArrayAccessor(query[i]):
			if IsRaw(res) {
				if RawArrayBranch(res) {
					res = accessRawArray(res, query[i])
				} else {
					res = JSON("")
					break Scan
				}
			} else {
				if ArrayBranch(res) {
					res = accessCookedArray(res, query[i])
				} else {
					res = JSON("")
					break Scan
				}
			}
		default:
			res = JSON("")
			break Scan
		}
	}
	return res
}

func accessRawMap(res JSON, acc Accessor) JSON {
	return applyFilter(res.(map[string]interface{})[acc.Key], acc.Filter)
}

func accessCookedMap(res JSON, acc Accessor) JSON {
	return applyFilter(res.(JSONMap)[acc.Key], acc.Filter)
}

func accessRawArray(res JSON, acc Accessor) JSON {
	return applyFilter(res.([]interface{})[acc.Index], acc.Filter)
}

func accessCookedArray(res JSON, acc Accessor) JSON {
	return applyFilter(res.(JSONArray)[acc.Index], acc.Filter)
}

func applyFilter(res JSON, filter string) JSON {
	switch {
	case filter == "":
	case ArrayBranch(res):
		oldRes := res.(JSONArray)
		newRes := JSONArray{}
		for i := 0; i < len(oldRes); i++ {
			if StringBranch(oldRes[i]) {
				oldElem := oldRes[i].(string)
				if ok, _ := regexp.MatchString("(?i)"+filter, oldElem); ok {
					newRes = append(newRes, oldElem)
				}
			}
		}
		res = newRes
	case RawArrayBranch(res):
		oldRes := res.([]interface{})
		newRes := []interface{}{}
		for i := 0; i < len(oldRes); i++ {
			if StringBranch(oldRes[i]) {
				oldElem := oldRes[i].(string)
				if ok, _ := regexp.MatchString("(?i)"+filter, oldElem); ok {
					newRes = append(newRes, oldElem)
				}
			}
		}
		res = newRes
	}
	return res
}

// IsSameQuery supports unit testing
func IsSameQuery(query1 Query, query2 Query) bool {
	same := len(query1) == len(query2)
	if same {
	Scan:
		for i := 0; i < len(query1); i++ {
			if !IsSameAccessor(query1[i], query2[i]) {
				same = false
				break Scan
			}
		}
	}
	return same
}

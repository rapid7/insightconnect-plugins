package actions

import (
	"encoding/json"
	"log"
	"regexp"
	"time"

	"github.com/rapid7/komand-plugins/fullcontact/types"
)

// Receivers - there can be only one (non-nil field, that is)
type Receivers struct {
	PersonPtr   *types.Person
	NamePtr     *types.Name
	ValidityPtr *types.Validity
}

const retryMsg = "Postprocess invoked with retry of %v seconds...\n"
const retryPreludeMsg = "Will retry '%v' after %v seconds...\n"
const retryPostludeMsg = "About to retry '%v'.\n"
const noRetryMsg = "Not retrying '%v'.\n"

const lookUpPersonFlag = "look up person"
const lookUpNameFlag = "look up name"
const validateEmailFlag = "validate email"

// Postprocess takes the marshaled JSON and parses it into a named
// struct reflecting the FullContact API
func Postprocess(marshaledJSON []byte, receivers Receivers, retryIntervalInSec int) bool {
	shouldRetry := false
	action := "unknown action"
	var unmarshalErr error
	switch {
	case receivers.PersonPtr != nil:
		action = lookUpPersonFlag
		unmarshalErr = json.Unmarshal(marshaledJSON, receivers.PersonPtr)
	case receivers.NamePtr != nil:
		action = lookUpNameFlag
		unmarshalErr = json.Unmarshal(marshaledJSON, receivers.NamePtr)
	case receivers.ValidityPtr != nil:
		action = validateEmailFlag
		unmarshalErr = json.Unmarshal(marshaledJSON, receivers.ValidityPtr)
	}
	if unmarshalErr == nil {
		switch {
		case receivers.PersonPtr != nil:
			shouldRetry = needToRetry(receivers.PersonPtr.Status, receivers.PersonPtr.Message)
		case receivers.NamePtr != nil:
			shouldRetry = needToRetry(receivers.NamePtr.Status, receivers.NamePtr.Message)
		case receivers.ValidityPtr != nil:
			shouldRetry = needToRetry(receivers.ValidityPtr.Status, receivers.ValidityPtr.Message)
		}
		if shouldRetry {
			if retryIntervalInSec > 0 {
				time.Sleep(time.Duration(retryIntervalInSec) * time.Second)
				log.Printf(retryPostludeMsg, action)
			} else {
				shouldRetry = false
			}
		}
	} else {
		log.Printf("action '%v', unmarshalErr: %v\n", action, unmarshalErr)
	}
	return shouldRetry
}

func needToRetry(status int, message string) bool {
	retry := status == 202
	if retry {
		retry, _ = regexp.MatchString("^Queued for search", message)
	}
	return retry
}

// Person holds person info
type Person struct {
	ContactInfo struct {
		Chats []struct {
			Client string `json:"client"`
			Handle string `json:"handle"`
		} `json:"chats"`
		FamilyName string `json:"familyName"`
		FullName   string `json:"fullName"`
		GivenName  string `json:"givenName"`
		Websites   []struct {
			URL string `json:"url"`
		} `json:"websites"`
	} `json:"contactInfo"`
	Demographics struct {
		Gender          string `json:"gender"`
		LocationDeduced struct {
			City struct {
				Code    string `json:"code"`
				Deduced bool   `json:"deduced"`
				Name    string `json:"name"`
			} `json:"city"`
			Continent struct {
				Code    string `json:"code"`
				Deduced bool   `json:"deduced"`
				Name    string `json:"name"`
			} `json:"continent"`
			Country struct {
				Code    string `json:"code"`
				Deduced bool   `json:"deduced"`
				Name    string `json:"name"`
			} `json:"country"`
			County struct {
				Code    string `json:"code"`
				Deduced bool   `json:"deduced"`
				Name    string `json:"name"`
			} `json:"county"`
			DeducedLocation    string `json:"deducedLocation"`
			NormalizedLocation string `json:"normalizedLocation"`
			State              struct {
				Code    string `json:"code"`
				Deduced bool   `json:"deduced"`
				Name    string `json:"name"`
			} `json:"state"`
		} `json:"locationDeduced"`
		LocationGeneral string `json:"locationGeneral"`
	} `json:"demographics"`
	DigitalFootprint struct {
		Scores []struct {
			Provider string `json:"provider"`
			Type     string `json:"type"`
			Value    int    `json:"value"`
		} `json:"scores"`
		Topics []struct {
			Provider string `json:"provider"`
			Value    string `json:"value"`
		} `json:"topics"`
	} `json:"digitalFootprint"`
	Message       string `json:"message"`
	Organizations []struct {
		Current   bool   `json:"current"`
		IsPrimary bool   `json:"isPrimary"`
		Name      string `json:"name"`
		StartDate string `json:"startDate"`
		Title     string `json:"title"`
	} `json:"organizations"`
	Photos []struct {
		IsPrimary bool   `json:"isPrimary"`
		Type      string `json:"type"`
		URL       string `json:"url"`
	} `json:"photos"`
	SocialProfiles []struct {
		Bio       string `json:"bio"`
		Followers int    `json:"followers"`
		Following int    `json:"following"`
		ID        string `json:"id"`
		Type      string `json:"type"`
		URL       string `json:"url"`
		Username  string `json:"username"`
	} `json:"socialProfiles"`
	Status int `json:"status"`
}

// Name holds name info
type Name struct {
	Message string `json:"message"`
	Name    struct {
		Family struct {
			Count int `json:"count"`
			//FrequencyRatioFloat64 string `json:"frequencyRatioFloat64"`
			FrequencyRatio float64 `json:"frequencyRatio"`
			Rank           int     `json:"rank"`
		} `json:"family"`
		Given struct {
			Count  int `json:"count"`
			Female struct {
				Age struct {
					DensityCurve struct {
						//MeanAgeFloat64 string `json:"meanAgeFloat64"`
						MeanAge float64 `json:"meanAge"`
						Mode    struct {
							Count int `json:"count"`
							//ModeAgeFloat64Array []string `json:"modeAgeFloat64Array"`
							ModeAge []float64 `json:"modeAge"`
						} `json:"mode"`
						Quartiles struct {
							/*
								Q1Float64 string `json:"q1Float64"`
								Q2Float64 string `json:"q2Float64"`
								Q3Float64 string `json:"q3Float64"`
							*/
							Q1 float64 `json:"q1"`
							Q2 float64 `json:"q2"`
							Q3 float64 `json:"q3"`
						} `json:"quartiles"`
					} `json:"densityCurve"`
				} `json:"age"`
				Count int `json:"count"`
				/*
					FrequencyRatioFloat64 string `json:"frequencyRatioFloat64"`
					LikelihoodFloat64     string `json:"likelihoodFloat64"`
				*/
				FrequencyRatio float64 `json:"frequencyRatio"`
				Likelihood     float64 `json:"likelihood"`
				Rank           int     `json:"rank"`
			} `json:"female"`
			Male struct {
				Age struct {
					DensityCurve struct {
						//MeanAgeFloat64 string `json:"meanAgeFloat64"`
						MeanAge float64 `json:"meanAge"`
						Mode    struct {
							Count int `json:"count"`
							//ModeAgeFloat64Array []string `json:"modeAgeFloat64Array"`
							ModeAge []float64 `json:"modeAge"`
						} `json:"mode"`
						Quartiles struct {
							/*
								Q1Float64 string `json:"q1Float64"`
								Q2Float64 string `json:"q2Float64"`
								Q3Float64 string `json:"q3Float64"`
							*/
							Q1 float64 `json:"q1"`
							Q2 float64 `json:"q2"`
							Q3 float64 `json:"q3"`
						} `json:"quartiles"`
					} `json:"densityCurve"`
				} `json:"age"`
				Count int `json:"count"`
				/*
					FrequencyRatioFloat64 string `json:"frequencyRatioFloat64"`
					LikelihoodFloat64     string `json:"likelihoodFloat64"`
				*/
				FrequencyRatio float64 `json:"frequencyRatio"`
				Likelihood     float64 `json:"likelihood"`
				Rank           int     `json:"rank"`
			} `json:"male"`
			Rank int `json:"rank"`
		} `json:"given"`
		Value string `json:"value"`
	} `json:"name"`
	Region string `json:"region"`
	Status int    `json:"status"`
}

// Validity holds validity info
type Validity struct {
	DisposableEmailDomain string `json:"disposableEmailDomain"`
	Message               string `json:"message"`
	Status                int    `json:"status"`
	UsernameSubAddressing string `json:"usernameSubAddressing"`
}

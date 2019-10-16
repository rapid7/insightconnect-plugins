package actions

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"time"
)

type implementationParams struct {
	ServerBase     string   // from Connection, slash-terminated
	Service        string   // URL component
	URLKeys        []string // list of URL parameters
	URLValues      []string // URL values in same order as UrlParams
	ApplicationKey string
	TimeoutInSec   int
}

// Query is the go process for accessing FullContact inside the given
// timeout interval
func Query(params implementationParams) []byte {
	jsonOut := []byte{}
	webOut := make(chan []byte, 1)
	timeout := time.After(time.Duration(params.TimeoutInSec) * time.Second)
	go func() { webFullContact(params, webOut) }()
	select {
	case jsonOut = <-webOut:
	case <-timeout:
		msg := fmt.Sprintf(`{"%v":%v}`, "TIMEOUT", 10)
		jsonOut = []byte(msg)
	}
	return jsonOut
}

func webFullContact(params implementationParams, webOut chan []byte) {
	url := ""
	url = url + params.ServerBase + params.Service
	paramsAndValues := ""
	delimiter := "?"
	for i := 0; i < len(params.URLValues); i++ {
		v := params.URLValues[i]
		if v != "" {
			paramsAndValues = paramsAndValues + delimiter + params.URLKeys[i] + "=" + v
			if delimiter == "?" {
				delimiter = "&"
			}
		}
	}
	url = url + paramsAndValues
	client := &http.Client{}
	req, newReqErr := http.NewRequest("GET", url, nil)
	if newReqErr == nil {
		req.Header.Add("X-FullContact-APIKey", params.ApplicationKey)
		resp, doReqErr := client.Do(req)
		if doReqErr == nil {
			body, readErr := ioutil.ReadAll(resp.Body)
			if readErr == nil {
				webOut <- body
			} else {
				log.Printf("readErr: %v", readErr)
			}
		} else {
			log.Printf("doReqErr: %v", doReqErr)
		}
	} else {
		log.Printf("newReqErr: %v", newReqErr)
	}
}

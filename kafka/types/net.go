package types

// Code generated by the Komand Go SDK Generator. DO NOT EDIT

// Net is a custom type generated off of the spec
type Net struct {
	KeepAlive       int `json:"keep_alive"`
	MaxOpenRequests int `json:"max_open_requests"`
	DialTimeout     int `json:"dial_timeout"`
	ReadTimeout     int `json:"read_timeout"`
	WriteTimeout    int `json:"write_timeout"`
}

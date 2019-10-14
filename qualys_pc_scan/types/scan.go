package types

import "time"

// Code generated by the Komand Go SDK Generator. DO NOT EDIT

// Scan is a custom type generated off of the spec
type Scan struct {
	Status         string    `json:"status"`
	Duration       string    `json:"duration"`
	LaunchDatetime time.Time `json:"launch_datetime"`
	Processed      int       `json:"processed"`
	ID             int       `json:"id"`
	Reference      string    `json:"reference"`
	Type           string    `json:"type"`
	Target         string    `json:"target"`
}

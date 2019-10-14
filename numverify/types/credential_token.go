package types

import "fmt"

// Code generated by the Komand Go SDK Generator. DO NOT EDIT

// CredentialToken is a special composite type, mapping to Credential-Structure: token
type CredentialToken struct {
	Token  string `json:"token"`
	Domain string `json:"domain"`
}

// String helps us prevent leaking private data to logs by accident
// by redacting private info
func (c *CredentialToken) String() string {
	return fmt.Sprintf("Token: <redacted>, Domain: %s", c.Domain)
}

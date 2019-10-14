package types

import "fmt"

// CredentialSecretKey is a special composite type, mapping to Credential-Structure: secret_key
type CredentialSecretKey struct {
	SecretKey string `json:"secretKey"`
}

// String helps us prevent leaking private data to logs by accident
// by redacting private info
func (c *CredentialSecretKey) String() string {
	return fmt.Sprintf("SecretKey: <redacted>")
}

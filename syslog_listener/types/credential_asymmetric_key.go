package types

import "fmt"

// CredentialAsymmetricKey is a special composite type, mapping to Credential-Structure: asymmetric_key
type CredentialAsymmetricKey struct {
	PrivateKey string `json:"privateKey"`
}

// String helps us prevent leaking private data to logs by accident
// by redacting private info
func (c *CredentialAsymmetricKey) String() string {
	return fmt.Sprintf("PrivateKey: <redacted>")
}

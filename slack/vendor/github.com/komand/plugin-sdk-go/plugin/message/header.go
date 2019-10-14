package message

// Header is appended to the top of every message
type Header struct {
	Version string `json:"version"` // version of messages
	Type    string `json:"type"`    // message type
}

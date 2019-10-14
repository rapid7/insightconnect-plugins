package implementation

import "github.com/rapid7/komand-plugins/office365/types"

// Office365Error represents an error accessing the Office365 REST
// API.
type Office365Error struct {
	ErrorString string
}

// Office365UnauthorizedError is a distinct object, so we can retry
// when the access token tokens expires.
var Office365UnauthorizedError = Office365Error{"REST API status 401 Unauthorized"}

func (err *Office365Error) Error() string { return err.ErrorString }

const (
	// InboxFolderID is the well-known identifer of the user's inbox
	// folder in the Office365 REST API.
	InboxFolderID = "Inbox"

	// DraftsFolderID is the well-known identifer of the user's drafts
	// folder in the Office365 REST API.
	DraftsFolderID = "Drafts"

	// SentItemsFolderID is the well-known identifer of the user's "sent items"
	// folder in the Office365 REST API.
	SentItemsFolderID = "SentItems"

	// DeletedItemsFolderID is the well-known identifer of the user's "deleted
	// items" folder in the Office365 REST API.
	DeletedItemsFolderID = "DeletedItems"
)

const (
	// LowImportance is an allowed value for the importance field of an
	// email message.
	LowImportance = "0"

	// NormalImportance is an allowed value for the importance field of an
	// email message.
	NormalImportance = "1"

	// HighImportance is am allowed value for the importance field of an
	// email message.
	HighImportance = "2"
)

const (
	// ContentTypeText indicates a mail message is in text/plain format.
	ContentTypeText = "0"

	// ContentTypeHTML indicates a mail message is in text/html format.
	ContentTypeHTML = "1"
)

// OtherFolderKey signals the plugin framework to use the
// non-enumerated field to get the folder ID.
const OtherFolderKey = "<other folder>"

// DefaultChunkForPagination is the size of a page of data when
// GetMassages and friends are exposed to the plugin framework.
const DefaultChunkForPagination = 50

// RelocateRequest contains the JSON to specify a new destination for a move or copy.
type RelocateRequest struct {
	DestinationID string `json:"DestinationId"`
}

// OpReturnValue is a union of all values returnable by access to
// Office 365 Outlook data.
type OpReturnValue struct {
	RetBool        bool
	RetString      string
	RetAttachments []types.Attachment
	RetContacts    []types.Contact
	RetFolders     []types.Folder
	RetMessages    []types.Message
}

// AssembleRecipients takes a list of email strings and converts it
// into a struct acceptable to the Office 365 REST API.
func AssembleRecipients(emails []string) []types.Recipient {
	recipients := []types.Recipient{}
	for _, email := range emails {
		address := types.EmailAddress{Address: email}
		recipient := types.Recipient{EmailAddress: address}
		recipients = append(recipients, recipient)
	}
	return recipients
}

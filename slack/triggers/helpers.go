package triggers

import (
	"github.com/levigross/grequests"
	"github.com/nlopes/slack"
)

type Message struct {
	*slack.MessageEvent
	ChannelID string `json:"channel_id"`
	UserID    string `json:"user_id"`
}

// File is a file
type File struct {
	Filename string `json:"filename"`
	Contents []byte `json:"contents"`
}

func downloadFromUrl(url string) (*File, error) {
	response, err := grequests.Get(url, nil)

	if err != nil {
		return nil, err
	}

	return &File{
		Filename: url,
		Contents: response.Bytes(),
	}, nil
}

func extractFile(file *slack.File, dst *File) error {
	url := file.URLPrivateDownload
	if url != "" {
		f, err := downloadFromUrl(url)
		if err != nil {
			return err
		}
		dst.Contents = f.Contents
		dst.Filename = f.Filename
	}

	return nil
}

package note

import (
	"encoding/json"
	"errors"
	"fmt"
	"os"
	"strings"
	"time"
)

type Note struct {
	Title  string `json:"title"`
	Content string `json:"content"`
	CreateAt time.Time `json:"created_at"`
}

func New(title, content string) (Note, error) {
	if title == "" || content == ""{
		return Note{}, errors.New("title and content can't be empty")
	}
	return Note{
		Title: title,
		Content: content,
		CreateAt: time.Now(),
	}, nil
}

func (n Note) Display() {
	fmt.Println("Title: ", n.Title)
	fmt.Println("Content: ", n.Content)
	fmt.Println("Created at: ", n.CreateAt)
}

func (n Note) Save() error {
	fileName := strings.ReplaceAll(n.Title, " ", "_")
	fileName = strings.ToLower(fileName) + ".json"

	jsonContent, err := json.Marshal(n)

	if err != nil {
		return err
	}

	return os.WriteFile(fileName, jsonContent, 0644)
}
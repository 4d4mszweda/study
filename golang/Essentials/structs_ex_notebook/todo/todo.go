package todo

import (
	"encoding/json"
	"errors"
	"fmt"
	"os"
)

type Todo struct {
	Text string `json:"text"`
}

func New(text string) (Todo, error) {
	if text == "" {
		return Todo{}, errors.New("todo can't be empty")
	}
	return Todo{
		Text: text,
	}, nil
}

func (n Todo) Display() {
	fmt.Println("Title: ", n.Text)
}

func (n Todo) Save() error {
	fileName := "todo.json"

	jsonContent, err := json.Marshal(n)

	if err != nil {
		return err
	}

	return os.WriteFile(fileName, jsonContent, 0644)
}
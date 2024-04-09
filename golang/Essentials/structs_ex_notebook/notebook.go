package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"

	"example.com/structs_ex_notebook/note"
)

// this is an golang any type
// value interface{}

func doSmt(value interface{}) {
	// type checking with switch
	switch v := value.(type) {
	case string:
		fmt.Println("String: ", v)
	case int:
		fmt.Println("Int: ", v)
	case bool:
		fmt.Println("Bool: ", v)
	default:
		fmt.Println("Unknown type")
	}

	// type check with type assertion
	typedVal, ok := value.(string)
	if ok {
		fmt.Println("String: ", typedVal)
	} else {
		fmt.Println("Unknown type")
	}
}

////GENERIC FUNCTIONS
func add[T int|float64|string](a, b T) T {
	return a + b
}

type saver interface {
	Save() error
}

type displayer interface {
	Display()
}

type outputable interface {
	// Display()
	// Save() error
	saver
	displayer
}

func main() {
	note, err := getNoteData()
	if err != nil {
		fmt.Println("Error: ", err)
		return
	}
	note.Display()

	saveData(note)
}

func saveData(s saver) error {
	err := s.Save()
	if err != nil {
		fmt.Println("Error: ", err)
		return err
	}
	return nil
}

func getNoteData() (note.Note, error) {
	title := getUserData("Note title: ")
	content := getUserData("Note content: ")

	note, err := note.New(title, content)
	
	return note, err
}

func getUserData(prompt string) (string) {
	fmt.Println(prompt)
	reader := bufio.NewReader(os.Stdin)

	text, err := reader.ReadString('\n')

	if err != nil {
		return ""
	}

	text = strings.TrimSuffix(text, "\n")
	text = strings.TrimSuffix(text, "\r")

	return text
}
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"

	"example.com/structs_ex_notebook/note"
)

func main() {
	note, err := getNoteData()
	if err != nil {
		fmt.Println("Error: ", err)
		return
	}
	note.Display()

	err = note.SaveToFile()
	if err != nil {
		fmt.Println("Error: ", err)
		return
	}
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
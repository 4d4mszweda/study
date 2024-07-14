package main

import (
	"fmt"

	"example.com/structs/user"
)

// custom type, with that i can create additional methods for basic types
type String string 

func (s String) Output() {
	fmt.Println(s)
}

func main() {
	firstName := getUserData("Please enter your first name: ")
	lastName := getUserData("Please enter your last name: ")
	birthdate := getUserData("Please enter your birthdate (MM/DD/YYYY): ")

	var s String = "Hello, World!"
	s.Output()

	// user.firstName = firstName
	// user.lastName = lastName
	// user.birthdate = birthdate
	// appUser := user{
	// 	firstName: firstName, 
	// 	lastName: lastName, 
	// 	birthdate: birthdate, 
	// 	createAt: time.Now(),
	// }
	appUser, err := user.NewUser(firstName, lastName, birthdate)

	if err != nil {
		fmt.Println(err)
		return
	}

	// ... do something awesome with that gathered data!

	// outputUserData(appUser)
	fmt.Println()
	appUser.OutputUserData()
	fmt.Println()
	appUser.UpdateFirstName("John")
	appUser.OutputUserData()

	admin, _ := user.NewAdmin("email", "password", "John", "Doe", "01/01/2000")
	fmt.Println()
	admin.OutputUserData()
}


// with big structs, it's better to pass a pointer to the struct
// func outputUserData(u *user.User) {
// 	// (*u).firstName is the same as u.firstName in Go
// 	fmt.Printf("First Name: %s\n", u.firstName)
// 	fmt.Printf("Last Name: %s\n", u.lastName)
// 	fmt.Printf("Birthdate: %s\n", u.birthdate)
// 	fmt.Printf("Created At: %s\n", u.createAt)
// }

func getUserData(promptText string) string {
	fmt.Print(promptText)
	var value string
	fmt.Scanln(&value)
	return value
}

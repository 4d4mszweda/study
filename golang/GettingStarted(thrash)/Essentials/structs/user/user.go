package user

import (
	"errors"
	"fmt"
	"time"
)

type User struct {
	firstName string
	lastName  string
	birthdate string
	createAt  time.Time
}

// you can embed a struct with additional name into another struct
// BUt if is on lowercase it will be private to the package and you can't access it and any method on it !!!!!
// type Admin struct {
// 	email string
// 	password string
// 	user User
// }


// here i can access the User struct and any method on it
// anoniymous field its like inheritance in OOP
type Admin struct {
	email string
	password string
	User
}

// factory function to create a new user struct
func NewUser(firstName, lastName, birthdate string) (*User, error) {
	if firstName == "" || lastName == "" || birthdate == "" {
		return nil, errors.New("firstName, lastName, and birthdate are required")
		
	}
	return &User{
		firstName: firstName,
		lastName:  lastName,
		birthdate: birthdate,
		createAt:  time.Now(),
	}, nil
}

func NewAdmin(email, password, firstName, lastName, birthdate string) (*Admin, error) {
	if email == "" || password == "" {
		return nil, errors.New("email and password are required")
	}
	user, err := NewUser(firstName, lastName, birthdate)
	if err != nil {
		return nil, err
	}
	return &Admin{
		email: email,
		password: password,
		User: *user,
	}, nil
}

// method on the user struct
func (u User) OutputUserData() {
	fmt.Printf("First Name: %s\n", u.firstName)
	fmt.Printf("Last Name: %s\n", u.lastName)
	fmt.Printf("Birthdate: %s\n", u.birthdate)
	fmt.Printf("Created At: %s\n", u.createAt)
}

// mutation method on the user struct, need to pass a pointer to the struct
func (u *User) UpdateFirstName(newFirstName string) {
	u.firstName = newFirstName
}

package main

import "fmt"

func displayMenu() (choice int) {
	fmt.Println("Welcome to the Bank of Golang")
	fmt.Println("What would you like to do today?")
	fmt.Println("1. Deposit")
	fmt.Println("2. Withdraw")
	fmt.Println("3. Check Balance")
	fmt.Println("4. Exit")

	fmt.Print("Enter your choice: ")
	fmt.Scanln(&choice)
	return
}
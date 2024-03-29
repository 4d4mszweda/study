package main

import (
	"errors"
	"fmt"
	"os"
	"strconv"
)

func main() {
	accountBalance, err := getBalanceFromFile()
	if err != nil {
		fmt.Println("You dont have a balance file")
		panic(err)
	}
	// infinite loop
	// for loop is only loop in golang
	// for init; condition; post {}
	// for condition {}
	// for {}
	for {
		choice := displayMenu()
		fmt.Println("You chose: ", choice)

		// if choice == 1 {
		// 	var depositAmount float64
		// 	fmt.Print("Enter the amount you want to deposit: ")
		// 	fmt.Scanln(&depositAmount)
		// 	if depositAmount <= 0 {
		// 		fmt.Println("Invalid amount")
		// 	} else{
		// 		accountBalance += depositAmount
		// 		fmt.Println("Your new account balance is: ", accountBalance)
		// 	}
		// } else if choice == 2 {
		// 	var withdrawAmount float64
		// 	fmt.Print("Enter the amount you want to withdraw: ")
		// 	fmt.Scanln(&withdrawAmount)
		// 	if withdrawAmount > accountBalance {
		// 		fmt.Println("Insufficient funds")
		// 	} else {
		// 		accountBalance -= withdrawAmount
		// 		fmt.Println("Your new account balance is: ", accountBalance)
		// 	}
		// } else if choice == 3 {
		// 	fmt.Println("Your account balance is: ", accountBalance)
		// } else {
		// 	fmt.Println("Bye!")
		// 	return
		// }
		switch choice {	
		case 1:
			var depositAmount float64
			fmt.Print("Enter the amount you want to deposit: ")
			fmt.Scanln(&depositAmount)
			if depositAmount <= 0 {
				fmt.Println("Invalid amount")
			} else{
				accountBalance += depositAmount
				fmt.Println("Your new account balance is: ", accountBalance)
				wirteBalanceToFile(accountBalance)
			}
		case 2:
			var withdrawAmount float64
			fmt.Print("Enter the amount you want to withdraw: ")
			fmt.Scanln(&withdrawAmount)
			if withdrawAmount > accountBalance {
				fmt.Println("Insufficient funds")
			} else {
				accountBalance -= withdrawAmount
				fmt.Println("Your new account balance is: ", accountBalance)
				wirteBalanceToFile(accountBalance)
			}
		case 3:
			fmt.Println("Your account balance is: ", accountBalance)
		default:
			fmt.Println("Bye!")
			return
	}
}
}

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

func wirteBalanceToFile(balance float64) {
	// convert float64 to string
	balanceTxt := fmt.Sprint(balance)
	// write to file -> os.WriteFile("filename", []byte(data string), permission code)
	// []byte(balanceTxt) -> convert string to byte collection
	os.WriteFile("balance.txt", []byte(balanceTxt), 0644)
}

// return type is float64 and error
// error must be the last return type
func getBalanceFromFile() (float64, error) {
	// read from file -> os.ReadFile("filename")
	// return type is byte collection and error
	data, err := os.ReadFile("balance.txt")
	if err != nil{
		return 0, errors.New("you dont have a balance file")
	}
	strData := string(data)
	// _ is used to ignore the vars, you infrom Go that you are not going to use the vars
	convertedData, _ := strconv.ParseFloat(strData, 64)
	return convertedData, nil
}
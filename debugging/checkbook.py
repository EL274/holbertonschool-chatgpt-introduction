#!/usr/bin/python3

def main():
    balance = 0.0
    
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        
        if action == "deposit":
            while True:
                try:
                    amount = float(input("Enter the amount to deposit: $"))
                    if amount < 0:
                        print("Please enter a positive amount.")
                    else:
                        balance += amount
                        print(f"Deposited ${amount:.2f}. New balance is ${balance:.2f}.")
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        
        elif action == "withdraw":
            while True:
                try:
                    amount = float(input("Enter the amount to withdraw: $"))
                    if amount < 0:
                        print("Please enter a positive amount.")
                    elif amount > balance:
                        print("Insufficient funds. Try a smaller amount.")
                    else:
                        balance -= amount
                        print(f"Withdrew ${amount:.2f}. New balance is ${balance:.2f}.")
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        
        elif action == "balance":
            print(f"Your current balance is ${balance:.2f}.")
        
        elif action == "exit":
            print("Exiting the checkbook program. Goodbye!")
            break
        
        else:
            print("Invalid action. Please choose from deposit, withdraw, balance, or exit.")

if __name__ == "__main__":
    main()

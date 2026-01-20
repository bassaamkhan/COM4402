# atm_refactor.py



def deposit(balance: float, amount: float):

    if amount <= 0:
        raise ValueError("Deposit amount must be positive")

    return balance + amount


def withdraw(balance: float, amount: float):

    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")

    if amount > balance:
        raise ValueError("Insufficient funds")

    return balance - amount


def show_balance(balance: float):

    return f"Current balance: £{balance:.2f}"


def atm():

    balance = 0.0

    while True:
        print("\n=== Simple ATM ===")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show balance")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount to deposit: "))
                balance = deposit(balance, amount)
            except ValueError as e:
                print("Error:", e)

        elif choice == "2":
            try:
                amount = float(input("Enter amount to withdraw: "))
                balance = withdraw(balance, amount)
            except ValueError as e:
                print("Error:", e)

        elif choice == "3":
            print(show_balance(balance))

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")



atm()

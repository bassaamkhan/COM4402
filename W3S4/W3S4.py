#practice
#1
# def atm_simple():
#     balance = 0.0
#     while True:
#         print("\n=== Simple ATM ===")
#         print("1. Deposit")
#         print("2. Withdraw")
#         print("3. Show balance")
#         print("0. Exit")
#         choice = input("Enter choice: ").strip()
#
#         if choice == "1":
#             amount = float(input("Enter deposit amount: "))
#             if amount > 0:
#                 balance += amount
#                 print(f"Deposited £{amount:.2f}")
#             else:
#                 print("Amount must be positive.")
#         elif choice == "2":
#             amount = float(input("Enter withdrawal amount: "))
#             if amount <= 0:
#                 print("Amount must be positive.")
#             elif amount > balance:
#                 print("Insufficient funds.")
#             else:
#                 balance -= amount
#                 print(f"Withdrew £{amount:.2f}")
#         elif choice == "3":
#             print(f"Current balance: £{balance:.2f}")
#         elif choice == "0":
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice, try again.")

#2
# def login_then_menu():
#     correct_user = "admin"
#     correct_pass = "python123"
#     attempts = 0
#     max_attempts = 3
#
#     # Login phase
#     while attempts < max_attempts:
#         username = input("Username: ")
#         password = input("Password: ")
#         if username == correct_user and password == correct_pass:
#             print("Login successful")
#             break
#         else:
#             print("Incorrect username or password")
#             attempts += 1
#     else:
#         print("Account locked")
#         return  # stop function
#
#     # Main menu phase
#     while True:
#         print("\n=== Main Menu ===")
#         print("1. Say hello")
#         print("2. Show username")
#         print("0. Logout")
#         choice = input("Enter choice: ").strip()
#         if choice == "1":
#             print(f"Hello, {username}!")
#         elif choice == "2":
#             print(f"Logged in as: {username}")
#         elif choice == "0":
#             print("Logging out...")
#             break
#         else:
#             print("Invalid choice.")


#3
# def marks_classification():
#     n = int(input("How many marks will you enter? "))
#     total = 0
#     fail_count = 0
#     distinction_count = 0
#
#     for i in range(1, n+1):
#         mark = int(input(f"Enter mark {i}: "))
#         total += mark
#         if mark < 40:
#             print("Fail")
#             fail_count += 1
#         elif mark >= 70:
#             print("Distinction")
#             distinction_count += 1
#         else:
#             print("Pass")
#
#     average = total / n if n > 0 else 0
#     print(f"\nTotal: {total}")
#     print(f"Average: {average:.2f}")
#     print(f"Fails: {fail_count}")
#     print(f"Distinctions: {distinction_count}")
#

#4
# def atm_with_limit():
#     balance = 100.0
#     withdrawn_today = 0.0
#     max_withdraw = 250.0
#
#     while True:
#         print("\n=== ATM with Daily Limit ===")
#         print("1. Deposit")
#         print("2. Withdraw")
#         print("3. Show balance")
#         print("4. Show withdrawn today")
#         print("0. Exit")
#         choice = input("Enter choice: ").strip()
#
#         if choice == "1":
#             amount = float(input("Enter deposit amount: "))
#             if amount > 0:
#                 balance += amount
#                 print(f"Deposited £{amount:.2f}")
#             else:
#                 print("Amount must be positive.")
#         elif choice == "2":
#             amount = float(input("Enter withdrawal amount: "))
#             if amount <= 0:
#                 print("Amount must be positive.")
#             elif amount > balance:
#                 print("Insufficient funds.")
#             elif withdrawn_today + amount > max_withdraw:
#                 print(f"Daily limit exceeded. You can withdraw up to £{max_withdraw - withdrawn_today:.2f} more today.")
#             else:
#                 balance -= amount
#                 withdrawn_today += amount
#                 print(f"Withdrew £{amount:.2f}")
#         elif choice == "3":
#             print(f"Current balance: £{balance:.2f}")
#         elif choice == "4":
#             print(f"Withdrawn today: £{withdrawn_today:.2f} / £{max_withdraw:.2f}")
#         elif choice == "0":
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice.")


#5

# def parking_meter():
#     time_minutes = 0
#     max_minutes = 120
#
#     while True:
#         print("\n=== Parking Meter ===")
#         print("1. Insert £1 (30 minutes)")
#         print("2. Insert £2 (60 minutes)")
#         print("3. Show time remaining")
#         print("0. Finish and print ticket")
#         choice = input("Enter choice: ").strip()
#
#         if choice == "1":
#             if time_minutes + 30 <= max_minutes:
#                 time_minutes += 30
#                 print("Added 30 minutes.")
#             else:
#                 time_minutes = max_minutes
#                 print("Reached maximum parking time.")
#         elif choice == "2":
#             if time_minutes + 60 <= max_minutes:
#                 time_minutes += 60
#                 print("Added 60 minutes.")
#             else:
#                 time_minutes = max_minutes
#                 print("Reached maximum parking time.")
#         elif choice == "3":
#             hours = time_minutes // 60
#             minutes = time_minutes % 60
#             print(f"Time remaining: {hours}h {minutes}m")
#         elif choice == "0":
#             hours = time_minutes // 60
#             minutes = time_minutes % 60
#             print(f"Printing ticket... Time purchased: {hours}h {minutes}m")
#             break
#         else:
#             print("Invalid choice.")


#

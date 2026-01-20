# ```python
# """
# COM4402 – While & Do-While Style Practice
# Solutions to Problems 1–10
# """
#
# # 1. Countdown to Launch
# def problem_1():
#     start = int(input("Enter starting number: "))
#
#     current = start
#     while current >= 1:
#         print(current)
#         current = current - 1
#
#     print("Lift off!")
#
#
# # 2. Sum Until Zero (Sentinel)
# def problem_2():
#     total = 0
#
#     while True:
#         num = int(input("Enter a number (0 to stop): "))
#         if num == 0:
#             break
#         total = total + num
#
#     print("Total:", total)
#
#
# # 3. Password Checker (Do-While Style)
# def problem_3():
#     correct_password = "python123"
#
#     while True:
#         pwd = input("Enter password: ")
#         if pwd == correct_password:
#             print("Access granted")
#             break
#         else:
#             print("Try again")
#
#
# # 4. Guess the Secret Number
# def problem_4():
#     secret = 17
#     guess = None
#
#     while guess != secret:
#         guess = int(input("Guess the number (1–100): "))
#         if guess < secret:
#             print("Too low")
#         elif guess > secret:
#             print("Too high")
#         else:
#             print("Well done")
#
#
# # 5. Menu Loop – Simple Calculator
# def problem_5():
#     while True:
#         print("\nSimple Calculator")
#         print("1. Add")
#         print("2. Subtract")
#         print("0. Exit")
#
#         choice = input("Enter choice: ").strip()
#
#         if choice == "0":
#             print("Goodbye!")
#             break
#         elif choice == "1":
#             a = float(input("Enter first number: "))
#             b = float(input("Enter second number: "))
#             print("Result:", a + b)
#         elif choice == "2":
#             a = float(input("Enter first number: "))
#             b = float(input("Enter second number: "))
#             print("Result:", a - b)
#         else:
#             print("Invalid choice")
#
#
# # 6. Input Validation (Positive Integer)
# def problem_6():
#     while True:
#         n = int(input("Enter a positive integer: "))
#         if n > 0:
#             print("You entered:", n)
#             break
#         else:
#             print("That is not positive, try again.")
#
#
# # 7. Average of Marks Until -1
# def problem_7():
#     total = 0
#     count = 0
#
#     while True:
#         mark = int(input("Enter mark (0–100, -1 to stop): "))
#         if mark == -1:
#             break
#         # simple check (optional)
#         if 0 <= mark <= 100:
#             total = total + mark
#             count = count + 1
#         else:
#             print("Invalid mark, ignored.")
#
#     if count > 0:
#         average = total / count
#         print("Number of marks:", count)
#         print("Average mark:", average)
#     else:
#         print("No valid marks entered.")
#
#
# # 8. Limited Login Attempts
# def problem_8():
#     correct_user = "admin"
#     correct_pass = "secret"
#     attempts = 0
#     max_attempts = 3
#
#     while attempts < max_attempts:
#         username = input("Username: ")
#         password = input("Password: ")
#
#         if username == correct_user and password == correct_pass:
#             print("Login successful")
#             return
#         else:
#             print("Incorrect username or password")
#             attempts = attempts + 1
#
#     print("Account locked")
#
#
# # 9. Bank Balance Simulator
# def problem_9():
#     balance = 100
#
#     while True:
#         print(f"\nCurrent balance: £{balance}")
#         amount = int(input("Enter withdrawal amount (0 to stop): "))
#
#         if amount == 0:
#             print("Session ended.")
#             break
#
#         if amount <= 0:
#             print("Please enter a positive amount.")
#             continue
#
#         if amount > balance:
#             print("Insufficient funds")
#         else:
#             balance = balance + (-amount)  # or: balance -= amount
#
#         if balance == 0:
#             print("Balance is now £0. No more withdrawals possible.")
#             break
#
#
# # 10. Text Menu with Do-While Style
# def problem_10():
#     last_name = None
#
#     while True:
#         print("\nName Menu")
#         print("1. Enter name")
#         print("2. Show last name entered")
#         print("0. Exit")
#
#         choice = input("Enter choice: ").strip()
#
#         if choice == "1":
#             last_name = input("Enter a name: ")
#         elif choice == "2":
#             if last_name is None:
#                 print("No name has been entered yet.")
#             else:
#                 print("Last name entered:", last_name)
#         elif choice == "0":
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice")
#
#
# # Optional menu to run any problem
# def main():
#     while True:
#         print("\nCOM4402 – While & Do-While Practice Menu")
#         print("----------------------------------------")
#         print(" 1. Countdown to Launch")
#         print(" 2. Sum Until Zero")
#         print(" 3. Password Checker")
#         print(" 4. Guess the Secret Number")
#         print(" 5. Simple Calculator Menu")
#         print(" 6. Positive Integer Validation")
#         print(" 7. Average of Marks Until -1")
#         print(" 8. Limited Login Attempts")
#         print(" 9. Bank Balance Simulator")
#         print("10. Name Menu (Do-While Style)")
#         print(" 0. Exit")
#         print("----------------------------------------")
#
#         choice = input("Enter your choice (0–10): ").strip()
#
#         if choice == "0":
#             print("Exiting...")
#             break
#         elif choice == "1":
#             problem_1()
#         elif choice == "2":
#             problem_2()
#         elif choice == "3":
#             problem_3()
#         elif choice == "4":
#             problem_4()
#         elif choice == "5":
#             problem_5()
#         elif choice == "6":
#             problem_6()
#         elif choice == "7":
#             problem_7()
#         elif choice == "8":
#             problem_8()
#         elif choice == "9":
#             problem_9()
#         elif choice == "10":
#             problem_10()
#         else:
#             print("Invalid choice, please try again.")
#
#
# if __name__ == "__main__":
#     main()
# ```


#practice

# COM4402 – While & Do-While Style Problems (1–10)

# 1. Countdown to Launch
# def countdown_to_launch():
#     start = int(input("Enter starting number: "))
#     while start >= 1:
#         print(start)
#         start -= 1
#     print("Lift off!")
#
#
# # 2. Sum Until Zero (Sentinel)
# def sum_until_zero():
#     total = 0
#     while True:
#         num = int(input("Enter a number (0 to stop): "))
#         if num == 0:
#             break
#         total += num
#     print("Total:", total)
#
#
# # 3. Password Checker (Do-While Style)
# def password_checker():
#     correct_password = "python123"
#     while True:
#         pwd = input("Enter password: ")
#         if pwd == correct_password:
#             print("Access granted")
#             break
#         else:
#             print("Try again")
#
#
# # 4. Guess the Secret Number
# def guess_secret_number():
#     secret = 17
#     guess = None
#     while guess != secret:
#         guess = int(input("Guess the number (1–100): "))
#         if guess < secret:
#             print("Too low")
#         elif guess > secret:
#             print("Too high")
#         else:
#             print("Well done")
#
#
# # 5. Menu Loop – Simple Calculator
# def simple_calculator():
#     while True:
#         print("\nSimple Calculator Menu")
#         print("1. Add")
#         print("2. Subtract")
#         print("0. Exit")
#         choice = input("Enter choice: ").strip()
#
#         if choice == "0":
#             print("Goodbye!")
#             break
#         elif choice == "1":
#             a = float(input("Enter first number: "))
#             b = float(input("Enter second number: "))
#             print("Result:", a + b)
#         elif choice == "2":
#             a = float(input("Enter first number: "))
#             b = float(input("Enter second number: "))
#             print("Result:", a - b)
#         else:
#             print("Invalid choice")
#
#
# # 6. Input Validation (Positive Integer)
# def positive_integer_input():
#     while True:
#         n = int(input("Enter a positive integer: "))
#         if n > 0:
#             print("You entered:", n)
#             break
#         else:
#             print("That is not positive, try again.")
#
#
# # 7. Average of Marks Until -1
# def average_marks():
#     total = 0
#     count = 0
#     while True:
#         mark = int(input("Enter mark (0–100, -1 to stop): "))
#         if mark == -1:
#             break
#         if 0 <= mark <= 100:
#             total += mark
#             count += 1
#         else:
#             print("Invalid mark, ignored.")
#     if count > 0:
#         print("Number of marks entered:", count)
#         print("Average mark:", total / count)
#     else:
#         print("No valid marks entered.")
#
#
# # 8. Limited Login Attempts
# def limited_login_attempts():
#     correct_user = "admin"
#     correct_pass = "secret"
#     attempts = 0
#     max_attempts = 3
#     while attempts < max_attempts:
#         username = input("Username: ")
#         password = input("Password: ")
#         if username == correct_user and password == correct_pass:
#             print("Login successful")
#             return
#         else:
#             print("Incorrect username or password")
#             attempts += 1
#     print("Account locked")
#
#
# # 9. Bank Balance Simulator
# def bank_balance_simulator():
#     balance = 100
#     while True:
#         print(f"\nCurrent balance: £{balance}")
#         amount = int(input("Enter withdrawal amount (0 to stop): "))
#         if amount == 0:
#             print("Session ended.")
#             break
#         if amount <= 0:
#             print("Please enter a positive amount.")
#             continue
#         if amount > balance:
#             print("Insufficient funds")
#         else:
#             balance -= amount
#         if balance == 0:
#             print("Balance is now £0. No more withdrawals possible.")
#             break
#
#
# # 10. Text Menu with Do-While Style
# def name_menu():
#     last_name = None
#     while True:
#         print("\nName Menu")
#         print("1. Enter name")
#         print("2. Show last name entered")
#         print("0. Exit")
#         choice = input("Enter choice: ").strip()
#         if choice == "1":
#             last_name = input("Enter a name: ")
#         elif choice == "2":
#             if last_name is None:
#                 print("No name has been entered yet.")
#             else:
#                 print("Last name entered:", last_name)
#         elif choice == "0":
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice")
#
#
# # Optional main menu to run any problem
# def main():
#     problems = {
#         "1": countdown_to_launch,
#         "2": sum_until_zero,
#         "3": password_checker,
#         "4": guess_secret_number,
#         "5": simple_calculator,
#         "6": positive_integer_input,
#         "7": average_marks,
#         "8": limited_login_attempts,
#         "9": bank_balance_simulator,
#         "10": name_menu,
#     }
#
#     while True:
#         print("\nCOM4402 – While & Do-While Practice Menu")
#         print("----------------------------------------")
#         for i in range(1, 11):
#             print(f"{i}. Problem {i}")
#         print("0. Exit")
#         choice = input("Enter your choice (0–10): ").strip()
#         if choice == "0":
#             print("Exiting...")
#             break
#         elif choice in problems:
#             problems[choice]()
#         else:
#             print("Invalid choice, please try again.")
#
#
# if __name__ == "__main__":
#     main()

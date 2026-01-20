#activity1
# def greet():
#    global message
#    message="hello from the function"
#
#
# greet()
# print(message)


# def greet():
#   message="hello from the function"
#   print(message)
#
# greet()





#activity2

# count = 0
#
# def add_one():
#     global count
#     count = count + 1
#     print("Inside:", count)
#
# add_one()
# print("outside:", count)

# count = 0
#
# def add_one(count):
#     count = count + 1
#     print("Inside:", count)
#     return count
#
# count = add_one(count)
# print("outside:", count)





#activity 3
# def area_of_rectangle(width, height):
#   area = width * height
#   return area
#
#
# w = float(input("Enter width: "))
# h = float(input("Enter height: "))
#
# result = area_of_rectangle(w, h)
# print("Area is", result)

#w, h, result are global variables because they out side of area_of_rectangle and can exist for lifetime of the program
#width,height, area are local variables because width and height are parameters and area inside of function body



#activity 4

# rate = 0.2
# def calculate_tax(amount):
#  return amount * rate
# # Version 2
# def calculate_tax(amount, rate):
#  return amount * rate

#1



# version 2 is better because the function does not rely on global state




#activity 5

# discount = 0
#
# def apply_discount(price):
#     if price > 100:
#         discount = 10
#     final_price = price - discount
#     return final_price
#
#

#corrected

# def apply_discount(price):
#  discount = 0
#  if price > 100:
#   discount = 10
#  final_price = price - discount
#  return final_price
#
#
# p = float(input("Enter price: "))
# result = apply_discount(p)
# print("Final price:", result)
#


#2
# def apply_discount(price):
#  if price > 100:
#   discount = 10
#  else:
#   discount = 0
#  return price - discount


#3
# def apply_discount(price, discount):
#  return price - discount
#
#
# p = float(input("Enter price: "))
#
# if p > 100:
#  discount = 10
# else:
#  discount = 0
#
# result = apply_discount(p, discount)
# print("Final price:", result)




#activity 6

# def show_menu():
#  print("\nATM Menu")
#  print("1. Deposit")
#  print("2. Withdraw")
#  print("0. Exit")
#  choice = input("Enter choice: ")
#  return choice
#
#
# def deposit(balance):
#  amount = float(input("Amount to deposit: "))
#  if amount > 0:
#   balance += amount
#   print(f"Deposited: {amount}")
#  else:
#   print("Error: Deposit must be positive!")
#  return balance
#
#
# def withdraw(balance):
#  amount = float(input("Amount to withdraw: "))
#  if amount <= 0:
#   print("Error: Withdrawal must be positive!")
#  elif amount > balance:
#   print("Error: Insufficient funds!")
#  else:
#   balance -= amount
#   print(f"Withdrawn: {amount}")
#  return balance


#2
# def show_menu():
#  print("\nATM Menu")
#  print("1. Deposit")
#  print("2. Withdraw")
#  print("0. Exit")
#  return input("Enter choice: ")
#
#
# # Main program
# def main():
#  balance = 1000  # local to main function
#  while True:
#   choice = show_menu()  # local variable in main
#   if choice == "1":
#    amount = float(input("Amount to deposit: "))  # local
#    balance = deposit(balance, amount)
#   elif choice == "2":
#    amount = float(input("Amount to withdraw: "))  # local
#    balance = withdraw(balance, amount)
#   elif choice == "0":
#    print("Thank you for using the ATM!")
#    break
#   else:
#    print("Invalid choice, try again.")
#   print(f"Current balance: {balance}")
#
#
# main()


#3
#function                              #lacal variables
#deposit(balance,amount)             balance, amount
#withdraw(balance,amount)           balance, amount
#show_menu()                         choice
#main()                                balance choice amount

#All variables are local to the function they are defined in.
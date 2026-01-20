"""
COM4402 – Multi-way Branching (Switch-style, match-case, and dictionaries)
Follow-along file for the "Switch Statements" lesson.

Use this file in class by UNCOMMENTING the sections you want to demonstrate.
Each block corresponds roughly to one or more slides/activities.
Requires Python 3.10+ for match/case examples.
"""

# ---------------------------------------------------------
# 0. Simple multi-way branching with if/elif/else
# ---------------------------------------------------------

# Example: choose an action based on `choice` using if/elif/else.
# This mirrors the "traditional switch" idea.

# choice = int(input("Enter a choice (1-3): "))
#
# if choice == 1:
#     print("You chose option 1 (do A)")
# elif choice == 2:
#     print("You chose option 2 (do B)")
# elif choice == 3:
#     print("You chose option 3 (do C)")
# else:
#     print("Invalid choice")


# ---------------------------------------------------------
# 1. The same idea using match / case (Python 3.10+)
# ---------------------------------------------------------

# choice = int(input("Enter a choice (1-3): "))
#
# match choice:
#     case 1:
#         print("You chose option 1 (do A)")
#     case 2:
#         print("You chose option 2 (do B)")
#     case 3:
#         print("You chose option 3 (do C)")
#     case _:
#         print("Invalid choice")


# ---------------------------------------------------------
# 2. Activity 1 – Static menu (if/elif/else)
# ---------------------------------------------------------

# With if/elif/else:
#
# print("1. Say hello")
# print("2. Say goodbye")
# print("3. Say your name")
#
# choice = int(input("Enter your choice: "))
#
# if choice == 1:
#     print("Hello!")
# elif choice == 2:
#     print("Goodbye!")
# elif choice == 3:
#     print("My name is Python.")
# else:
#     print("Invalid choice")


# ---------------------------------------------------------
# 3. Activity 1 – Static menu (match/case)
# ---------------------------------------------------------

# Same menu using match/case:

# print("1. Say hello")
# print("2. Say goodbye")
# print("3. Say your name")
#
# choice = int(input("Enter your choice: "))
#
# match choice:
#     case 1:
#         print("Hello!")
#     case 2:
#         print("Goodbye!")
#     case 3:
#         print("My name is Python.")
#     case _:
#         print("Invalid choice")


# ---------------------------------------------------------
# 4. Menu-driven calculator skeleton – if/elif/else
# ---------------------------------------------------------

# This version uses a while True loop (infinite loop) and breaks when user exits.
# Each branch is like a "case" in a switch.

# while True:
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Exit")
#
#     choice = int(input("Enter your choice: "))
#
#     if choice == 1:
#         # TODO: perform addition
#         pass
#     elif choice == 2:
#         # TODO: perform subtraction
#         pass
#     elif choice == 3:
#         # TODO: perform multiplication
#         pass
#     elif choice == 4:
#         # TODO: perform division
#         pass
#     elif choice == 5:
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice")


# ---------------------------------------------------------
# 5. Menu-driven calculator skeleton – match / case
# ---------------------------------------------------------

# Same structure, but using match/case instead of if/elif/else.

# while True:
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Exit")
#
#     choice = int(input("Enter your choice: "))
#
#     match choice:
#         case 1:
#             # TODO: perform addition
#             pass
#         case 2:
#             # TODO: perform subtraction
#             pass
#         case 3:
#             # TODO: perform multiplication
#             pass
#         case 4:
#             # TODO: perform division
#             pass
#         case 5:
#             print("Goodbye!")
#             break
#         case _:
#             print("Invalid choice")


# ---------------------------------------------------------
# 6. Filling in one case – Addition (if/elif and match)
# ---------------------------------------------------------

# Using if/elif (choice == 1):

# choice = int(input("Enter your choice: "))
#
# if choice == 1:
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     result = a + b
#     print("Result:", result)
# else:
#     print("Other choices go here")


# Using match/case:

# choice = int(input("Enter your choice: "))
#
# match choice:
#     case 1:
#         a = float(input("Enter first number: "))
#         b = float(input("Enter second number: "))
#         result = a + b
#         print("Result:", result)
#     case _:
#         print("Other choices go here")


# ---------------------------------------------------------
# 7. Complete calculator using if/elif/else
# ---------------------------------------------------------

# This version actually performs all four operations.
# Note: very basic error handling (only division by zero check).

# while True:
#     print("\nSimple Calculator (if/elif/else)")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Exit")
#
#     choice = int(input("Enter your choice: "))
#
#     if choice == 5:
#         print("Goodbye!")
#         break
#
#     if choice in (1, 2, 3, 4):
#         a = float(input("Enter first number: "))
#         b = float(input("Enter second number: "))
#
#     if choice == 1:
#         result = a + b
#         print("Result:", result)
#     elif choice == 2:
#         result = a - b
#         print("Result:", result)
#     elif choice == 3:
#         result = a * b
#         print("Result:", result)
#     elif choice == 4:
#         if b == 0:
#             print("Error: Division by zero!")
#         else:
#             result = a / b
#             print("Result:", result)
#     else:
#         print("Invalid choice")


# ---------------------------------------------------------
# 8. Complete calculator using match / case
# ---------------------------------------------------------

# Same calculator, using match/case for the multi-way branch.

# while True:
#     print("\nSimple Calculator (match/case)")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Exit")
#
#     choice = int(input("Enter your choice: "))
#
#     if choice == 5:
#         print("Goodbye!")
#         break
#
#     if choice in (1, 2, 3, 4):
#         a = float(input("Enter first number: "))
#         b = float(input("Enter second number: "))
#
#     match choice:
#         case 1:
#             result = a + b
#             print("Result:", result)
#         case 2:
#             result = a - b
#             print("Result:", result)
#         case 3:
#             result = a * b
#             print("Result:", result)
#         case 4:
#             if b == 0:
#                 print("Error: Division by zero!")
#             else:
#                 result = a / b
#                 print("Result:", result)
#         case _:
#             print("Invalid choice")


# ---------------------------------------------------------
# 9. Optional: Dictionary as a “switch”
# ---------------------------------------------------------

# Here we use a dictionary mapping numbers → functions.
# This avoids a long if/elif ladder.

# def add():
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     print("Result:", a + b)
#
#
# def subtract():
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     print("Result:", a - b)
#
#
# def multiply():
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     print("Result:", a * b)
#
#
# def divide():
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     if b == 0:
#         print("Error: Division by zero!")
#     else:
#         print("Result:", a / b)
#
#
# actions = {
#     1: add,
#     2: subtract,
#     3: multiply,
#     4: divide,
# }
#
# while True:
#     print("\nDictionary-based Calculator")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Exit")
#
#     choice = int(input("Enter your choice: "))
#
#     if choice == 5:
#         print("Goodbye!")
#         break
#
#     if choice in actions:
#         actions[choice]()  # call the selected function
#     else:
#         print("Invalid choice")


# ---------------------------------------------------------
# 10. Reflection (no code)
# ---------------------------------------------------------

# In comments or in your notes:
# - When is an if/elif/else ladder good enough?
# - When does match/case make the code clearer?
# - When might a dictionary-based "switch" be easier to maintain?








#practice

#1
# age = int(input("Enter your age: "))
#
# match age:
#     case a if a < 5:
#         print("Free entry")
#     case a if a <= 17:
#         print("Child ticket")
#     case a if a <= 64:
#         print("Adult ticket")
#     case _:
#         print("Senior ticket")

#2
# days_late = int(input("Enter days late: "))
#
# match days_late:
#     case 0:
#         print("No fine")
#     case d if 1 <= d <= 5:
#         print("Fine = £1")
#     case d if 6 <= d <= 10:
#         print("Fine = £5")
#     case _:
#         print("Fine = £10 and membership review")

#3
# colour = input("Enter traffic light colour: ").lower()
#
# match colour:
#     case "red":
#         print("Stop")
#     case "amber":
#         print("Get ready")
#     case "green":
#         print("Go")
#     case _:
#         print("Invalid colour")

#4
# number = int(input("Enter a number: "))
#
# match True:
#     case _ if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     case _ if number % 3 == 0:
#         print("Fizz")
#     case _ if number % 5 == 0:
#         print("Buzz")
#     case _:
#         print("No match")

#4
# coursework = int(input("Enter coursework mark: "))
# exam = int(input("Enter exam mark: "))
#
# average = (coursework + exam) / 2
#
# match True:
#     case _ if coursework < 35 or exam < 35:
#         print("Automatic fail (component below 35).")
#     case _ if average >= 40:
#         print("Module passed.")
#     case _:
#         print("Module failed (average below 40).")

#6
# shape = input("Enter shape: ").lower()
#
# match shape:
#     case "circle":
#         radius = float(input("Enter radius: "))
#         area = 3.14159 * radius ** 2
#         print("Area:", area)
#
#     case "square":
#         side = float(input("Enter side length: "))
#         area = side ** 2
#         print("Area:", area)
#
#     case "triangle":
#         base = float(input("Enter base: "))
#         height = float(input("Enter height: "))
#         area = 0.5 * base * height
#         print("Area:", area)
#
#     case "rectangle":
#         length = float(input("Enter length: "))
#         width = float(input("Enter width: "))
#         area = length * width
#         print("Area:", area)
#
#     case _:
#         print("Invalid shape")

#7

# day = int(input("Enter day number (1–7): "))
#
# match day:
#     case 1:
#         print("Monday - Start of work week")
#     case 6 | 7:
#         print("Weekend - Relax!")
#     case 2 | 3 | 4 | 5:
#         print("Weekday")
#     case _:
#         print("Invalid day number")

#8
# drink = input("Enter drink choice: ").lower()
#
# match drink:
#     case "coffee":
#         price = 2.50
#     case "tea":
#         price = 1.80
#     case "water":
#         price = 1.00
#     case "juice":
#         price = 2.20
#     case _:
#         price = 0
#
# if price > 0:
#     print(f"You ordered {drink}. Price: £{price}")
# else:
#     print("Invalid drink choice")

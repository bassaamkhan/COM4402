"""
COM4402 – Input, Output & Data Types in Python
Follow-along file for the I/O lesson.

Use this during class by uncommenting the sections you want to demonstrate.
Each section corresponds roughly to a slide or activity.
"""

# ---------------------------------------------------------
# 0. Name Greeting – Basic input() and print()
# ---------------------------------------------------------

# Plain version of:
# BEGIN
#   OUTPUT "What is your name?"
#   INPUT name
#   OUTPUT "Hello " + name
# END

# print("What is your name?")
# name = input()  # waits for the user to type and press Enter
# print("Hello", name)


# ---------------------------------------------------------
# 1. Activity 1 – Name & Age
# ---------------------------------------------------------

# Pseudocode:
# BEGIN
#   OUTPUT "Enter your name:"
#   INPUT name
#   OUTPUT "Enter your age:"
#   INPUT age
#   OUTPUT "Hello " + name + ", you are " + age + " years old."
# END

# name = input("Enter your name: ")
# age = input("Enter your age: ")  # NOTE: this is a string

# print("Hello", name + ", you are", age, "years old.")
# # age is still a string here. We haven't converted it yet.


# ---------------------------------------------------------
# 2. Data types – simple examples
# ---------------------------------------------------------

# age = 21          # int
# price = 3.50      # float
# name = "Aamir"    # str
# is_student = True # bool

# print(age, "→", type(age))
# print(price, "→", type(price))
# print(name, "→", type(name))
# print(is_student, "→", type(is_student))


# ---------------------------------------------------------
# 3. input() always returns str
# ---------------------------------------------------------

# Even if the user types 21, the result is a string.

# age = input("Enter age: ")
# print("You typed:", age)
# print("Type of age is:", type(age))  # str


# ---------------------------------------------------------
# 4. Converting input to numbers (type casting)
# ---------------------------------------------------------

# We use int() for whole numbers, float() for decimals.

# age = int(input("Enter age as a whole number: "))
# height = float(input("Enter height in metres (e.g. 1.75): "))

# print("Age:", age, "Type:", type(age))
# print("Height:", height, "Type:", type(height))

# age_next_year = age + 1
# print("Next year you will be", age_next_year)


# ---------------------------------------------------------
# 5. Activity 2 – Simple Calculator (Pairs)
# ---------------------------------------------------------

# Pseudocode:
# BEGIN
#   OUTPUT "Enter first number:"
#   INPUT a
#   OUTPUT "Enter second number:"
#   INPUT b
#   SET sum TO a + b
#   SET product TO a * b
#   OUTPUT "Sum is " + sum
#   OUTPUT "Product is " + product
# END

# One possible Python solution:

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# sum_value = a + b
# product = a * b

# print("Sum is", sum_value)
# print("Product is", product)


# ---------------------------------------------------------
# 6. Dynamic typing – changing the type of a variable's value
# ---------------------------------------------------------

# In Python, the type is attached to the VALUE, not the NAME.

# x = 10          # x refers to an int
# print("x:", x, "Type:", type(x))

# x = "Hello"     # now x refers to a str
# print("x:", x, "Type:", type(x))

# # This will cause an error if uncommented:
# # print(x + 1)  # TypeError: can only concatenate str (not "int") to str


# ---------------------------------------------------------
# 7. Activity 3 – Type confusion bug
# ---------------------------------------------------------

# This is the buggy version:

# age = input("Enter age: ")
# age_next_year = age + 1   # ❌ can't add int to str
# print(age_next_year)

# Fixed version:

# age = int(input("Enter age: "))
# age_next_year = age + 1
# print("Next year you will be", age_next_year)


# ---------------------------------------------------------
# 8. Naming rules – good vs bad variable names
# ---------------------------------------------------------

# Bad: single letters that don't explain meaning
# x = 21
# y = 1.75
# z = True

# Better: descriptive, lowercase_with_underscores
# age = 21
# height_m = 1.75
# is_student = True

# print("age:", age)
# print("height_m:", height_m)
# print("is_student:", is_student)


# ---------------------------------------------------------
# 9. Activity 4 – Rename variables
# ---------------------------------------------------------

# Pseudocode:
# SET a TO 50
# SET b TO 60
# SET c TO a + b
# OUTPUT c

# Better pseudocode:
# SET test1_mark TO 50
# SET test2_mark TO 60
# SET total_mark TO test1_mark + test2_mark
# OUTPUT total_mark

# Python version:
# test1_mark = 50
# test2_mark = 60
# total_mark = test1_mark + test2_mark
# print("Total mark:", total_mark)


# ---------------------------------------------------------
# 10. Activity 5 – User Profile Program
# ---------------------------------------------------------

# Pseudocode:
# BEGIN
#   OUTPUT "Enter your name:"
#   INPUT name
#   OUTPUT "Enter your age:"
#   INPUT age
#   OUTPUT "Enter your height in metres:"
#   INPUT height
#   SET age_plus_one TO age + 1
#   OUTPUT "Hello " + name
#   OUTPUT "Next year you will be " + age_plus_one
# END

# Python version:

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# height = float(input("Enter your height in metres: "))

# age_plus_one = age + 1

# print("Hello", name)
# print("Next year you will be", age_plus_one)
# print("Your height is", height, "metres")


# ---------------------------------------------------------
# 11. Activity 6 – Product Cost (Pairs)
# ---------------------------------------------------------

# Pseudocode:
# BEGIN
#   OUTPUT "Enter product name:"
#   INPUT product_name
#   OUTPUT "Enter price:"
#   INPUT price
#   OUTPUT "Enter quantity:"
#   INPUT quantity
#   SET total_cost TO price * quantity
#   OUTPUT "You bought " + quantity + " of " + product_name
#   OUTPUT "Total cost is " + total_cost
# END

# Python version:

# product_name = input("Enter product name: ")
# price = float(input("Enter price: "))
# quantity = int(input("Enter quantity: "))

# total_cost = price * quantity

# print("You bought", quantity, "of", product_name)
# print("Total cost is", total_cost)


# ---------------------------------------------------------
# 12. Reflection (no code)
# ---------------------------------------------------------

# In your own words:
# - Why do data types matter, even in small programs?
# - How do good variable names make code easier to read and debug?

# You can ask students to write their answers in comments here, e.g.:
# my_reflection = """
# I think data types matter because ...
# Good variable names are important because ...
# """
# print(my_reflection)


#practice


#1
# item_name = input("Enter item name: ")
# price = float(input("Enter price: "))
# quantity = int(input("Enter quantity: "))
#
# total = price * quantity
#
# print(
#     "You bought " + str(quantity) +
#     " x " + item_name +
#     " at £" + str(price) +
#     " each. Total = £" + str(total)
# )


#2

# item_name = input("Enter item name: ")
# price = float(input("Enter price: "))
# quantity = int(input("Enter quantity: "))
#
# total = price * quantity
#
# print(f"You bought {quantity} x {item_name} at £{price} each. Total = £{total}")
# age = int(input("Enter your age: "))
#
#
# print("You are", age, "years old.")
#
#
# print(f"You are {age} years old.")


#3
# full_name = input("Enter full name: ").strip()
# course_name = input("Enter course name: ").strip()
#
# full_name = full_name.title()
# course_name = course_name.upper()
#
# print(f"Student: {full_name} ({course_name})")

#4
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# course = input("Enter your course: ")
#
# print(
#     f"Your details:\n"
#     f"Name: {name}\n"
#     f"Age: {age}\n"
#     f"Course: {course}"
# )


#5
# template = "Hello NAME, welcome to COURSE."
#
# name = input("Enter your name: ").strip()
# course = input("Enter your course: ").strip()
#
# message = template.replace("NAME", name).replace("COURSE", course)
#
# print(message)

#6

# sentence = input("Type a sentence: ")
#
# print(sentence.upper())
# print(sentence.lower())
# print("Length:", len(sentence))


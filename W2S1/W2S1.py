# ---------------------------------------------------------
# 1. Type casting recap: input() always returns a string
# ---------------------------------------------------------

# Example: raw input and type
# age = input("Enter age: ")
# print(age)
# print("Type of age:", type(age))  # will be <ass 'str'>


# Example: converting to int and float
# age = int(input("Enter age as a whole number: "))
# height = float(input("Enter height in metres (e.g. 1.75): "))
# print("Age:", age, "Type:", type(age))
# print("Height:", height, "Type:", type(height))


# ---------------------------------------------------------
# 2. Simple receipt – type casting in practice
# ---------------------------------------------------------

# item_name = input("Enter item name: ")
# price = float(input("Enter price per item: "))
# quantity = int(input("Enter quantity: "))
# total = price * quantity
# print("Total cost:", total)


# ---------------------------------------------------------
# 3. Concatenation vs commas vs f-strings
# ---------------------------------------------------------

# # Setup variables
# name = "Sam"
# age = 19
# course = "COM4402"

# # A) Concatenation with +
# print("Using concatenation (+):")
# print("Hello " + name + ", you are " + str(age) + " and enrolled in " + course + ".")

# # B) Commas in print()
# print("\nUsing commas in print():")
# print("Hello", name + ", you are", age, "and enrolled in", course + ".")

# # C) f-strings
# print("\nUsing an f-string:")
# print(f"Hello {name}, you are {age} and enrolled in {course}.")


# ---------------------------------------------------------
# 4. f-strings with expressions
# ---------------------------------------------------------

# price = 3.5
# quantity = 4
# # f-string can evaluate expressions inside {}
# print(f"\nTotal cost: £{price * quantity}")


# ---------------------------------------------------------
# 5. Escape characters
# ---------------------------------------------------------

# # Using \" to include quotes inside a string
# print("He said \"Hello\" to everyone.")

# # Using \n for new lines
# print("Line 1\nLine 2\nLine 3")

# # Using \\ for backslash
# print("Windows path: C:\\Users\\student\\Documents")


# ---------------------------------------------------------
# 6. Multi-line message (different approaches)
# ---------------------------------------------------------

# # A) Multiple print calls
# print("Your details:")
# print("Name: Alice")
# print("Age: 20")
# print("Course: COM4402")

# # B) Single print with \n
# print("Your details:\nName: Alice\nAge: 20\nCourse: COM4402")

# # C) f-string with \n
# name = "Alice"
# age = 20
# course = "COM4402"
# print(f"Your details:\nName: {name}\nAge: {age}\nCourse: {course}")


# ---------------------------------------------------------
# 7. Common string methods: upper, lower, strip, replace, title
# ---------------------------------------------------------

# text = "  hello, world!  "
# print("Original:", repr(text))  # repr() shows spaces clearly
# print("upper():", repr(text.upper()))
# print("lower():", repr(text.lower()))
# print("strip():", repr(text.strip()))
# print("replace('world', 'Python'):", repr(text.replace("world", "Python")))

# # title(), startswith(), endswith(), len()
# phrase = "python programming"
# print("\nPhrase:", repr(phrase))
# print("title():", phrase.title())
# print("startswith('py'):", phrase.startswith("py"))
# print("endswith('ing'):", phrase.endswith("ing"))
# print("len(phrase):", len(phrase))


# ---------------------------------------------------------
# 8. Trimming input with .strip()
# ---------------------------------------------------------

# name = input("Enter your name (with extra spaces if you like): ")
# print("Raw name:      ", repr(name))
# print("Stripped name: ", repr(name.strip()))


# ---------------------------------------------------------
# 9. Tidy name – combining strip() and upper()
# ---------------------------------------------------------

# full_name = input("Enter your full name: ")
# print("Original:", repr(full_name))
# processed = full_name.strip().upper()
# print("Processed:", repr(processed))


# ---------------------------------------------------------
# 10. Personalised letter generator – basic version
# ---------------------------------------------------------

# name = input("Enter your full name: ")
# course = input("Enter your course name: ")
# year = int(input("Enter your current year of study: "))
# language = input("Enter your favourite programming language: ")

# # Clean up strings a bit
# name = name.strip().title()       # remove outer spaces, Title Case
# course = course.strip().upper()   # remove spaces, all caps
# language = language.strip()       # just remove outer spaces

# letter = (
#     f"Dear {name},\n\n"
#     f"Welcome to {course}.\n"
#     f"You are currently in year {year} of your studies,\n"
#     f"and it's great to hear that you enjoy {language}.\n\n"
#     "Best wishes,\n"
#     "COM4402 Teaching Team"
# )

# print("\n--- Your Letter ---\n")
# print(letter)


# ---------------------------------------------------------
# 11. Extended letter generator with goal
# ---------------------------------------------------------

# name = input("Enter your full name: ")
# course = input("Enter your course name: ")
# year = int(input("Enter your current year of study: "))
# language = input("Enter your favourite programming language: ")
# goal = input("What is one goal you have for this module? ")

# name = name.strip().title()
# course = course.strip().upper()
# language = language.strip()
# goal = goal.strip()

# letter_with_goal = (
#     f"Dear {name},\n\n"
#     f"Welcome to {course}.\n"
#     f"You are currently in year {year} of your studies,\n"
#     f"and it's great to hear that you enjoy {language}.\n\n"
#     f"Your goal for this module is: \"{goal}\".\n"
#     "Keep this in mind as you work through the course.\n\n"
#     "Best wishes,\n"
#     "COM4402 Teaching Team"
# )

# print("\n--- Your Personalised Letter with Goal ---\n")
# print(letter_with_goal)


# ---------------------------------------------------------
# End of examples file
# ---------------------------------------------------------




#practice



#1
# name = input("Enter your name: ")
# print("Hello", name)



#3
# name = input("Enter your name: ")
# age = input("Enter your age: ")

# print(f"Hello {name}, you are {age} years old.")
# print(type(age))


# 4
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# sum_result = num1 + num2
# product_result = num1 * num2

# print("Sum:", sum_result)
# print("Product:", product_result)

# print("Type of sum:", type(sum_result))
# print("Type of product:", type(product_result))


#5
# x = 10
# print(x)
# print(type(x))
#
# x = "Hello"
# print(x)
# print(type(x))
#
# x + 1


#6
# age = int(input("Enter age: "))
# age_next_year = age + 1
# print(f"Next year you will be {age_next_year}")















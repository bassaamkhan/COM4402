# #1
#
# n=int(input("Enter a number: "))
#
# name=input("Enter a word: ")
#
# for i in range(n):
#  print(i)
#  print(name)
#  print(i, name)
#  print(str(i) + ": " + name)
#  print(f"{i}: {name}")
#
#
#
#
# print()
#
# #2
# n=int(input("Enter a number"))
# sum=0
# for i in range(1,n+1):
#     sum=sum +i
# print(sum)
#
#   #3
#
# n=int(input("enter the number"))
#
# for i in range(1,11):
#     print(n, "x", i,"=", n*i)
#     print(f"{n} X {i} = {n * i}")
#
# #4
#
# sentence = input("Enter a sentence: ")
# count = 0
#
#
# for char in sentence:
#     if char != ' ':
#  count= count + 1
# print("Number of non-space characters:", count)
#
#
#
# #5
#
# n = int(input("How many marks will you enter? "))
#
#
# max_mark = None
#
#
# for i in range(n):
#     mark = int(input(f"Enter mark {i + 1}: "))
#
#
#     if max_mark is None or mark > max_mark:
#         max_mark = mark
#
#
# if max_mark is not None:
#     print(f"The highest mark is: {max_mark}")
# else:
#     print("No marks were entered.")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# #6
# # Ask how many marks to enter
# n = int(input("How many marks to enter? "))
#
# # Initialize counter
# pass_count = 0
#
# print("Passing marks (≥40):")
# for i in range(n):
#     mark = int(input(f"Enter mark {i+1}: "))
#     if mark >= 40:
#         print(mark)
#         pass_count += 1
#
# print(f"Total passed: {pass_count}")
#
#
#
#
#
#
# #7
# # Ask user for a word
# word = input("Enter a word: ")
#
# # Initialize empty string for reversed word
# reversed_word = ""
#
# # Use for loop to build reversed string
# for char in word:
#     reversed_word = char + reversed_word  # Add character to the front
#
# print(f"Original: {word}")
# print(f"Reversed: {reversed_word}")
#
#
#
#
#
# #8
# # Ask how many names to enter
# n = int(input("How many names to enter? "))
#
# # Store names in a list
# names = []
#
# # Input names
# for i in range(n):
#     name = input(f"Enter name {i+1}: ")
#     names.append(name)
#
# # Ask for a letter
# letter = input("Enter a letter to search for: ").lower()
#
# # Count names containing the letter
# count = 0
# for name in names:
#     if letter in name.lower():  # Case-insensitive check
#         count += 1
#
# print(f"Number of names containing '{letter}': {count}")
#
#
#
#
#
# #9
# # Ask for number of students
# n = int(input("How many students? "))
#
# # Initialize variables
# total = 0
# distinction_count = 0
#
# # Input marks and calculate statistics
# for i in range(n):
#     while True:  # Input validation loop
#         mark = int(input(f"Enter mark for student {i + 1} (0-100): "))
#         if 0 <= mark <= 100:
#             break
#         print("Invalid mark! Please enter between 0 and 100.")
#
#     total += mark
#     if mark >= 70:
#         distinction_count += 1
#
# # Calculate average
# average = total / n if n > 0 else 0
#
# # Print results
# print(f"\nGrade Statistics:")
# print(f"Total marks: {total}")
# print(f"Average mark: {average:.2f}")
# print(f"Distinctions (≥70): {distinction_count}")
#
#
#
#
#
# #10
#
# # Ask how many numbers to enter
# n = int(input("How many numbers to enter? "))
#
# # Create an empty list
# numbers = []
#
# # Input positive integers into the list using for loop
# for i in range(n):
#     value = int(input(f"Enter positive integer {i+1}: "))
#     if value <= 0:
#         # If not positive, use default value of 1
#         print("Invalid! Using 1 instead.")
#         value = 1
#     numbers.append(value)
#
# # Print the bar chart using for loop
# print("\nBar Chart:")
# for value in numbers:
#     bar = "*" * value
#     print(bar)
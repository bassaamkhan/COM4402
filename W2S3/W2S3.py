"""
COM4402 – Decision-Making in Python
Follow-along code for the lesson on if / elif / else and nested conditions.

Use this file in class by uncommenting the sections you want to demonstrate.
Each section corresponds roughly to a slide/activity.
"""

# ---------------------------------------------------------
# 0. Basic Pass / Fail example
# ---------------------------------------------------------
# Pseudocode:
# BEGIN
#   INPUT score
#   IF score >= 40 THEN
#       OUTPUT "Pass"
#   ELSE
#       OUTPUT "Fail"
#   ENDIF
# END

# score = int(input("Enter score: "))
#
# if score >= 40:
#     print("Pass")
# else:
#     print("Fail")


# ---------------------------------------------------------
# 1. Activity 1 – Even or Odd
# ---------------------------------------------------------
# Pseudocode:
# BEGIN
#   INPUT number
#   IF number is even THEN
#       OUTPUT "Even"
#   ELSE
#       OUTPUT "Odd"
#   ENDIF
# END

# number = int(input("Enter an integer: "))
#
# # number % 2 gives remainder after dividing by 2
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# ---------------------------------------------------------
# 2. if / elif / else – simple grade classification
# ---------------------------------------------------------
# Pseudocode:
# BEGIN
#   INPUT score
#   IF score >= 70 THEN
#       grade = "Distinction"
#   ELSEIF score >= 40 THEN
#       grade = "Pass"
#   ELSE
#       grade = "Fail"
#   ENDIF
#   OUTPUT grade
# END

# score = int(input("Enter score (0–100): "))
#
# if score >= 70:
#     grade = "Distinction"
# elif score >= 40:
#     grade = "Pass"
# else:
#     grade = "Fail"
#
# print("Your grade is:", grade)


# ---------------------------------------------------------
# 3. Activity 2 – Finer grade classification (A–D, Fail)
# ---------------------------------------------------------
# Requirements:
#   80–100 → A
#   70–79  → B
#   60–69  → C
#   50–59  → D
#   < 50   → Fail

# score = int(input("Enter score (0–100): "))
#
# if score >= 80:
#     grade = "A"
# elif score >= 70:
#     grade = "B"
# elif score >= 60:
#     grade = "C"
# elif score >= 50:
#     grade = "D"
# else:
#     grade = "Fail"
#
# print("Your grade is:", grade)


# ---------------------------------------------------------
# 4. Nested if – Pass with merit
# ---------------------------------------------------------
# Pseudocode:
# BEGIN
#   INPUT score
#   IF score >= 40 THEN
#       IF score >= 70 THEN
#           OUTPUT "Pass with merit"
#       ELSE
#           OUTPUT "Pass"
#       ENDIF
#   ELSE
#       OUTPUT "Fail"
#   ENDIF
# END

# score = int(input("Enter score (0–100): "))
#
# if score >= 40:
#     if score >= 70:
#         print("Pass with merit")
#     else:
#         print("Pass")
# else:
#     print("Fail")


# ---------------------------------------------------------
# 5. Login system – nested if
# ---------------------------------------------------------
# Pseudocode:
# BEGIN
#   INPUT username
#   INPUT password
#   IF username == "admin" THEN
#       IF password == "secret" THEN
#           OUTPUT "Login successful"
#       ELSE
#           OUTPUT "Wrong password"
#       ENDIF
#   ELSE
#       OUTPUT "Unknown username"
#   ENDIF
# END

# username = input("Enter username: ")
# password = input("Enter password: ")
#
# if username == "admin":
#     if password == "secret":
#         print("Login successful")
#     else:
#         print("Wrong password")
# else:
#     print("Unknown username")


# ---------------------------------------------------------
# 6. Login system – combined condition (and)
# ---------------------------------------------------------
# Pseudocode:
# IF username == "admin" AND password == "secret" THEN
#   OUTPUT "Login successful"
# ELSE
#   OUTPUT "Login failed"
# ENDIF

# username = input("Enter username: ")
# password = input("Enter password: ")
#
# if username == "admin" and password == "secret":
#     print("Login successful")
# else:
#     print("Login failed")


# ---------------------------------------------------------
# 7. Activity 4 – Login variants (two valid users)
# ---------------------------------------------------------
# Requirements:
#   - If username == "admin" → "Welcome, admin."
#   - If username == "student" → "Welcome, student."
#   - Otherwise → "Unknown user."

# username = input("Enter username: ")
#
# if username == "admin":
#     print("Welcome, admin.")
# elif username == "student":
#     print("Welcome, student.")
# else:
#     print("Unknown user.")


# ---------------------------------------------------------
# 8. Common pitfalls demonstration (commented examples)
# ---------------------------------------------------------

# Mistake: using = instead of == in a condition
# score = 50
# if score = 50:   # ❌ SYNTAX ERROR – cannot use = in if condition
#     print("Score is 50")

# Correct:
# if score == 50:  # ✅ comparison
#     print("Score is 50")


# ---------------------------------------------------------
# 9. Mini design task – Ticket price classifier
# ---------------------------------------------------------
# Requirements:
#   Age < 12   → "Child ticket"
#   12–17      → "Teen ticket"
#   18+        → "Adult ticket"

# age = int(input("Enter your age: "))
#
# if age < 12:
#     print("Child ticket")
# elif age < 18:  # if we get here, age is at least 12
#     print("Teen ticket")
# else:
#     print("Adult ticket")


# ---------------------------------------------------------
# 10. Mini design task – Temperature classifier
# ---------------------------------------------------------
# Requirements:
#   temp < 0    → "Freezing"
#   0–19        → "Cold"
#   20–29       → "Warm"
#   30+         → "Hot"

# temp = float(input("Enter temperature in °C: "))
#
# if temp < 0:
#     print("Freezing")
# elif temp < 20:
#     print("Cold")
# elif temp < 30:
#     print("Warm")
# else:
#     print("Hot")


# ---------------------------------------------------------
# End of follow-along file
# ---------------------------------------------------------






#practice

#1
# age = int(input("Enter your age: "))
#
# if age < 5:
#     print("Free entry")
# elif age <= 17:
#     print("Child ticket")
# elif age <= 64:
#     print("Adult ticket")
# else:
#     print("Senior ticket")


#2
# days_late = int(input("Enter days late: "))
#
# if days_late == 0:
#     print("No fine")
# elif days_late <= 5:
#     print("Fine = £1")
# elif days_late <= 10:
#     print("Fine = £5")
# else:
#     print("Fine = £10 and membership review")

#3
# score = int(input("Enter score (0–100): "))
#
# if score >= 40:
#     if 38 <= score <= 42:
#         print("Borderline pass, consider review.")
#     else:
#         print("Clear pass.")
# else:
#     print("Fail.")
#


#4
# is_student = input("Are you a student? (yes/no): ").lower()
# age = int(input("Enter your age: "))
#
# if is_student == "yes" or age < 18:
#     print("Discount applied")
# else:
#     print("No discount")

#5
# colour = input("Enter traffic light colour: ").lower()
#
# if colour == "red":
#     print("Stop")
# elif colour == "amber":
#     print("Get ready")
# elif colour == "green":
#     print("Go")
# else:
#     print("Invalid colour")


#6

# number = int(input("Enter a number: "))
#
# if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
# elif number % 3 == 0:
#     print("Fizz")
# elif number % 5 == 0:
#     print("Buzz")
# else:
#     print("No match")


#7
# time_of_day = input("Enter time of day: ").lower()
# is_hungry = input("Are you hungry? (yes/no): ").lower()
#
# if is_hungry == "no":
#     print("Have some water and rest.")
# else:
#     if time_of_day == "morning":
#         print("Have breakfast.")
#     elif time_of_day == "afternoon":
#         print("Have lunch.")
#     elif time_of_day == "evening":
#         print("Have dinner.")
#     else:
#         print("Snack time.")


#8
# coursework = int(input("Enter coursework mark: "))
# exam = int(input("Enter exam mark: "))
#
# average = (coursework + exam) / 2
#
# if coursework < 35 or exam < 35:
#     print("Automatic fail (component below 35).")
# elif average >= 40:
#     print("Module passed.")
# else:
#     print("Module failed (average below 40).")

#9
# pin = input("Enter 4-digit PIN: ")
#
# if pin == "1234":
#     colour = input("What is your favourite colour? ").lower()
#     if colour == "blue":
#         print("Access granted.")
#     else:
#         print("Security answer incorrect.")
# else:
#     print("Wrong PIN.")


#10
# weather = input("Enter weather: ").lower()
# mood = input("Enter mood: ").lower()
#
# if weather == "sunny" and mood == "active":
#     print("Go for a run.")
# elif weather == "sunny" and mood == "tired":
#     print("Relax in the park.")
# elif weather == "rainy":
#     print("Indoor workout.")
# elif weather == "cold":
#     print("Go to the gym.")
# else:
#     print("No suggestion available.")
#

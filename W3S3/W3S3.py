# """
# COM4402 – Nested Loop Applications
# Solutions to 10 pattern / grid problems
# """
#
# # 1. Right-Angled Triangle of Stars
# def problem_1():
#     rows = 5
#     for i in range(1, rows + 1):
#         print("*" * i)
#
#
# # 2. Number Triangle (Row Number)
# def problem_2():
#     rows = 5
#     for i in range(1, rows + 1):
#         print(str(i) * i)
#
#
# # 3. Increasing Number Triangle
# def problem_3():
#     rows = 4
#     current = 1
#     for i in range(1, rows + 1):
#         line = ""
#         for _ in range(i):
#             line += str(current)
#             current += 1
#         print(line)
#
#
# # 4. Square Multiplication Grid
# def problem_4():
#     size = 5
#     for row in range(1, size + 1):
#         line = ""
#         for col in range(1, size + 1):
#             line += f"{row * col:3}"
#         print(line)
#
#
# # 5. Coordinate Grid
# def problem_5():
#     rows = 3
#     cols = 4
#     for r in range(rows):
#         line = ""
#         for c in range(cols):
#             line += f"({r},{c}) "
#         print(line.strip())
#
#
# # 6. Hollow Square of Stars
# def problem_6():
#     size = 5
#     for r in range(size):
#         line = ""
#         for c in range(size):
#             if r == 0 or r == size - 1 or c == 0 or c == size - 1:
#                 line += "*"
#             else:
#                 line += " "
#         print(line)
#
#
# # 7. Centered Pyramid of Stars
# def problem_7():
#     rows = 4
#     for i in range(1, rows + 1):
#         spaces = rows - i
#         stars = 2 * i - 1
#         print(" " * spaces + "*" * stars)
#
#
# # 8. Times Table Block (2–4 by 1–5)
# def problem_8():
#     for mul in range(1, 6):
#         line = ""
#         for table in range(2, 5):
#             result = table * mul
#             line += f"{table} x {mul} = {result:<2}   "
#         print(line.rstrip())
#
#
# # 9. Checkerboard Pattern
# def problem_9():
#     size = 8
#     for r in range(size):
#         line = ""
#         for c in range(size):
#             if (r + c) % 2 == 0:
#                 line += "#"
#             else:
#                 line += "."
#         print(line)
#
#
# # 10. Pascal-like Triangle (5 rows)
# def problem_10():
#     rows = 5
#     current_row = [1]
#     for _ in range(rows):
#         print(" ".join(str(x) for x in current_row))
#         next_row = [1]
#         for i in range(len(current_row) - 1):
#             next_row.append(current_row[i] + current_row[i + 1])
#         next_row.append(1)
#         current_row = next_row
#
#
# # Optional menu to run problems
# def main():
#     while True:
#         print("\nCOM4402 – Nested Loop Applications Menu")
#         print("----------------------------------------")
#         print(" 1. Right-angled triangle of stars")
#         print(" 2. Number triangle (row number)")
#         print(" 3. Increasing number triangle")
#         print(" 4. Square multiplication grid")
#         print(" 5. Coordinate grid")
#         print(" 6. Hollow square of stars")
#         print(" 7. Centered pyramid of stars")
#         print(" 8. Times table block (2–4 by 1–5)")
#         print(" 9. Checkerboard pattern")
#         print("10. Pascal-like triangle (5 rows)")
#         print(" 0. Exit")
#         print("----------------------------------------")
#
#         choice = input("Enter your choice (0–10): ").strip()
#
#         if choice == "0":
#             print("Goodbye!")
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


#practice

# 1. Right-Angled Triangle of Stars
# def right_triangle():
#     rows = 5
#     for i in range(1, rows + 1):
#         print("*" * i)
#
#
# # 2. Number Triangle (Row Number)
# def number_triangle():
#     rows = 5
#     for i in range(1, rows + 1):
#         print(str(i) * i)
#
#
# # 3. Increasing Number Triangle
# def increasing_triangle():
#     rows = 4
#     current = 1
#     for i in range(1, rows + 1):
#         line = ""
#         for _ in range(i):
#             line += str(current)
#             current += 1
#         print(line)
#
#
# # 4. Square Multiplication Grid
# def multiplication_grid():
#     size = 5
#     for r in range(1, size + 1):
#         line = ""
#         for c in range(1, size + 1):
#             line += f"{r * c:2} "
#         print(line.strip())
#
#
# # 5. Coordinate Grid
# def coordinate_grid():
#     rows, cols = 3, 4
#     for r in range(rows):
#         line = ""
#         for c in range(cols):
#             line += f"({r},{c}) "
#         print(line.strip())
#
#
# # 6. Hollow Square of Stars
# def hollow_square():
#     size = 5
#     for r in range(size):
#         line = ""
#         for c in range(size):
#             if r == 0 or r == size - 1 or c == 0 or c == size - 1:
#                 line += "*"
#             else:
#                 line += " "
#         print(line)
#
#
# # 7. Centered Pyramid of Stars
# def centered_pyramid():
#     rows = 4
#     for i in range(1, rows + 1):
#         spaces = rows - i
#         stars = 2 * i - 1
#         print(" " * spaces + "*" * stars)
#
#
# # 8. Times Table Block (2–4 by 1–5)
# def times_table_block():
#     for mul in range(1, 6):
#         line = ""
#         for table in range(2, 5):
#             line += f"{table} x {mul} = {table * mul:<2}   "
#         print(line.rstrip())
#
#
# # 9. Checkerboard Pattern
# def checkerboard():
#     size = 8
#     for r in range(size):
#         line = ""
#         for c in range(size):
#             line += "#" if (r + c) % 2 == 0 else "."
#         print(line)
#
#
# # 10. Pascal-like Triangle (Simple Sums)
# def pascal_triangle():
#     rows = 5
#     current_row = [1]
#     for _ in range(rows):
#         print(" ".join(str(x) for x in current_row))
#         next_row = [1]
#         for i in range(len(current_row) - 1):
#             next_row.append(current_row[i] + current_row[i + 1])
#         next_row.append(1)
#         current_row = next_row
#
#
# # Menu to run all problems
# def main():
#     while True:
#         print("\nNested Loop Patterns Menu")
#         print("1. Right-Angled Triangle")
#         print("2. Number Triangle")
#         print("3. Increasing Number Triangle")
#         print("4. Multiplication Grid")
#         print("5. Coordinate Grid")
#         print("6. Hollow Square")
#         print("7. Centered Pyramid")
#         print("8. Times Table Block")
#         print("9. Checkerboard Pattern")
#         print("10. Pascal-like Triangle")
#         print("0. Exit")
#
#         choice = input("Enter choice (0-10): ").strip()
#         if choice == "0":
#             print("Goodbye!")
#             break
#         elif choice == "1":
#             right_triangle()
#         elif choice == "2":
#             number_triangle()
#         elif choice == "3":
#             increasing_triangle()
#         elif choice == "4":
#             multiplication_grid()
#         elif choice == "5":
#             coordinate_grid()
#         elif choice == "6":
#             hollow_square()
#         elif choice == "7":
#             centered_pyramid()
#         elif choice == "8":
#             times_table_block()
#         elif choice == "9":
#             checkerboard()
#         elif choice == "10":
#             pascal_triangle()
#         else:
#             print("Invalid choice, try again.")
#
#
# if __name__ == "__main__":
#     main()

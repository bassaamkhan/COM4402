#1
# def add_mark(marks, name, mark):
#     marks[name] = mark
#     return marks
#
# def get_mark(marks, name):
#     return marks.get(name, None)
#
# def update_mark(marks, name, new_mark):
#     if name in marks:
#         marks[name] = new_mark
#         return True
#     return False
#
# def delete_mark(marks, name):
#     if name in marks:
#         del marks[name]
#         return True
#     return False
#
# # Example usage
# marks = {}
# add_mark(marks, "Aisha", 85)
# update_mark(marks, "Aisha", 90)
# print(get_mark(marks, "Aisha"))  # 90
# delete_mark(marks, "Aisha")
# print(marks)  # {}


#2
# def create_row(names):
#     return names.copy()
#
# def get_student_at(row, index):
#     if 0 <= index < len(row):
#         return row[index]
#     return None
#
# def swap_seats(row, index1, index2):
#     if 0 <= index1 < len(row) and 0 <= index2 < len(row):
#         row[index1], row[index2] = row[index2], row[index1]
#
# def remove_student(row, name):
#     if name in row:
#         row.remove(name)
#
# # Example
# row = create_row(["Alice", "Bob", "Charlie"])
# swap_seats(row, 0, 2)
# print(row)  # ['Charlie', 'Bob', 'Alice']
# remove_student(row, "Bob")
# print(row)  # ['Charlie', 'Alice']


#3
# def enrol_module(modules, code):
#     modules.add(code)
#
# def is_enrolled(modules, code):
#     return code in modules
#
# def drop_module(modules, code):
#     modules.discard(code)
#
# def count_modules(modules):
#     return len(modules)
#
# # Example
# modules = set()
# enrol_module(modules, "COM4402")
# enrol_module(modules, "COM4403")
# print(is_enrolled(modules, "COM4402"))  # True
# drop_module(modules, "COM4403")
# print(count_modules(modules))  # 1


#4
# def create_student(id_number, name, year):
#     return (id_number, name, year)
#
# def get_name(student):
#     return student[1]
#
# def get_year(student):
#     return student[2]
#
# # Example
# s = create_student("S001", "Aisha", 2)
# print(get_name(s))  # Aisha
# print(get_year(s))  # 2


#5
# def add_product(catalogue, name, price):
#     catalogue[name] = price
#
# def get_price(catalogue, name):
#     return catalogue.get(name, None)
#
# def increase_all_prices(catalogue, percent):
#     for key in catalogue:
#         catalogue[key] *= (1 + percent / 100)
#
# def remove_product(catalogue, name):
#     catalogue.pop(name, None)
#
# # Example
# catalogue = {}
# add_product(catalogue, "Coffee", 2.5)
# increase_all_prices(catalogue, 10)
# print(get_price(catalogue, "Coffee"))  # 2.75
# remove_product(catalogue, "Coffee")


#6
# def average(numbers):
#     if not numbers:  # prevent division by zero
#         return 0
#     total = sum(numbers)  # simpler and correct
#     return total / len(numbers)
#
# marks = [50, 60, 70]
# print("Average is", average(marks))  # 60.0


#7

# capitals = {"France": "Paris", "Spain": "Madrid", "Japan": "Tokyo"}
#
# def get_capital(country):
#     return capitals.get(country, "Unknown country")
#
# print(get_capital("France"))  # Paris
# print(get_capital("Germany"))  # Unknown country

#8

# def count_unique_emails(emails):
#     unique_emails = set(emails)  # use set, not dict
#     return len(unique_emails)
#
# emails_list = ["a@x.com", "b@x.com", "a@x.com"]
# print(count_unique_emails(emails_list))  # 2


#9
# def word_counts(sentence):
#     counts = {}
#     words = sentence.lower().split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
#     return counts
#
# sentence = "This is a test this is only a test"
# print(word_counts(sentence))
# # {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}

#10
# def add_student(students, student_id, name, mark):
#     students[student_id] = {"name": name, "mark": mark}
#
# def get_student(students, student_id):
#     return students.get(student_id, None)
#
# def update_mark(students, student_id, new_mark):
#     if student_id in students:
#         students[student_id]["mark"] = new_mark
#         return True
#     return False
#
# def delete_student(students, student_id):
#     return students.pop(student_id, None) is not None
#
# # Example
# students = {}
# add_student(students, "S001", "Aisha", 85)
# add_student(students, "S002", "Bilal", 72)
# update_mark(students, "S002", 75)
# for sid, info in students.items():
#     print(sid, info["name"], info["mark"])
#

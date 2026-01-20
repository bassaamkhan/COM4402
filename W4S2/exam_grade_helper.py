from typing import List, Tuple


def classify_mark(mark: int):


    if not isinstance(mark, int):
        raise TypeError("Mark must be an integer")


    if mark < 0 or mark > 100:
        raise ValueError("Mark must be between 0 and 100 inclusive")


    if mark < 40:
        return "Fail"
    elif mark < 70:
        return "Pass"
    else:
        return "Distinction"


def calculate_summary(marks: List[int]) -> Tuple[int, float, int, int]:


    if not isinstance(marks, list):
        raise TypeError("Marks must be a list")


    total = 0
    fail_count = 0
    distinction_count = 0

    for mark in marks:

        if not isinstance(mark, int):
            raise TypeError("All marks must be integers")


        if mark < 0 or mark > 100:
            raise ValueError(f"Mark {mark} is out of range 0–100")


        total += mark


        classification = classify_mark(mark)
        if classification == "Fail":
            fail_count += 1
        elif classification == "Distinction":
            distinction_count += 1


    average = total / len(marks) if marks else 0.0

    return total, average, fail_count, distinction_count

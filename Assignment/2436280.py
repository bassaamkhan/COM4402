# Import the random module to allow randomization of questions
import random


def load_questions():
    """
    Load and return a list of quiz questions.
    Each question is stored as a dictionary.
    """
    return [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Paris", "Berlin", "Madrid"],
            "answer": 2
        },
        {
            "question": "Which car is the fastest in the world?",
            "options": ["Bugatti", "Ferrari", "Jesko", "BMW"],
            "answer": 3
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Venus"],
            "answer": 2
        },
        {
            "question": "Which language is primarily used for web styling?",
            "options": ["Python", "C++", "CSS", "SQL"],
            "answer": 3
        },
        {
            "question": "Who wrote the play 'Romeo and Juliet'?",
            "options": [
                "William Shakespeare",
                "Charles Dickens",
                "Mark Twain",
                "Jane Austen"
            ],
            "answer": 1
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": [
                "Atlantic Ocean",
                "Indian Ocean",
                "Arctic Ocean",
                "Pacific Ocean"
            ],
            "answer": 4
        },
        {
            "question": "How many continents are there on Earth?",
            "options": ["Five", "Six", "Seven", "Eight"],
            "answer": 3
        },
        {
            "question": "Which country is famous for the pyramids?",
            "options": ["Mexico", "Greece", "Egypt", "Peru"],
            "answer": 3
        },
        {
            "question": "What gas do plants absorb from the atmosphere?",
            "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
            "answer": 3
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["Gold", "Iron", "Diamond", "Silver"],
            "answer": 3
        }
    ]


def check_answer(user_answer, correct_answer):
    """
    Compare the user's answer with the correct answer.
    Returns True if correct, otherwise False.
    """
    return user_answer == correct_answer


def get_user_answer():
    """
    Ask the user for an answer and validate the input.
    Keeps asking until the user enters a number between 1 and 4.
    """
    while True:
        try:
            user_input = int(input("Your answer: "))
            if 1 <= user_input <= 4:
                return user_input
            print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")


def calculate_percentage(score, total_questions):
    """
    Calculate and return the percentage score.
    """
    return (score / total_questions) * 100


def get_grade(percentage):
    """
    Return the grade based on the percentage score.
    """
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


def run_quiz():
    """
    Main function that runs the quiz.
    Displays questions, checks answers, and shows results.
    """
    print("Welcome to the Holton College Quiz!")
    print("Please answer with 1, 2, 3, or 4.\n")

    # Load and randomize questions
    questions = load_questions()
    random.shuffle(questions)

    score = 0
    total_questions = len(questions)

    for index, question_data in enumerate(questions, start=1):
        print(f"Question {index}: {question_data['question']}")

        for option_number, option in enumerate(
            question_data["options"], start=1
        ):
            print(f"{option_number}. {option}")

        user_answer = get_user_answer()

        if check_answer(user_answer, question_data["answer"]):
            print("Correct!\n")
            score += 1
        else:
            correct_option = question_data["options"][
                question_data["answer"] - 1
            ]
            print(f"Incorrect! The correct answer was: {correct_option}\n")

    percentage = calculate_percentage(score, total_questions)
    grade = get_grade(percentage)

    print("Quiz Complete!")
    print(f"You scored {score} out of {total_questions}.")
    print(f"Your percentage score: {percentage:.2f}%")
    print(f"Your grade: {grade}")
    print("Thank you for playing!")


# Run the quiz only if this file is executed directly
if __name__ == "__main__":
    run_quiz()

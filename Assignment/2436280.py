


def load_questions():

    return [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Paris", "Berlin", "Madrid"],
            "answer": 2
        },
        {
            "question": "Which car is the fastest in world?",
            "options": ["buggati", "ferrari", "jesko", "bmw"],
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

    ]


def check_answer(user_answer, correct_answer):

    return user_answer == correct_answer


def run_quiz():

    print("Welcome to the Holton College Quiz!")
    print("Please answer with 1, 2, 3, or 4.\n")

    questions = load_questions()
    score = 0

    for index, q in enumerate(questions, start=1):
        print(f"Question {index}: {q['question']}")
        for i, option in enumerate(q['options'], start=1):
            print(f"{i}. {option}")

        # Get valid user input
        while True:
            try:
                user_input = int(input("Your answer: "))
                if user_input in [1, 2, 3, 4]:
                    break
                else:
                    print("Invalid input. Please enter 1, 2, 3, or 4.")
            except ValueError:
                print("Please enter a number.")

        # Check answer
        if check_answer(user_input, q["answer"]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {q['answer']}.\n")

    # Final results
    print("Quiz Complete!")
    print(f"You scored {score} out of {len(questions)}.")
    print("Thank you for playing!")


# Run the quiz
if __name__ == "__main__":
    run_quiz()

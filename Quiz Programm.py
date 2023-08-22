def ask_question(question, options, correct_option):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    
    answer = int(input("Enter your answer (1/2/3/4): "))
    if answer == correct_option:
        print("Correct! You earn $500.\n")
        return 500
    else:
        print("Incorrect! You lost the game.\n")
        return 0

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Rome"],
        "correct_option": 1
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "correct_option": 1
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Lion"],
        "correct_option": 2
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Au", "Ag", "Fe", "Cu"],
        "correct_option": 1
    },
    {
        "question": "Which gas is essential for photosynthesis?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Helium"],
        "correct_option": 3
    }
]

total_earned = 0

print("Welcome to the Quiz Game!")
for i, q in enumerate(questions, start=1):
    print(f"\nQuestion {i}:")
    total_earned += ask_question(q["question"], q["options"], q["correct_option"])

print(f"Congratulations! You won ${total_earned}.")

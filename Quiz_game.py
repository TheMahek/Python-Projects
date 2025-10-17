# Quiz questions and answers
quiz = [
    {
        "question": "Which language is known as the language of the web?",
        "options": ["A. Python", "B. JavaScript", "C. C++", "D. Java"],
        "answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Processing Unit", "B. Computer Personal Unit", "C. Control Process Utility", "D. Central Program Unit"],
        "answer": "A"
    },
    {
        "question": "Which of these is a Python data type?",
        "options": ["A. Banana", "B. Integer", "C. Folder", "D. Mouse"],
        "answer": "B"
    },
    {
        "question": "What symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. /* */"],
        "answer": "C"
    }
]

def quiz_game():
    print("👉 Welcome to the Quiz Game!\n")
    score = 0

    for i, q in enumerate(quiz, start=1):
        print(f"Q{i}: {q['question']}")
        for option in q["options"]:
            print(option)
        
        answer = input("Your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.\n")

    print("🏆 Quiz Over!")
    print(f"Your final score: {score}/{len(quiz)}")
    percentage = (score / len(quiz)) * 100
    print(f"📊 Percentage: {percentage:.2f}%")

# Run game
quiz_game()


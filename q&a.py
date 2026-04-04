print("Welcome to the Simple Quiz Game!")
score = 0

questions = [
    {
        "question": "What is the capital of Sri Lanka?",
        "options": ["A) Kandy", "B) Sri Jayawardhanapura kotte", "C) Jaffna", "D) Galle"],
        "answer": "B"
    },
    {
        "question": "What is the national sport of Sri Lanka?",
        "options": ["A) Cricket", "B) Hockey", "C) Swimming", "D) Volleyball"],
        "answer": "D"
    },
    {
        "question": "Which river is the longest in Sri Lanka?",
        "options": ["A) Kelani", "B) Walawe", "C) Mahaweli", "D) Nilwala"],
        "answer": "C"
    },
    {
        "question": "What is Sri Lanka’s national flower?",
        "options": ["A) Lotus", "B) Blue Water Lily", "C) Rose", "D) Jasmine"],
        "answer": "B"
    },
    {
        "question": "Sri Lanka is the largest exporter of which spice?",
        "options": ["A) Pepper", "B) Cinnamon", "C) Cloves", "D) Cardamom"],
        "answer": "B"
    }
]

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    answer = input("Your answer (A, B, C, D): ").upper()
    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer was", q["answer"])

print(f"\nYour final score is: {score}/{len(questions)}")
print("Thanks for playing!")
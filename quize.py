import time

questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "2. Which language is used to create Python programs?",
        "options": ["A. Java", "B. C++", "C. Python", "D. HTML"],
        "answer": "C"
    },
    {
        "question": "3. What is the value of 10 + 20?",
        "options": ["A. 20", "B. 30", "C. 40", "D. 50"],
        "answer": "B"
    },
    {
        "question": "4. Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "5. Who developed Python programming language?",
        "options": [
            "A. Dennis Ritchie",
            "B. James Gosling",
            "C. Guido van Rossum",
            "D. Elon Musk"
        ],
        "answer": "C"
    },
    {
        "question": "6. Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. define", "C. def", "D. function"],
        "answer": "C"
    },
    {
        "question": "7. Which data type stores True or False values?",
        "options": ["A. Integer", "B. Boolean", "C. String", "D. Float"],
        "answer": "B"
    },
    {
        "question": "8. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    },
    {
        "question": "9. Which company developed the Android operating system?",
        "options": ["A. Google", "B. Apple", "C. Microsoft", "D. IBM"],
        "answer": "A"
    },
    {
        "question": "10. Which one is a Python loop?",
        "options": ["A. repeat", "B. foreach", "C. for", "D. loop"],
        "answer": "C"
    }
]

score = 0
time_limit = 10

print("=" * 40)
print("        PYTHON QUIZ APPLICATION")
print("=" * 40)
print("You have 10 seconds for each question.\n")

for q in questions:
    print(q["question"])

    for option in q["options"]:
        print(option)

    start_time = time.time()
    answer = input("\nEnter your answer (A/B/C/D): ").upper()
    end_time = time.time()
    time_taken = end_time - start_time

    if time_taken > time_limit:
        print("Time Over! ⏰")
    elif answer == q["answer"]:
        print("Correct Answer! ✅")
        score += 1
    else:
        print("Wrong Answer! ❌")

    print("-" * 40)

print("\n========== RESULT ==========")
print(f"Total Questions: {len(questions)}")
print(f"Correct Answers: {score}")
print(f"Wrong Answers: {len(questions)-score}")

percentage = (score / len(questions)) * 100
print(f"Score Percentage: {percentage}%")

if percentage >= 80:
    print("Excellent Performance! 🏆")
elif percentage >= 50:
    print("Good Performance! 👍")
else:
    print("Need More Practice! 📚")
import random

# Step 1: Define the dictionary with questions and answers
Quiz_questions = {
    "What is the capital of France?": "Paris",
    "What is 5 + 7?": "12",
    "Which planet is known as the red planet?": "Mars",
    "Who wrote 'Harry Potter'?": "J.K. Rowling",
    "What is the square root of 64?": "8"
}

# Step 2: Function to play the quiz
def play_quiz():
    score = 0  # Variable to store correct answers

    while score < 3:  # Loop until three correct answers
        question, answer = random.choice(list(Quiz_questions.items()))  # Pick random question
        user_answer = input(f"{question} - ")

        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}")

        print(f"your score is {score}/3\n")

    print("congratulations! you have completed the quiz")

# step 3: Run the function
play_quiz()
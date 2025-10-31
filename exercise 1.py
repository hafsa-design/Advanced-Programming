import random

# Function to display the difficulty menu and get user's choice
def displayMenu():
    print("DIFFICULTY LEVEL")
    print(" 1. Easy")
    print(" 2. Moderate")
    print(" 3. Advanced")
    
    while True:
        choice = input("Select difficulty level (1-3): ")
        if choice in ["1", "2", "3"]:
            return int(choice)
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

# Function to generate a random integer based on difficulty level
def randomInt(difficulty):
    if difficulty == 1:       # Easy: single-digit
        return random.randint(1, 9)
    elif difficulty == 2:     # Moderate: double-digit
        return random.randint(10, 99)
    else:                     # Advanced: four-digit
        return random.randint(1000, 9999)

# Function to randomly decide whether the operation is addition or subtraction
def decideOperation():
    return random.choice(['+', '-'])

# Function to display a problem and get user's answer
def displayProblem(num1, num2, operation):
    while True:
        try:
            answer = int(input(f"{num1} {operation} {num2} = "))
            return answer
        except ValueError:
            print("Please enter a valid integer.")

# Function to check if the user's answer is correct
def isCorrect(user_answer, num1, num2, operation):
    if operation == '+':
        correct = num1 + num2
    else:
        correct = num1 - num2
    
    if user_answer == correct:
        print("Correct! ✅")
        return True
    else:
        print("Incorrect. Try again.")
        return False

# Function to display final results
def displayResults(score):
    print("\n--- Quiz Results ---")
    print(f"Your score: {score} / 100")
    
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "F"
        
    print(f"Your grade: {grade}\n")

# Main program
def quiz():
    while True:
        difficulty = displayMenu()
        score = 0

        for _ in range(10):  # 10 questions
            num1 = randomInt(difficulty)
            num2 = randomInt(difficulty)
            operation = decideOperation()

            # First attempt
            user_answer = displayProblem(num1, num2, operation)
            if isCorrect(user_answer, num1, num2, operation):
                score += 10
            else:
                # Second attempt
                user_answer = displayProblem(num1, num2, operation)
                if isCorrect(user_answer, num1, num2, operation):
                    score += 5

        displayResults(score)

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye!")
            break

# Run the quiz
quiz()

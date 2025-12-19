import random

# Function to show difficulty menu and receive the choice of the user.
def displayMenu():
print("DIFFICULTY LEVEL")
print(" 1. Easy")
print(" 2. Moderate")
print(" 3. Advanced")

while True:
choice = input choice choice = input("/level of difficulty: 1-3):
if choice in ["1", "2", "3"]:
return int(choice)
else:
print("Invalid input. Please enter 1, 2, or 3.")

## Random number generator with level of difficulty.
def randomInt(difficulty):
=== when difficulty = 1:
. Easy: Many-digit: single -digit
return random.randint(1, 9)
elif difficulty =2: et. al. Moderate: double-digit
return random.randint(10, 99)
else: # Advanced: four-digit
return random.randint(1000, 9999)

# Function to choose the operation to be performed, that is addition or subtraction, randomly.
def decideOperation():
return random.choice(['+', '-'])

To present a problem and receive an answer of the user.
The def displayProblem takes the following model: def displayProblem(num1, num2, operation):
while True:
try:
answer = int(input(f Notice num1 num2 = operation num1 num2 = operation num1 num2 = observation num1 num1 num1 num1 num1 num1 num1 num1 num1 num1 num1: Now carefully indexed transactions and reversed the result to get this number: Number Command Response Command result Index Response Command result ($ 2)
importance:"))
return answer
except ValueError:
Some valid integer can be entered by the user by typing in a print statement.

# Check if the answer provided by the user is correct
|human|>Function to check whether the answer given by the user is correct or not.
test valid user-answer,num1,num2 operation Correct(user-answer,num1,num2,operation):
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

# Function to portray the final results.
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

for _ in range(10): # 10 questions
num1 = randomInt(difficulty)
num2 = randomInt(difficulty)
operation = decideOperation()

# First attempt
user answer = while number one, number two and operation num1 num 2 operation
|human|>user answer= displayProblem(num1, num2 operation)
in case isCorrect(user answer,num1,num 2, operation):
score += 10
else:
# Second attempt
user answer = while number one, number two and operation num1 num 2 operation
|human|>user answer= displayProblem(num1, num2 operation)
in case isCorrect(user answer,num1,num 2, operation):
score += 5

displayResults(score)

play again = input as follows: do you wish to play again? (y/n): play again.
if play_again != 'y':
print("Thanks for playing! Goodbye!")
break

# Run the quiz
quiz()

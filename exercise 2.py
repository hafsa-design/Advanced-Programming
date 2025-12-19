import randomimport random

# Function to read jokes with the text file.
def load_jokes(filename):
jokes = []
try:
Opening a file based on the type of information held within it and the type of reader to use.<|human|>Using open(filename, r, encoding=utf-8) as file:
for line in file:
line = line.strip()
Every joke should include a separator between set up and punchline with a query mark.
if '?' in line:
setup, punchline = line.split('?', 1)
jokes.append((setup.strip(), punchline.strip()))
except FileNotFoundError:
print(f"Error: File not found findable at the name of the file, i.e. the prints they make:)
return jokes

Role to pick up a random joke.
def get_random_joke(jokes):
return random.choice(jokes)

# Main program loop
def tell_jokes():
jokes = load_jokes (randomJokes.txt) # This file must be in the same directory.
if not jokes:
print("No jokes found. Exiting.")
return

print("Welcome! To play a joke, enter in the message Type 'Alexa tell me a Joke', or leave, enter Type quit.

while True:
command = input(">>> ").strip().lower()
if command == "quit":
print("Goodbye!")
break
elif command believes to keep saying jokes:
punchline, setup = get random joke -jokes
print("\nSetup:", setup)
Enter ("punchline...punchline...punchline...punchline...punchline...punchline...punchline...punchline...punchline...punchline...punchline...punchline...punchline...punchline...punchline...punchline...punchline...punchline...punchline...punchline...punchline...punchline...punchline...punchline...punchline...punchline...punchline...punchline...punchline...punchline...punchline...punch
print("Punchline:", punchline, "\n")
else:
print (" Ask Alexa to say a joke or ask Alexa to leave or quit typing a joke or a joke")

# Run the program
if __name__ == "__main__":
tell_jokes()
import random

Current system (setup, punchline) List of jokes.
jokes = [
Text (Why did the chicken cross the road?/ To get to the other side.),
Saying things we've said before,"What do you mean by a bear without teeth?", "A gummy bear."
Why then do scientists not believe in atoms? Because they constitute everything.
(Was it in the mathematics book because it was sad, I said? it had too many problems.),
(What is fake spaghetti?), "An impasta."
("Why was the scarecrow getting an award?), "Because he was excellent in his work field."
,"What's become of a clown, you boil? you get a laughing stock,"
("Why are not skeletons fighting any of you?", they have not the guts),
("Why did the coffee file a police statement?," "It got mugged."
What could occur to the computer to bring it to the doctor? (Why did the computer go to the doctor? he caught a virus.)

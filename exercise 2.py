import random

# Function to load jokes from the text file
def load_jokes(filename):
    jokes = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                # Each joke must have a '?' separating setup and punchline
                if '?' in line:
                    setup, punchline = line.split('?', 1)
                    jokes.append((setup.strip(), punchline.strip()))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return jokes

# Function to select a random joke
def get_random_joke(jokes):
    return random.choice(jokes)

# Main program loop
def tell_jokes():
    jokes = load_jokes("randomJokes.txt")  # Make sure this file is in the same folder
    if not jokes:
        print("No jokes found. Exiting.")
        return

    print("Welcome! Type 'Alexa tell me a Joke' to hear a joke, or 'quit' to exit.")

    while True:
        command = input(">>> ").strip().lower()
        if command == "quit":
            print("Goodbye!")
            break
        elif command == "alexa tell me a joke":
            setup, punchline = get_random_joke(jokes)
            print("\nSetup:", setup)
            input("Press Enter for the punchline...")
            print("Punchline:", punchline, "\n")
        else:
            print("Try typing: Alexa tell me a Joke or quit")

# Run the program
if __name__ == "__main__":
    tell_jokes()
import random

# List of jokes (setup, punchline)
jokes = [
    ("Why did the chicken cross the road?", "To get to the other side."),
    ("What do you call a bear with no teeth?", "A gummy bear."),
    ("Why don’t scientists trust atoms?", "Because they make up everything."),
    ("Why did the math book look sad?", "Because it had too many problems."),
    ("What do you call fake spaghetti?", "An impasta."),
    ("Why did the scarecrow win an award?", "Because he was outstanding in his field."),
    ("What happens if you boil a clown?", "You get a laughing stock."),
    ("Why don’t skeletons fight each other?", "They don’t have the guts."),
    ("Why did the coffee file a police report?", "It got mugged."),
    ("Why did the computer go to the doctor?", "Because it caught a virus.")
]


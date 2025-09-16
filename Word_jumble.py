import random

# Word list with hints
words_with_hints = {
    "python": "A popular programming language 🐍",
    "keyboard": "You type on this ⌨️",
    "developer": "Someone who writes code 👩‍💻",
    "science": "Systematic study of nature 🔬",
    "student": "A person who is learning 📚",
    "computer": "An electronic machine 💻",
    "variable": "A container for storing data 🔢",
    "function": "Block of code that does a task ⚙️"
}

def word_jumble():
    print("👉 Welcome to Word Jumble!")
    print("Unscramble the letters to form a word. Type 'quit' to stop.\n")

    word = random.choice(list(words_with_hints.keys()))
    hint = words_with_hints[word]
    scrambled = "".join(random.sample(word, len(word)))

    print(f"Scrambled word: {scrambled}")
    print(f"💡 Hint: {hint}")

    while True:
        guess = input("Your guess: ").lower()

        if guess == "quit":
            print("🚪 You quit the game. The word was:", word)
            break
        elif guess == word:
            print("🎉 Correct! The word was:", word)
            break
        else:
            print("❌ Wrong guess, try again!")

# Run game
word_jumble()

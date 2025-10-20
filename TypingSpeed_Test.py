import time
import random

# List of sample words
words = [
    "python", "developer", "keyboard", "programming", "speed",
    "accuracy", "function", "variable", "project", "learning",
    "typing", "challenge", "computer", "science", "student"
]

def typing_test():
    print("👉 Welcome to Typing Speed Test!")
    print("You will be shown 5 random words to type.")
    print("Type them as fast and accurately as you can.\n")
    
    # Choose random words
    test_words = random.sample(words, 5)
    print("Words to type:")
    print(" ".join(test_words))
    
    input("Press ENTER when you are ready...")

    # Start timing
    start_time = time.time()
    typed_text = input("\nType here: ")
    end_time = time.time()

    # Calculate results
    time_taken = end_time - start_time
    words_typed = typed_text.split()
    
    # Accuracy calculation
    correct = 0
    for i in range(len(test_words)):
        if i < len(words_typed) and words_typed[i] == test_words[i]:
            correct += 1

    accuracy = (correct / len(test_words)) * 100
    wpm = (len(words_typed) / time_taken) * 60

    print("\n⏱ Time Taken: {:.2f} seconds".format(time_taken))
    print("💨 Speed: {:.2f} words per minute".format(wpm))
    print("✅ Accuracy: {:.2f}%".format(accuracy))

# Run the game
typing_test()


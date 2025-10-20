import random

choices = ["rock", "paper", "scissors"]

def rps_game():
    print("👉 Welcome to Rock, Paper, Scissors!")
    print("Best of 5 rounds wins the game.\n")
    
    player_score = 0
    computer_score = 0
    rounds = 0

    while rounds < 5:
        player = input("Enter rock, paper, or scissors: ").lower()
        if player not in choices:
            print("⚠️ Invalid choice! Try again.\n")
            continue

        computer = random.choice(choices)
        print(f"Computer chose: {computer}")

        if player == computer:
            print("🤝 It's a tie!")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("✅ You win this round!")
            player_score += 1
        else:
            print("❌ Computer wins this round!")
            computer_score += 1

        rounds += 1
        print(f"Score → You: {player_score} | Computer: {computer_score}\n")

    print("🏆 Final Result:")
    if player_score > computer_score:
        print("🎉 You win the game!")
    elif computer_score > player_score:
        print("💻 Computer wins the game!")
    else:
        print("🤝 It's a tie overall!")

# Run game
rps_game()



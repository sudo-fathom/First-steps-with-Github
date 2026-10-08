import random
import time
print("Welcome to the game of Rock, Paper, Scissors!")

print("1. Rock")
time.sleep(1)
print("2. Paper")
time.sleep(1)
print("3. Scissors")
time.sleep(1)

while True:
    user_input = int(input("Enter your choice: "))
    if user_input in [1, 2, 3]:
        computer_input = random.randint(1, 3)
        print(f"Computer chose: {computer_input}")

        if user_input == computer_input:
            print("It's a tie!")
            time.sleep(1)
        elif (user_input == 1 and computer_input == 3) or (user_input == 2 and computer_input == 1) or (user_input == 3 and computer_input == 2):
            print("You win!")
            time.sleep(1)
        else:
            print("You lose!")
        time.sleep(1)
        print("Do you want to play again? (y/n): ")
        play_again = input().lower()
        if play_again != 'y':
            time.sleep(2)
            print("Thanks for playing!")
            break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
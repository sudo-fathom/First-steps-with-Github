import random

prizes = ["Rolls Royce 2026", "Pizza", "Polo T-shirt", "Xiaomi Microwave", "Macbook Pro", "iphone 18 pro"]

def available_prizes():
    print("Available prizes:")
    for i in range(len(prizes)):
        print(f"{i+1}. {prizes[i]}")

available_prizes()

dice = random.randint(1,6)

def roll_dice():
    print("Rolling the dice...")
    print(f"You rolled a {dice}!")
    
    if dice == 1:
        print(f"Congratulations! You won a {prizes[0]}!")
    elif dice == 2:
        print(f"Congratulations! You won a {prizes[1]}!")
    elif dice == 3:
        print(f"Congratulations! You won a {prizes[2]}!")
    elif dice == 4:
        print(f"Congratulations! You won a {prizes[3]}!")
    elif dice == 5:
        print(f"Congratulations! You won a {prizes[4]}!")
    elif dice == 6:
        print(f"Congratulations! You won a {prizes[5]}!")
    else:
        print("Invalid roll. Please try again.")
roll_dice()
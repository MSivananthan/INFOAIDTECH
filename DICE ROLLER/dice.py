import random

def roll_dice(num_dice):
    results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        results.append(roll)
    return results

def main():
    print("Welcome to the Dice Rolling App!")
    while True:
        num_dice = int(input("Enter the number of dice to roll: "))
        dice_results = roll_dice(num_dice)
        print("Dice Results:", dice_results)
        choice = input("Roll  the dice again? (yes/no): ")
        if choice.lower() != 'yes':
            break
    print("Quit Dice Rolling App!")

if __name__ == "__main__":
    main()

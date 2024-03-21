import random

# Unicode characters for dice faces
dice_faces = [
    '\u2680',  # ⚀
    '\u2681',  # ⚁
    '\u2682',  # ⚂
    '\u2683',  # ⚃
    '\u2684',  # ⚄
    '\u2685'  # ⚅
]


def roll_dice():
    """Simulate rolling two dice."""
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2


def display_roll(dice1, dice2):
    """Display the outcomes of rolling two dice."""
    print(f"Die 1: {dice_faces[dice1 - 1]}")
    print(f"Die 2: {dice_faces[dice2 - 1]}")


def main():
    """Main function to roll the dice and display the outcomes."""
    print("Welcome to PyDiceRoll!")
    input("Press Enter to roll the dice...")

    dice1, dice2 = roll_dice()
    display_roll(dice1, dice2)


if __name__ == "__main__":
    main()

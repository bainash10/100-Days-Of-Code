import random

def generate_random_chars():
    return str(random.choice('012'))

player = int(input("Enter 0 for snake, 1 for water, and 2 for gun: "))
print("The player chose", player)
computer = generate_random_chars()
print("The computer chose", computer)

if computer == '0' and player == 0:
    print("This is a draw")
elif computer == '0' and player == 1:
    print("You lose")
elif computer == '0' and player == 2:
    print("You win")
elif computer == '1' and player == 0:
    print("You win")
elif computer == '1' and player == 1:
    print("This is a draw")
elif computer == '1' and player == 2:
    print("You lose")
elif computer == '2' and player == 0:
    print("You lose")
elif computer == '2' and player == 1:
    print("You win")
elif computer == '2' and player == 2:
    print("This is a draw")
else:
    print("Nothing")

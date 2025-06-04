# Import Modules
import random
import time

def roll_dice():
    return random.randint(1, 6)

input("Press Enter to roll the dice...")
print("Rolling the dice...")
switch = True
for i in range(10):
    switch = not switch
    # Simulate rolling animation
    if switch:
        print("Rolling.../", end="\r")
    else:
        print("Rolling...\\", end="\r")
    time.sleep(0.2)  # Simulate the rolling time

print(f"You rolled a {roll_dice()}")
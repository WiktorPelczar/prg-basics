###
# The program simulates five dice rolls.
#
import random
print("Dice rolling simulator")
for i in range(7):
    dice_roll = random.randint(1,8)
    print(dice_roll, end=" ")

import random

i = 0
while i < 5:
    side = random.randint(0, 1)
    if side == 1:
        print("Heads!")
    elif side == 0:
        print("Tails!")
    i += 1
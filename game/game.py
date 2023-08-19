import random
import sys
while True:
    try:

        n = int(input("LEVEL: "))

        if n > 0:
            level = random.randint(1,n)
            break
    except ValueError:
        continue

while True:
    try:

        guess = int(input("Guess: "))
        if guess < level:
            print("Too small!")
        elif guess > level:
            print("Too large!")
        else:
            print("Just right!")
            sys.exit()
    except ValueError:
        continue

#NB P7 number guessing game

import random

answer = random.randint(1, 100)
guess_count = 0

while guess_count < 6:
	guess = int(input("Guess a number from 1 to 100: "))
	guess_count += 1
	if guess == answer:
		print(f"Correct you got it in {guess_count} tries!")
		break
	elif guess < answer:
		print("Guess higher")
	else:
		print("Guess lower")
if guess_count == 6:
	print(f"Your out of tries. The answer was {answer}")

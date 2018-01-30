#!/usr/bin/python3

import sys, random

assert sys.version_info >= (3,4), "This script requires at least Python 3.4"

#variables
guesses = 10
guess_range = 20
quit = False

#generate a random integer between 1 and 20 (inclusive) and store it in the variable [number]
while quit == False:
	number = random.randint(1,guess_range)
	trap = random.randint(1,guess_range)
	#ask the user for a response and store it in the variable [guess]

	print('This is the rebel attack on the Deathstar. We need to shutdown the Empires defenses!')

	#a try/except block is a great tool for programmers to be able to deal with errors. In this instance, it reports an error if the user enters something other than an integer
	for count in range(guesses):
		try:
			guess = input( 'Please enter a number 1-{0} to hack the empires shields (you have {1} guesses left): '.format(guess_range, guesses-count))
		#convert the guess to an integer
			guess = int(guess)
				#check if the guess is less than the random number'
			while trap == number:
				trap = random.randint(1,guess_range)
			if guess == trap:
				print('Admiral Akbar voice- Its a Trap! (The empire has detected our attack)')
				break
			if guess < number:
				print('Too low!')
				#check if the guess is more than the random number
			if guess > number:
				print('Too high!')
			if guesses == 0:
				print('The empire has detected our attack!')
			if guess == number:
				print('You have infiltrated the empires defense systems and shutdown the deathstar shields (You Win!)')
				break
		except ValueError:
			print('Please enter a whole number.')
	play_again = input('The rebellion still needs your assistance: play again Y/N?')
	if play_again.upper() == 'Y':
		print('Ready?')
	if play_again.upper() == 'N':
		quit = True

print('Thanks for helping the resistance!')
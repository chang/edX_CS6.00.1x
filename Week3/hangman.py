"""
My solution to problem set 3: hangman.
"""

import random

def getWords():
	'''
	Returns list of words from 'words.txt'
	'''
	words = open('words.txt')
	words = words.readlines()
	words = words[0].split(' ')
	return words

def randomWord(words):
	'''
	Returns random word from list `words`
	'''
	return words[random.randrange(0, len(words))]

def isWordGuessed(secretWord, lettersGuessed):
	'''
	returns true if all letters in secret_word have been guessed in list guessed_letters
	'''
	trueList = []
	for letter in secretWord:
		trueList.append(letter in lettersGuessed)
	return all(trueList)

def getGuessedWord(secretWord, lettersGuessed):
	'''
	returns string with masked letters
	'''
	guessed_word = ""

	for letter in secretWord:
		if letter in lettersGuessed:
			guessed_word += letter + " "
		else:
			guessed_word += "_ "

	return guessed_word

def getAvailableLetters(lettersGuessed):
	'''
	returns remaining letters of the alphabet
	'''
	abc = ""

	for letter in 'abcdefghijklmnopqrstuvwxyz':
		if letter not in lettersGuessed:
			abc += letter + " "
		else:
			abc += "_ "

	return abc

def hangman():
	'''
	starts a game of hangman
	'''
	word = randomWord(getWords())
	guessed_letters = []
	wrong_guesses = 0
	finish = False

	# Print opening instructions
	print("Welcome to hangman. Your word has", str(len(word)), 'letters.', 'You get', str(NUMBER_INCORRECT_ALLOWED), "incorrect guesses.")

	while finish == False:
		# Instructions
		print("\nYour word:\n" + getGuessedWord(word, guessed_letters))
		print("Remaining letters:\n" + getAvailableLetters(guessed_letters))

		# Get guess, append to list
		guess = input("Enter a letter: ")
		guessed_letters.append(guess[0].lower())

		# Evaluate guess
		if guess in word:
			print("Good guess!")
		else:
			wrong_guesses += 1
			if wrong_guesses >= NUMBER_INCORRECT_ALLOWED:
				print("You lost, sucker.")
				finish = True
			else:			
				print("You suck.", str(NUMBER_INCORRECT_ALLOWED - wrong_guesses), "incorrect guesses remaining.")

		# Finishing conditions
		if isWordGuessed(word, guessed_letters):
			print("You won!")
			finish = True
			
# Start game
NUMBER_INCORRECT_ALLOWED = 5
hangman()







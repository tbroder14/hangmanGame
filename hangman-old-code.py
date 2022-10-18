import randomword
from time import sleep

# TODO 
# Present to user fancy hangman graphics
# Get a word from random_word
# tell the user how many letters are in the word
# ask the user for their first guess
# if guess is equal to a letter, print that letter with the appropriate other underscores
# if guess is incorrect, notify user and detract from number of guesses
# also, print letters guessed with strikethrough on letter
# rinse and repeat until either the user correctly guesses the word or they run out of guesses 

sleep(0.5)
print("Welcome to Hangman!")

incorrectGuesses = []
correctGuesses = []

# randomWord = randomword.get_random_word()
randomWord = "test"
print(randomWord)

numberOfDashes = len(randomWord)
print(f"The word to win has {numberOfDashes} letters.")

# this is looping for each letter in randomWord and printint out an underscore for each letter
for letter in randomWord:
	print("_", end=" ")

while True:

	guess = input("\n" + "What is your guess?" + "\n")

	correctGuess = False
	# loop through each letter of our random word
	for letter in randomWord:
		if guess == letter:
			correctGuess = True

	# what happens if they guess correctly
	if correctGuess == True:
		# print out letter with underscore and underscores for the other unknown letters
		for letter in randomWord:
			if guess == letter:
				print(letter, end=" ")
				correctGuesses.append(guess)
					# print(correctGuesses)
			elif letter in correctGuesses:
				print(letter, end=" ")
			else:	
				print("_", end=" ")	 

	else:
		# assign number of guesses to a variable
		incorrectGuesses.append(guess)
		print("You guessed incorrectly!")
		print(incorrectGuesses)

	# function - compare the number of letters in correctGuesses to the number of letters in the random word
	# if the number of letters is the same, the person is a winner! 
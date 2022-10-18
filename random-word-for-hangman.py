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

# provide an error message if they've used that letter before
# prevent the input of anything but a single letter
# if the user inputs "hint," they get one letter for free 

sleep(0.5)
print("Welcome to Hangman!")

incorrectGuesses = []
correctGuesses = []

randomWord = randomword.get_random_word()
# randomWord = "test"

# converts the list into a dictionary (to eliminate duplicates) and then sorts the list into alphabetical order 
randomWordDict = list(sorted((dict.fromkeys(randomWord))))

numberOfDashes = len(randomWord)
print(f"The word to win has {numberOfDashes} letters.")

# this is looping for each letter in randomWord and printint out an underscore for each letter
for letter in randomWord:
	print("_", end=" ")

attempts = 5

while attempts >= 0:

	guess = str(input("\n" + "What is your guess?" + "\n"))

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
				correctGuesses = list(sorted(dict.fromkeys(correctGuesses)))
				# print(correctGuesses)
			elif letter in correctGuesses:
				print(letter, end=" ")
			else:	
				print("_", end=" ")
		if correctGuesses == randomWordDict:
			print("\n" + f"You guessed the right word! The word was {randomWord}. Congratulations!")
			break

	# if the player guesses the same incorrect letter twice, add an attempt 	
	else:
		for letter in incorrectGuesses:
			if guess == letter:
				attempts = attempts + 1
		
		incorrectGuesses.append(guess)
		incorrectGuesses = list(dict.fromkeys(incorrectGuesses))
				
		print(f"You guessed incorrectly! You have {attempts} attempts left.")
		print(incorrectGuesses)	
		# decrease the number of guesses by one after each incorrect attempt
		attempts = attempts - 1

	# # correct code 
	# else:
	# 	incorrectGuesses.append(guess)
	# 	incorrectGuesses = list(dict.fromkeys(incorrectGuesses))
	# 	print(f"You guessed incorrectly! You have {attempts} attempts left.")
	# 	print(incorrectGuesses)	
	# 	# decrease the number of guesses by one after each incorrect attempt
	# 	attempts = attempts - 1


# did this becuase attempts == 0 was ending the game even though there was one attempt left
# it would skip the final attempt; probably becuase it would print there is 1 attempt left and then minus 1 to zero
if attempts == -1:
   print(f"You ran out of guesses. Nice try though! The word was {randomWord}.")


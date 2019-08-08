import word_game
import random
wordList = []
guessesRemaining = 4
won = 0
wordList = random.sample(word_game.candidateWords,8)
password = random.choice(wordList)
print password
print "\nWelcome to the Guess-The-Word Game."
print "Password is one of these words:"
while(guessesRemaining>0):
  for index, item in enumerate(wordList):
    print "(",index,").", item
  print "\nGuesses remaining:",guessesRemaining 
  guessesRemaining = guessesRemaining - 1
  guessNum = int(raw_input("Guess (enter 0-7):"))	
  print "\n",wordList[guessNum]
  if wordList[guessNum] == password:
	won = 1
	break
  else:
	match = word_game.compareWords(wordList[guessNum], password)
	print "Password Incorrect"	
	print match,"/ 6 corect\n"
if won == 1 :
  print "\nPassword Correct."
  print "Congratulations, You win"
else: 
  print "You lose"



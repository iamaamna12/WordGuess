

#Word Bank
#First, we'll need to create a word bank of all the possible words to be guessed, and randomly select one to be the correct answer. 
# This way, the game has an element of mystery and surprise! 🔍🕵
import random

print('\n ▶️ You have to guess the social media platform ◀️ ')
word_bank = ['instagram', 'twitter', 'facebook', 'tiktok', 'snapchat', 'tumblr', 'threads']

word = random.choice(word_bank)

guessedWord = ['_'] * len(word)

attempts = 10

#Game Loop
#We need to create a while loop so the player can continuously guess until they run out of attempts or guess the word correctly. 🔁

while attempts > 0:

    print('\nCurrent word: ' + ' '.join(guessedWord))
    guess = input ('\nGuess a letter: ')

    if guess in word:
      for i in range(len(word)):
       if word[i] == guess:
        guessedWord[i] = guess
      print('\n😎 Wow! Great guess! 🎉')

    else:
        attempts -= 1
        print('\n🫣 Wrong guess! Attempts left: ' + str(attempts))

    if '_' not in guessedWord:
        print('\n🎉 Congratulations!! You guessed the word: ' + word)
        break

    #Only shows the below message when the player lost all the attempts

    if attempts == 0:
        print('\n😔 You have run out of attempts! The word was: ' + word)





  



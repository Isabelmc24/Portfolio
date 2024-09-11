import random

words = ['lonestar', 'longhorn', 'cowboys', 'rangers', 'dallas']

selected_word = random.choice(words)
letter_count = ['_' for _ in selected_word]
attempts = 10

print("Welcome to Texan Hangman!")

while attempts > 0 and '_' in letter_count:
    print("\n" + ' '.join(letter_count))
    guess = input("Guess letter: ").lower()
    if guess in selected_word:
        for index, letter in enumerate(selected_word):
            if letter == guess:
                letter_count[index] = guess
    else:
        print("This letter is not in the hidden word. Please try again!")
        attempts -= 1

if '_' not in letter_count:
    print("Congratulations! You guessed the word!")
    print(' '.join(letter_count))

else:
    print("Sorry you lost...the word was: " + selected_word)

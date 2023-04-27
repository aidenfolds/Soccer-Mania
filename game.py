import random


# Aiden Folds
# Soccer Mania
# The goal of this game is to correctly answer each question to pass the defenders and score on the goalie
def main():
    print("Welcome to Soccer Mania!")
    print('')
    print("The score is 2-2 in the final minute of the Quarter-Final game.")
    print("To win the game all you have to do is guess the word I'm thinking of.")
    print('')
    print("I'll give you a hint, it's a type of fruit")
    # list of words to choose from
    words = ["orange", "apple", "banana", "watermelon", "grape", "mango", "kiwi", "lemon", "lime", "cherry"]

    # choose a random word from the list
    word = random.choice(words)

    # create a list of underscores to represent the hidden word
    hidden_word = ["_"] * len(word)

    # set the number of guesses
    max_guesses = 6
    num_guesses = 0

    # keep track of the guessed letters
    guessed_letters = []

    # function to check if the player has won
    def has_won():
        return "_" not in hidden_word

    # loop until the player wins or runs out of guesses
    while not has_won() and num_guesses < max_guesses:
        # print the current state of the game
        print(" ".join(hidden_word))
        print(f"Guesses remaining: {max_guesses - num_guesses}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        # get the player's guess
        guess = input("Guess a letter: ")

        # check if the guess is correct
        if guess in word:
            print("Correct!")
            # update the hidden word with the guessed letter
            for i in range(len(word)):
                if word[i] == guess:
                    hidden_word[i] = guess
        else:
            print("Incorrect.")
            num_guesses += 1

        # add the guessed letter to the list of guessed letters
        guessed_letters.append(guess)

    # print the final state of the game
    if has_won():
        print("Congratulations, you won!")
    else:
        print(f"Sorry, you lost. The word was {word}.")

    print('')

    print("You will now do some math problems to try and win the Semi-Final game.")
    print("Answer each question correctly to dribble around the defenders.")
    print("If you answer these following questions successfully, you will go on to play in the Semi-Final game.")
    print("The questions will only get harder resulting in the final question being the hardest")
    print('')

    # This question is using addition.
    print("You are trying to perform a move. answer this question to successfully do so.")
    answer1 = int(input("What is 10+15? "))
    if answer1 == 10 + 15:
        print("Congratulations! ")
        print("You managed to pull off the move and pass the first defender.")
    else:
        print("False! The defender stole the ball resulting in them scoring.")
    print('')
    print("The time left on the clock is now 53 seconds! ", end="Hurry!")
    print('')

    # This question is using multiplication.
    print("You are attempting a nutmeg on your opponent. Answer this question successfully to do so.")
    answer2 = int(input("What is 3*20? "))
    if answer2 == 3 * 20:
        print("Nice Job! You cleared the defender.")
        print("You are getting closer and closer!")
    else:
        print("Nice try. The ball was stolen from you.")
    print('')

    # This question is using an exponent.
    print("The opponent is coming in for a slide tackle! Get this question right to jump over it.")
    answer3 = int(input("What is 8**3? "))
    if answer3 == 8 ** 3:
        print("Good going! Way to avoid that tackle!")
    else:
        print("Incorrect. The opponent slide right through you and stole the ball.")
    print('')
    print("With 34 second one the clock", "you are nearing the 18 yard box.", sep=", ")
    print('')

    # This question is using subtraction and division.
    print(
        "Your teammate's open for the pass so you are crossing it to them. Answer this question successfully to do so.")
    answer4 = int(input("What is (100-48)/4? "))
    if answer4 == (100 - 48) / 4:
        print("Way to go!")
        print("Your teammate received the pass")
    else:
        print("Bummer! The pass was intercepted.")
    print('')
    print("Your teammate is dribbling down the sidelines looking for a cross")
    print('')

    # This question is using division with integral result.
    print("Get this question correct to get in the box to have correct positioning for the cross.")
    answer5 = int(input("What is 11//4? "))
    if answer5 == 11 // 4:
        print("Correct! You are not in the 18 yard box ready for the cross.")
    else:
        print("Nope. You aren't in the correct positioning resulting in a turnover.")
    print('')

    # This question is using modulo.
    print("Your teammate crossed the ball. Answer this question successfully to head the ball into the net.")
    answer6 = int(input("What is 5*(17%12)? "))
    if answer6 == 5 * (17 % 12):
        print("Goal!" * 10)
        print("You are a winner! " + "Congrats on winning the Semi-Final game!")
    else:
        print("A header and a miss! You just missed the game winning header to lose the game.")
    print('')
    print("With just a minute left on the clock", "you did the unthinkable", sep=", ")
    print('')

    # Since you answered the previous questions correctly, you will now try to guess a number.
    # If you guess the number correctly, you win the Championship game. If you guess it wrong, you will lose.

    print("You will now play Bayern FC in the Championship game.")
    print("Guess the number right and you win, guess wrong and you lose.")
    print("Welcome to Guess the Number game!")
    print("I am thinking of a number between 1 and 20.")
    print("You have 5 attempts to guess it.")

    secret_number = random.randint(1, 20)
    attempts_left = 5

    while attempts_left > 0:
        print("Attempts left:", attempts_left)
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print("Congratulations! You guessed the number!")
            break
        elif guess < secret_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

        attempts_left -= 1

    if attempts_left == 0:
        print("Sorry, you ran out of attempts. The secret number was", secret_number)

    print("You did it! You won the Championship game!")
    print("Congratulations! Good job!")

    # This uses string operators, multiplication and addition.
    str1 = "Thanks "
    str2 = "for "
    str3 = "playing!"
    str4 = "!"

    # combine str1, str2, and str3 to make a sentence
    print(str1 + str2 + str3 + str4 * 10)


main()
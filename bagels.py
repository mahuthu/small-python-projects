#BAGELS


#In Bagels, a deductive logic game, you
#must guess a secret three-digit number
#based on clues. The game offers one of
#the following hints in response to your guess:
#“Pico” when your guess has a correct digit in the
#wrong place, “Fermi” when your guess has a correct
#digit in the correct place, and “Bagels” if your guess
#has no correct digits. You have 10 tries to guess the
#secret number.

#Keep in mind that this program uses not integer values but rather string
#values that contain numeric digits. For example, '426' is a different value
#than 426. We need to do this because we are performing string comparisons
#with the secret number, not math operations. Remember that '0' can be
#a leading digit: the string '026' is different from '26', but the integer 026 is
#the same as 26.

import random
num_digits = 3
max_guess = 10 

def main():
    print('''Bagels, a deductive logic game.
             By Al Sweigart al@inventwithpython.com
            
             I am thinking of a {}-digit number with no repeated digits.
             Try to guess what it is. Here are some clues:
             When I say: That means:
             Pico One digit is correct but in the wrong position.
             Fermi One digit is correct and in the right position.
             Bagels No digit is correct.
            
             For example, if the secret number was 248 and your guess was 843, the
             clues would be Fermi Pico.'''.format(num_digits))
    while True:
        secret_num = getSecretNum()
        print("i have thought up a number")
        print("You have {} guesses to get it right".format(max_guess))
    
        num_guesses = 1
        while num_guesses <= max_guess:
            guess = ""
            # Keep looping until they enter a valid guess:
            while len(guess) != num_digits or not guess.isdecimal():
                print("Guess{}:".format(num_guesses))
                guess = input(".")
            clues = getClues(guess, secret_num)
            print(clues)
            num_guesses += 1
            
            if guess == secret_num:
                break
            if num_guesses >= max_guess:
                print("you ran out of guesses")
                print("the answer was{}".format(secret_num))
        
        print("do you want to play again( yes or no)")
        if not input(">").lower().startswith("y"):
            break
    print ("Thanks for playing")
    
    
def getClues(guess, secret_num):
    """Returns a string with the pico, fermi, bagels clues for a guess
    73. and secret number pair."""
    if guess == secret_num:
        return "you got it"
    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[1]:
            clues.append("fermi")
        elif guess[i] != secret_num[i]:
            clues.append("pico")
    if len(clues) == 0:
        return "bagels"
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return " ".join(clues)
    
def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789') # Create a list of digits 0 to 9.
    random.shuffle(numbers) # Shuffle them into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ""
    for i in range(len(num_digits)):
        secretNum += str(numbers[i])
    return secretNum



    
    
if __name__ == "__main__":
    main()

        

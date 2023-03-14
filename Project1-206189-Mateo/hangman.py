# Raymund Neil T. Mateo, 201104
# March 12, 2023

# I/we certify that this submission complies with the DISCS Academic Integrity
# Policy.

# If I/we have discussed my/our Python language code with anyone other than
# my/our instructor(s), my/our groupmate(s), the teaching assistant(s),
# the extent of each discussion has been clearly noted along with a proper
# citation in the comments of my/our program.

# If any Python language code or documentation used in my/our program
# was obtained from another source, either modified or unmodified, such as a
# textbook, website, or another individual, the extent of its use has been
# clearly noted along with a proper citation in the comments of my/our program.

################################################################################

# cite your sources here, if any

################################################################################
#Intro
print("LET'S PLAY HANGMAN \n")

#Input word
word = input("Please enter a word for the other player to guess: \n")

#To split the word into letters
list_word = list(word)

#Convert the word into dashes to hide it
dashed_word = ['-'] * len(list_word)

def check(list_word, guess):
    for n in range(len(list_word)):
        if list_word[n] == guess:
            return True

#Number of guesses
num_guesses = int(input("Please enter the number of guesses allowed: \n"))
    
# yung turning hidden word na list to string
while num_guesses > 0:
    
    # putting empty list in string
    guesses_left = f"Guess the word: {num_guesses} guess(es) left: "
    for i in dashed_word:
        guesses_left += i
    print (guesses_left)
            
    # cross checking kung nandun yung hula
    guess = input()
    
    # Unused letters
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_letters = ""
    guessed_list = []
    for letter in letters:
        if letter == guess:
            continue
        else:
            new_letters += letter
            letters = new_letters
            guessed_list.append(guess)
    print(f"Unused letters: {letters}")
    
    if check(list_word, guess) == True:
        for n in range(len(list_word)):
            if list_word[n] == guess:
                dashed_word[n] = guess
    else:
        num_guesses -= 1
    
    if dashed_word == list_word:
        print("CONGRATULATIONS! YOU WIN!\n")
        again = input("Would you like to play again? (Yes/No)\n")
        if again == "No":
            break
        elif again == "Yes":
            print("") # Line break
            firstloop = True
            continue
    elif num_guesses == 0:
        print("SORRY, YOU ARE HANGED!")
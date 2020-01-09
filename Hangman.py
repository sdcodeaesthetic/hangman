import random

def scaffold(guesses, word):
    if(guesses == 0):
        print("__________")
        print("|   |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|_________")
    elif(guesses == 1):
        print("__________")
        print("|   |")
        print("|   O")
        print("|")
        print("|")
        print("|")
        print("|_________")
    elif(guesses == 2):
        print("__________")
        print("|   |")
        print("|   O")
        print("|   |")
        print("|   |")
        print("|")
        print("|_________")
    elif(guesses == 3):
        print("__________")
        print("|   |")
        print("|   O")
        print("|  \|")
        print("|   |")
        print("|")
        print("|_________")
    elif(guesses == 4):
        print("__________")
        print("|   |")
        print("|   O")
        print("|  \|/")
        print("|   |")
        print("|")
        print("|_________")
    elif(guesses == 5):
        print("__________")
        print("|   |")
        print("|   O")
        print("|  \|/")
        print("|   |")
        print("|  /")
        print("|_________")
    elif(guesses == 6):
        print("__________")
        print("|   |")
        print("|   O")
        print("|  \|/")
        print("|   |")
        print("|  / \ ")
        print("|_________")
        print("\n")
        print("\nThe word was " + word)
        print("YOU LOSE")
        print("\n")
        print("Do You Want To Play More?")
        print("> Press 1 To Play")
        print("> Press 2 To Quit")
        sd = input("> ")
        sd = int(sd)
        if(sd == 1):
            hgman()
        else:
            quit()



def selectWord():
    file = open('Words.txt')
    words = file.readlines()
    myword = 'a'
    while len(myword) < 4:
        myword = random.choice(words)
        myword = str(myword).strip('[]')
        myword = str(myword).strip("''")
        myword = str(myword).strip("\n")
        myword = str(myword).strip("\r")
    myword = myword.lower()
    return myword



def hgman():
    word = selectWord()
    l = len(word)
    blanks = '_' * l
    word_list = list(word)
    blanks_list = list(blanks)
    new_blanks_list = list(blanks)
    guess_list = []
    guesses = 0

    print("HANGMAN\n")
    scaffold(guesses, word)
    print("\n")
    print("" + ' '.join(blanks_list))
    print("\nGuess a Letter.")

    while guesses < 6:
        guess = input("> ")
        g = len(guess)
        guess = guess.lower()

        if(g > 1):
            print("Stop Cheating! Enter One Letter at a Time.")
        elif(guess == ""):
            print("Don't You Want to Play? Enter Atleast One Letter.")
        elif(guess in guess_list):
            print("You already guessed that letter! Here is what you've guessed:")
            print(' '.join(guess_list))
        else:
            guess_list.append(guess)
            i = 0
            while i < len(word):
                if(guess == word[i]):
                    new_blanks_list[i] = word_list[i]
                i = i + 1

            if(new_blanks_list == blanks_list):
                print("\nYou Guessed The Wrong Letter.")
                guesses = guesses + 1
                scaffold(guesses, word)
                if(guesses < 6):
                    print("\nGuess Again.")
                    print(' '.join(blanks_list))
                    print("")

            elif(new_blanks_list == word_list):
                print("\nYOU WIN!")
                print("\n")
                print("Do You Want To Play More?")
                print("> Press 1 To Play")
                print("> Press 2 To Quit")
                sd = input("> ")
                sd = int(sd)
                if(sd == 1):
                    hgman()
                else:
                    quit()
                
            else:
                blanks_list = new_blanks_list[:]
                print(' '.join(blanks_list))
                print("\nGreat Guess! Guess Another")

hgman()

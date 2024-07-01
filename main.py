# Functions



def intro():


    # Say hello to players
    print("Hello, player")


    # Ask the player their name
    name = input("what's your name")


    # Greet the player and introduce the game
    print("Welcome to this game,", name)
    print("This test tests the player's sensitivity to letter and word combinations")

    # Tell players how to play the game
    print("Our game will give players letters, and players need to look at these letters and input them.")
    print("If the letters are correct, keep it.")
    print("If the executioner is wrong, his life will be lost.")
    print("If you run out of lives, it's game over.")

    # The beginning of the game
    print("We will give you 26 letters and shuffle them.")
    # Play a round
    print("We will tell you the number of letters and you need to enter these letters")


# Main Code

intro()

def playgame():
    
    word = "spiderman"
    guesses = [""]
    chance = 5

    while True:
        guess = input()
        blank = ""
        if guess in word:
            guesses.append(guess)
        else:
            chance -=1
            if chance >=0:
                print("There are only",chance," chances to guess wrong")
                print("Pleace try again")
                continue
            else:
                print("You don't have any chance left")
                print("Game over")
                break

        for letter in word:
            if letter in guesses:
                blank += letter
            else:
                blank += "_"

        print(blank) 
    
        if blank == word:
            print("Good job")
            break
        

play = input("Do you want to play?")

while play == "yes":
     print("The topic is action and fiction film")
     print("You only have 5 chances to guess wrong, if you guess wrong more than 5 times, the game is over")
     playgame()
     paly = input()
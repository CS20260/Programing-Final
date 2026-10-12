# Alexia, Start Room and Plot
#start info
import random
words = ["cat","hat","leave","looser","unwanted","imagine","password"]

inventory = []
# only 7 moves allowed!
moves = 0

outside = 0

word = random.choice(words)
# varaible for  wrong guesses
incorrect = 0
# varable for guessed letters
guessed = []

guesses_left = 6-incorrect
position = 1
with open("win_loss.txt", "r")as file:
    win_loss = file.read().strip().split(",")
#use split(",") on content of the words txt doc to create list of words
#turn win loss into an integer so that we can concatinate
# pull win and loose totals from other txt file and save them as 2 seperate variables
win = int(win_loss[0])

loss = int(win_loss[1])
position == 1





def display(word,guessed):
    # variable for display word (starts as an empty word)
    display_output = ""
    #loop over the correct word (look at every letter)
    for letter in word:
        # check if letter had been guessed
        if letter in guessed:
            # then add the letter to display word
            display_output += letter
            
        # if they havent guessed letter
        else:
            #add underscore to display word
            display_output += "-"


    return display_output
    # return finished display word (OUTSIDE OF LOOP)

print("Hello! You are trapped in a house that is flooding. To survive, you must escape the house. Because the house is flooding, you have limited moves to escape. Good Luck!!!")
#function for room one or basement
def room1(incorrect, position):
    # while true loop for lock
    while True:
        if incorrect <= 0:
            lock = input("""
                        It's Dark. You can't see well. ('cuz it's dark...) You are in the basement, and water is pooling around you ankles. You notice there is a locked door with a lock on it. (WOW! So smart!) Do you sit and accept your fate, or look at the lock? (say SIT or LOOK.)  """).strip().lower()
            if lock == "sit":
                print("You accepted your fate. You drowned. Imagine...")
                position == 7
                break
            elif lock == "look":
                print("""You look at the lock. Its a password code thing. Since you didn't give up, you are going to at least pretend to open the lock. (Yes I'm making you do this. You're welcome!)""")
                ### CODE FOR GUESSING GAME ###
                #### mini game loop (while true) 
                while True:
                    display(word,guessed)
                    # creat variable (ask user to guess letter)
            # creat variable (ask user to guess letter)
                    letter = input("Guess a letter: ").strip().lower()
                    # make a space to make it look better 
                    print("""
                """)
                    # add letter to list of guessed letters
                    if letter in guessed:
                        print("""You guessed this already...
                        
                        
                        """)
                        continue
                    guessed.append(letter)
                    # check "if not letter in word:"
                    if letter not in word:
                        # increase incorrect guesses
                        incorrect += 1

                    # recheck if display word is same as word (call function)
                    current_display = (display(word,guessed))
                    # print function to show display word
                    print(current_display)
                    if current_display == word:
                        # tell user they won
                        print("You finaly got it!")
                        print("""
                            The door swings open. The water is now chest-deep and rising fast. You go out the open door and up some stairs.""")
                        position == 2
                        break
                        #check if they lost (6 wrong guesses)
                    if incorrect == 6:
                        print(f"The code was {word}.")
                        position == 7
                        break
            else:
                print("""
                    Dude. You are either a looser or you can't spell. (I can't spell, but I'm not the one stuck in a flooding house...) Put the right thing in this time.""")
                
    return room1

def room2():
    print("room2") 
    return "room2"

def room3():
    print("room3")
    return "room3"

def room4():
    print("room4")
    return "room4"

def room5():
    print("room5")
    return "room5"

def dead():
    print("You died. You are dead.")
    return "dead"


#Alexia, Main Game Loop
while True:
    while True:
        if position == "1":
            position = room1(incorrect, position)
        elif position == "2":
            position = room2()
        elif position == "3":
            position = room3()
        elif position == "4":
            position = room4()
        elif position == "5":
            position = room5()
        elif position == "7":
            position = dead()

        else:
            break

        if outside == 1:
            print("""
                You got outside. Nice. Work on your people skills, because I don't want to help you with this. AGAIN. But then again, knowing you I will have too. ugh.""")
            replay = input("""
                        Welp. Might as well get it over with now. If you insist on getting locked up again say so now. (Put: I   for 'I Insist on making bad life choices'   or: N   for 'Nah I'll be smart': )""").strip().lower()
            if replay == "i":
                win += 1
                moves = 0
                outside = 0
                word = random.choice(words)
                # varaible for  wrong guesses
                incorrect = 0
                # varable for guessed letters
                guessed = []
            elif replay == "n":
                print("A smart choice, yay. Hopeful I won't see you around!")
                win += 1
                with open("win_loss.txt", "w") as file:
                    file.write(f"{win},{loss}")
                    print(f"Wins: {win}, Losses : {loss}.")
                break

        if position == 7:
            print("You died. You are dead. Get it now? You had 'dangerous enimies' so you died. Make better choices. Well. I can give you another shot...")
            replay = input("""
                        Welp. Might as well get it over with now. If you insist on getting locked up again say so now. (Put: I   for 'I Insist on making bad life choices'   or: N   for 'Nah I'll be smart': )""").strip().lower()
            if replay == "i":
                loss += 1
                moves = 0
                outside = 0
                word = random.choice(words)
                # varaible for  wrong guesses
                incorrect = 0
                # varable for guessed letters
                guessed = []
            elif replay == "n":
                print("A smart choice finally. yay. Hopeful I won't see you around!")
                loss += 1
                with open("win_loss.txt", "w") as file:
                    file.write(f"{win},{loss}")
                    print(f"Wins: {win}, Losses : {loss}.")
                break
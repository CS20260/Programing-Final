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
def room_one(incorrect, position):
    # while true loop for lock
    while True:
        lock = input("""
                     It's Dark. You can't see well. ('cuz it's dark...) You are in the basement, and water is pooling around you ankles. You notice there is a locked door with a lock on it. (WOW! So smart!) Do you sit and accept your fate, or look at the lock? (say SIT or LOOK.)  """).strip().lower()
        if lock == "sit":
            print("You accepted your fate. You drowned. Imagine...")
            break
        elif lock == "look":
            print("""You look at the lock. Its a password code thing. Sence you didn't give up, you are going to at least pretend to open the lock. (Yes I'm making you do this. You're welcome!)""")
            ### CODE FOR GUESSING GAME ###
            #### mini game loop (while true) 
            display(word,guessed)
            while True:
                #make the display print thing work (make it simplier)
                current_display = display(word,guessed)
                if guessed == 0:
                    print(current_display)
                # create variable (ask user to guess letter)
                user = input("Guess a letter: ").strip().lower()
                # make a space to make it look better 
                print("""


            """)
                # add letter to list of guessed letters
                if current_display == word:
                    # tell user they won
                    print("You finaly got it.")
                    print("""
                    The door swings open. The water is now chest-deep and rising fast. You go out the open door and up some stairs.""")
                    locked == 1
                if user in guessed:
                    print("""You guessed this already...
                    
                    
                    """)
                    continue
                guessed.append(user)
                # check "if not letter in word:"
                if user not in word:
                    print("Wrong!")
                    # increase incorrect guesses
                    incorrect += 1
                    
                # recheck if display word is same as word (call function)
                current_display = (display(word,guessed))
                # print function to show display word
                print(current_display)
                if current_display == word:
                    # tell user they won
                    print("You finaly got it.")
                    print("""
                    The door swings open. The water is now chest-deep and rising fast. You go out the open door and up some stairs.""")
                    locked = 1
                #check if they lost (6 wrong guesses)
                if incorrect == 6:
                    print(f"The code was {word}.")
                    print("You didn't get it in time. You are dead.")
        elif locked == 1:
            position = 2

        else:
            print("""
                  Dude. You are either a looser or you can't spell. (I can't spell, but I'm not the one stuck in a flooding house...) Put the right thing in this time.""")
            
        


#Alexia, Main Game Loop
while True:
    while True:
        if position == 1:
            room_one(incorrect, position)
        elif position == 2:
            #living_room()
            print("you in da living room")
        elif position == 3:
            #room_three()
            print("you in da kithen ")
        elif position == 4:
            #upstaris()
            print("you are in the attic")
        elif position == 5:
            #rooftop()
            print("You are on the roof")
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
                loss += 1
                with open("win_loss.txt", "w") as file:
                    file.write(f"{win},{loss}")
                    print(f"Wins: {win}, Losses : {loss}.")
                break
# AB, AB, NBP, Final Build a Game
#### Alexia Variables ####
#start info
import random

inventory = []
# only 4 moves allowed!
words = ["cat","hat","leave","looser","unwanted","imagine","password"]
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
position = "room1"



#### Alexia (Minigame stuff) ####
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

#### Alexia (Minigame stuff) ####
def mini_game(display, position,incorrect, moves):
    while True:
                        display(word,guessed)
                        # creat variable (ask user to guess letter)
                # creat variable (ask user to guess letter)
                        letter = input("Guess ONE letter: ").strip().lower()
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
                                The door swings open. The water is now chest-deep and rising fast. You go out the open door and there are some stairs.""")
                            moves = moves + 1
                            return "room2"
                            break
                            #check if they lost (6 wrong guesses)
                        if incorrect == 6:
                            print(f"The code was {word}.")
                            return "room7"
                            break



#### Alexia (Starting stuff) ####
print("Hello! You are trapped in a house that is flooding. To survive, you must escape the house. Because the house is flooding, you have limited moves to escape. Good Luck!!!")


#### Alexia (function for room one or basement) ####

def room1(incorrect, position, moves):
    # while true loop for lock
    while True:
        lock = input("""
                        It's Dark. You can't see well. ('cuz it's dark...) You are in the basement, and water is pooling around you ankles. You notice there is a locked door with a lock on it. (WOW! So smart!) Do you sit and accept your fate, or look at the lock? (say SIT or LOOK.)  """).strip().lower()
            
        if lock == "sit":
            print("You accepted your fate. You drowned. Imagine...")
            return "room7"
            break
        elif lock == "look":
            print("""You look at the lock. Its a password code thing. Since you didn't give up, you are going to at least pretend to open the lock. (Yes I'm making you do this. You're welcome!)""")
            ### CODE FOR GUESSING GAME ###
            #### mini game loop (while true) 
            mini_game(display, position,incorrect, moves)


            move = input("Do you leave(1) or stay(2)?: ").strip()
            if move == "1":
                print("You go up the stairs")
                moves = moves + 1
                return "room2"
            elif move == "2":
                print("You stay. Unwisely.")
                return "room7"
        else:
            print("""
                Dude. You are either a looser or you can't spell. (I can't spell, but I'm not the one stuck in a flooding house...) Put the right thing in this time.""")
                
    return room1



#### Alexia (If you die...(function)) ####
def room7(position, loss, moves, outside, word,incorrect, guessed):
    print("You died. You are dead. Get it now? You had 'dangerous enimies' so you died. You have to make better choices, because I can't fix your problems. Well. That's not true. But I won't. I guess CAN give you another shot at this...")
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
       




#Addison, Room 3 kitchen
def room3(moves, position):
    print("You stepped into the kitchen, where you faintly smell pizza sause. You see a door, but the door has a lock on it, preventing anyone from coming in. ")
    while True:
        door= input("The door to escape is locked, you began to panic a bit, would you like to break the door down. (yes or no) ").upper().strip()
        if door == "Yes":
            search= input("You tried to break down the door, but failed. Would you like to search the kitchen? (yes or no) ").upper().strip()
            if search == "Yes":
                print("You began to search everywhere, the cabnets, the stove, the fridge, all of it. You cannot find the key. ")
            elif search == "No":
                    print("You didn't really want to check it. ")
        elif door == "No":
            search2= input("You proceeded to not break the door. You then thought to go back to the living room, but you also thought to search the kitchen one more time. Would you like to, A, check upstairs, or B search kitchen. ").upper().strip()
            if search2 == "A":
                print("You decided to go to the upstairs. ")
                move = move + 1
                return "room2"
            elif search2 == "B":
                print("You decided to check the kitchen, but you cannot find it again. ")
    else: 
        print("JUST ANSWER THE QUESTION!")





#nickolle, Room 2
# if they decide to go to the living room.
def room2(moves, position, inventory):
    action= input("You are now in the living room. Would you like to go to the kitchen, upstairs, or would you like to search the room? (say search or upstairs or kitchen)")
    while True:
        if action == "search":
            print("You have decided to search the room. You found a key! You now have a key.")
            inventory= inventory+"Key"
        elif action == "kitchen":
            print("you decided to go to the kitchen")
            moves = moves+ 1
            return "room3"
        elif action == ("upstairs"):
            print ("you decided to go upstairs")
            return "room4"
        elif action == "search":
            print("you decide to search the room.You found a key. You now have a key.")
            inventory= inventory +"Key"
    else:
        print("I gave you three options can you pick one.. preferably now")





#nickolle, room 4 Upstairs 
#if they decide to go upstairs 
def room4(moves, position, inventory):
    while True:
        action2 = input("You are now in the upstairs. Would you like to go to the rooftop from the window?, or would you like to search the room? (say rooftop or search)")
        if action2 == "search":
            print("You now have decided to search the room. You found a crowbar! you now have a crowbar.")
            inventory = inventory + "crowbar"
        elif action2:
                if action2 == "rooftop":
                    print("you decided to go to the rooftop")
                    moves = moves + 1
                    return "room 5"
    else:
        print("Okay why arent you choosing any of the options. choose now.")
            


    



#Addison, room 5 Rooftop
#if they go to the rooftop
def room5(outside, position): # nickolle is doing this first part since addison is not here.
    while True:
        action3 = input("You are now in the rooftop would you like to jump off the roof or just sit? The house is flooding really bad. Hurry up. Think what your decision is going to be. Hurry up. (say SIT or JUMP ) ")
        if action3 == "SIT":
            print("You decided to sit in your misery. you lasted 2 days, starved and died. :) ")
            #Addison starts here.
        else:
            if action3 == "JUMP":
                print("You stood back untill you reach the end of the back of the roof, you realized that there was a trampoline in the backyard, you then jumped off the roof, trying to land on the trampoline. ")
            jump = random.randint(1-11)
        while True:
            if jump < 5:
                print("You jumped, then missed the trampoline, you tragically died from the fall. ")
            else:
                print("You managed to jump on the trampoline to safty. Congrats, you were able to survive. ")
                outside += 1
    
    

    


  #### Alexia, Main Game Loop ####
while True:
    while True:# they are all gonna need position at some point...
        if position == "room1":
            position = room1(incorrect, position, moves)
        elif position == "room2":
            position = room2(position, moves, inventory)
        elif position == "room3":
            position = room3(position, moves)
        elif position == "room4":
            position = room4(moves, position, inventory)
        elif position == "room5":
            position = room5(outside, position)
        elif position == "room7":
            position = room7(position, loss, moves, outside, word,incorrect, guessed)
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
        if moves > 4:
            position == 7 #### Might be wrong....
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
    

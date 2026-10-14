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
    out = ""
    #loop over the correct word (look at every letter)
    for letter in word:
        # check if letter had been guessed
        if letter in guessed:
            # then add the letter to display word
            out += letter
            
        # if they havent guessed letter
        else:
            #add underscore to display word
            out += "-"


    return out
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
                            moves += 1
                            return "room2", display, position,incorrect, moves
                            
                            #check if they lost (6 wrong guesses)
                        if incorrect == 6:
                            print(f"The code was {word}.")
                            return "room7", display, position,incorrect, moves
                            



#### Alexia (Starting stuff) ####
print("Hello! You are trapped in a house that is flooding. To survive, you must escape the house. Because the house is flooding, you have limited moves to escape. Good Luck!!!")


#### Alexia (function for room one or basement) ####

def room1(incorrect, moves, position):
    # while true loop for lock
        while True:
            lock = input("""
                            It's Dark. You can't see well. ('cuz it's dark...) You are in the basement, and water is pooling around you ankles. You notice there is a locked door with a lock on it. (WOW! So smart!) Do you sit and accept your fate, or look at the lock? (say SIT or LOOK.)  """).strip().lower()
            
            if lock == "sit":
                print("You accepted your fate. You drowned. Imagine...")
                return "room7", moves, incorrect
                
            elif lock == "look":
                print("""You look at the lock. Its a password code thing. Since you didn't give up, you are going to at least pretend to open the lock. (Yes I'm making you do this. You're welcome!)""")
                    ### CODE FOR GUESSING GAME ###
                    #### mini game loop (while true) 
                mini_game(display, position,incorrect, moves)

                while True:
                    move = input("Do you leave(1) or stay(2)?: ").strip()
                    if move == "1":
                        print("You go up the stairs")
                        moves += 1
                        return "room2", moves, incorrect
                    elif move == "2":
                        print("You stay. Unwisely.")
                        return "room7", moves, incorrect
                    else:
                        print("""
                            Dude. You are either a looser or you can't spell. (I can't spell, but I'm not the one stuck in a flooding house...) Put the right thing in this time.""")
        
    



#### Alexia (If you die...(function)) ####
def room7(moves, position, incorrect, loss, outside, word, guessed, win):
    print("You died. You are dead. Get it now? You had 'dangerous enimies' so you died. You have to make better choices, because I can't fix your problems. Well. That's not true. But I won't. I guess CAN give you another shot at this...")
    replay = input("""
                        Welp. Might as well get it over with now. If you insist on getting locked up again say so now. (Put: I   for 'I Insist on making bad life choices'   or: N   for 'Nah I'll be smart': )""").strip().lower()
    while True:
        if replay == "i":
            loss += 1
            moves = 0
            outside = 0
            word = random.choice(words)
            # varaible for  wrong guesses
            incorrect = 0
            # varable for guessed letters
            guessed = []
            print("Don't mess up this time!")
            return position, moves, incorrect, loss, outside, word, guessed, win
        elif replay == "n":
            print("A smart choice finally. yay. Hopeful I won't see you around!")
            loss += 1
            with open("win_loss.txt", "w") as file:
                file.write(f"{win},{loss}")
                print(f"Wins: {win}, Losses : {loss}.")
                break
        else:
            print("Not a option. Pick 'I' or 'N' ")




#Addison, Room 3 kitchen
def room3(moves, position, inventory, outside):
    print("You stepped into the kitchen, where you faintly smell pizza sause. You see a door, but the door has a lock on it, preventing anyone from coming or going. ")
    while True:
        door= input("The door to escape is locked, you began to panic a bit, would you like to break the door down(1) or unlock the door(2). ").lower().strip()
        if door == "1":
            search= input("""
                          You tried to break down the door, but failed. Would you like to search the kitchen? """).lower().strip()
            if search == "yes":
                print("You began to search everywhere, the cabnets, the stove, the fridge, all of it. You cannot find the key. ")
                leave = input("""
                              Would you like to go back to the living room?""").lower().strip()
                if leave == "yes":
                    print("You go to the living room")
                    moves += 1
                    return "room2",  moves, position, inventory, outside
                elif leave == "no":
                    print("You stay. ")
                    return "room7",  moves, position, inventory, outside
            elif search == "No":
                print("You didn't really want to check it. ")
                leave = input("""
                              Would you like to go back to the living room?""").lower().strip()
                if leave == "yes":
                    print("You go to the living room")
                    moves += 1
                    return "room2", moves, position, inventory, outside
                elif leave == "no":
                    print("You stay. ")
                    return "room7", moves, position, inventory, outside
        elif door == "2":
            print("You try to open the door.")
            if "key" in inventory :
                print(" you use the key you had to unlock the door.")
                outside += 1
                moves += 1
                return moves, position, inventory, outside
            else:
                print("You couldn't unlock the door.")
                search2= input("You then thought to go back to the living room, but you also thought to search the kitchen one more time. Would you like to, A, Go to the living room, or B search kitchen. ").lower().strip()
                if search2 == "A":
                    print("You decided to go to the living room. ")
                    moves += 1
                    return "room2", moves, position, inventory, outside
                elif search2 == "B":
                    print("You decided to check the kitchen, but you cannot find it again. ")
                    leave = input("""
                                Would you like to go back to the living room?""").lower().strip()
                    if leave == "yes":
                        print("You go to the living room")
                        moves += 1
                        return "room2", moves, position, inventory, outside
                    elif leave == "no":
                        print("You stay. ")
                        return "room7", moves, position, inventory, outside
           
        else: 
            print("JUST ANSWER THE QUESTION!")





#nickolle, Room 2
# if they decide to go to the living room.
def room2(moves, position, inventory):
    while True:
        action= input("You are now in the living room. Would you like to go to the kitchen, upstairs, or would you like to search the room? (say search or upstairs or kitchen)").lower().strip()
        if action == "search":
            print("You have decided to search the room. You found a key! You now have a key.")
            inventory.append("key")
            print(f"Your inventory is: {inventory}.")
            while True:
                action_hidden= input("Would you like to go to the kitchen(1) or upstairs(2)")
                if action_hidden == "1":
                    print("you decided to go to the kitchen")
                    moves += 1
                    return "room3", position, inventory
                elif action_hidden == "2":
                    print("you decided to go upstairs")
                    moves += 1
                    return "room4", position, inventory
                else:
                    print("It's 1 or 2. Not that hard")
        elif action == "kitchen":
            print("you decided to go to the kitchen")
            moves += 1
            return "room3", position, inventory
        elif action == "upstairs":
            print("you decided to go upstairs")
            moves += 1
            return "room4", position, inventory
        
        else:
            print("I gave you three options can you pick one.. preferably now")





#nickolle, room 4 Upstairs 
#if they decide to go upstairs 
def room4(moves, position, inventory):
    while True:
        action2 = input("You are now in the upstairs. Would you like to go to the rooftop from the window?, or would you like to search the room? (say rooftop or search)").lower().strip()
        if action2 == "search":
            print("You now have decided to search the room. You found a crowbar! you now have a crowbar.")
            inventory.append("crowbar")
            leave = input("""
                              Would you like to go back to the (1)living room, or (2)stay?""").lower().strip()
            if leave == "1":
                print("You go to the living room")
                moves += 1
                return "room2", moves, position, inventory
            elif leave == "2":
                print("You stay. ")
                while True:
                    escape = input("Would you like to go to the rooftop(1) or quit(2):  ")
                    if escape == "1":
                        if "crowbar" in inventory:
                            print("You have a crowbar, so you used to pry the window open to go to the rooftop")
                            moves += 1
                            return "room 5", moves, position, inventory
                        else:
                            print("You are weak and can't open the window.")
                    elif escape == "2":
                        print("You quit and drown.")
                        return "room7", moves, position, inventory
                    else:
                        print("1 or 2. Just pick!")
                break
            else:
                print("Pick 1 or 2.")
        elif action2:
                if action2 == "rooftop":
                    if "crowbar" in inventory:
                        print("You have a crowbar, so you used to pry the window open to go to the rooftop")
                        moves += 1
                        return "room 5", moves, position, inventory
                    else:
                        print("You are weak and can't open the window.")
        else:
            print("Okay why arent you choosing any of the options. Choose now.")
            


    



#Addison, room 5 Rooftop
#if they go to the rooftop
def room5(outside, position, moves, incorrect, inventory): # nickolle is doing this first part since addison is not here.
    while True:
        action3 = input("You are now in the rooftop would you like to jump off the roof or just sit? The house is flooding really bad. Hurry up. Think what your decision is going to be. Hurry up. (say SIT or JUMP ) ").upper().strip()
        if action3 == "SIT":
            print("You decided to sit in your misery. you lasted 2 days, starved and died. :) ")
            #Addison starts here.:
        elif action3 == "JUMP":
                print("You stood back untill you reach the end of the back of the roof, you realized that there was a trampoline in the backyard, you then jumped off the roof, trying to land on the trampoline. ")
                jump = random.randint(1,10)
                while True:
                    if jump < 5:
                        print("You jumped, then missed the trampoline, you tragically died from the fall. ")
                        return "room7", outside, moves, incorrect, inventory
                    else:
                        print("You managed to jump on the trampoline to safty. Congrats, you were able to survive. ")
                        outside += 1
                        return "room5", outside, moves, incorrect, inventory
        else:
            print("Don't be a hero. Answer the question.")
    

    


  #### Alexia, Main Game Loop ####
while True:
    if moves > 4:
        print("You took to long to get out of the house, and drowned.")
        position = "room7" 

   
    if position == "room1":
        position, moves, incorrect   = room1(incorrect, moves, position)
        

    elif position == "room2":
         position, place_holder, inventory = room2(moves, position, inventory)

    elif position == "room3":
        position, moves, inventory, outside = room3(moves, position, inventory, outside)

    elif position == "room4":
         position, moves, place_holder, inventory = room4(moves, position, inventory)

    elif position == "room5":
         position, outside, moves, incorrect, inventory = room5(outside, position, moves, incorrect, inventory)

    elif position == "room7":
         position, moves, incorrect, loss, outside, word, guessed, win = room7(moves, position, incorrect, loss, outside, word, guessed, win)


    if outside == 1:
            print("""
                You got outside. Nice. Work on your people skills, because I don't want to help you with this. AGAIN. But then again, knowing you I will have too. ugh.""")
            while True:
                win += 1
                with open("win_loss.txt", "w") as file:
                    file.write(f"{win},{loss}")
                    print(f"Wins: {win}, Losses : {loss}.")
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
                    inventory = []
                    position = "room1"
                    print("Well. Don't be as slow this time.")
                    break
                elif replay == "n":
                    print("A smart choice, yay. Hopeful I won't see you around!")
                    break
                else:
                    print("Put in 'I' or 'N'")
        
    elif position == 7:
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
            position = "room1"
        elif replay == "n":
            print("A smart choice finally. yay. Hopeful I won't see you around!")
            loss += 1
            with open("win_loss.txt", "w") as file:
                file.write(f"{win},{loss}")
                print(f"Wins: {win}, Losses : {loss}.")
                break
    elif position not in ["room1","room2","room3","room4","room5","room7"]:
        print("Yo, you got lost. see ya.")
        break
    
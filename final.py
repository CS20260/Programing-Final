# AB, TG, AB, NB, Final Build a Game

print("Start")

#ctrl alt f => stop following people

inventory = []
# only 7 moves allowed!
moves = 0
outside = 0
# read files
with open("words.txt","r") as file:
    words= file.read().split(",")
with open("win_loss.txt", "r")as file:
    win_loss = file.read().strip().split(",")
#use split(",") on content of the words txt doc to create list of words
#turn win loss into an integer so that we can concatinate
# pull win and loose totals from other txt file and save them as 2 seperate variables
win = int(win_loss[0])
loss = int(win_loss[1])


# Alexia, Start room and Plot
#start info
print("Hello! You are trapped in a house that is flooding. To survive, you must escape the house. Because the house is flooding, you have limited moves to escape. Good Luck!!!")
#function for room one or basement
def room_one():
    # while true loop for lock
    while True:
        lock = input("It's Dark. You can't see well. ('cuz it's dark...) You are in the basement, and water is pooling around you ankles. You notice there is a locked door with a lock on it. (WOW! So smart!) Do you sit and accept your fate, or look at the lock? (say SIT or LOOK.)").strip().lower()
        if lock == "sit":
            print("You acepted your fate. You drowned. Imagine...")
            break
        elif lock == "look":
            print("You look at the lock. Its a password code thing. Sence you didn't give up, you are going to at least pretend to open the lock")
            ### CODE FOR GUESSING GAME ###
            
        else:
            print("Dude. You are either a looser or you can't spell. (I can't spell, but I'm not the one stuck in a flooding house...)")










#Addison, Room 3 
print("You have entered the kitchen")
def room_three():
    print("You stepped into the kitchen, where you faintly smell pizza sause. You turned your head and saw the backdoor locked, you then reaslize that door is your only ticket out of the house. You then relize you have to find the key to escape the house.")
    while True:
        door= input("The door to escape is locked, you began to panic a bit, would you like to break the door down. ")
        if door == "Yes":
            print("You tried to break down the door, but failed. Would you like to search the kitchen? ")
            search= input
            if search == "Yes":
                print("You began to search everywhere, the cabnets, the stove, the fridge, of of it. You cannot find the key. ")
                if search == "No":
                    print("You didn't really wanted to check it. ")
        else:
            door == "No"
            print("You proceeded to not break the door, as you saved your move. You then thought to check up the stairs, but you also thought to searched the kitchen one more time. Would you like to, A, check upstairs, or B ")





#nickolle, Room 2
# if they decide to go to the living room.
def living_room():
    action= input("You are now in the living room. Would you like to go to the kitchen, upstairs, or would you like to search the room? (say search or upstairs or kitchen)")
    if action == "search":
        print("You have decided to search the room. You found a key! You now have a key.")
        inventory= inventory+"Key"
    elif action == "upstairs":

    elif action == "kitchen":




#nickolle, room 4 Upstairs 
#if they decide to go upstairs 
def upstairs():
    action2 = input("You are now in the upstairs. Would you like to go to the rooftop from the window?, or would you like to search the room? (say rooftop or search)")
    if action2 == "rooftop":
        print("You decided to go to the rooftop. Looks like the window in the livingroom is too hard to open with just your hands.")
    if action2 == "Search":
        print("You now have decided to search the room. You found a crowbar! you now have a crowbar.")
        inventory = inventory + "crowbar"



#Addison, room 5 Rooftop
#if they go to the rooftop
def rooftop(): # nickolle is doing this next part since addison is not here.
    action3 = input("You are now in the rooftop would you like to jump off the roof or just sit? The building if flooding really bad. Hurry up. Think what your decision is going to be. Hurry up. (say SIT or JUMP ) ")
    if action3 == "SIT"
    print("You decided to sit in your misery. you lasted 2 days starved and died. :) ")
    
    

    


  
    
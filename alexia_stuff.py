# Alexia, Start Room and Plot
#start info
print("Hello! You are trapped in a house that is flooding. To survive, you must escape the house. Because the house is flooding, you have limited moves to escape. Good Luck!!!")
#function for room one or basement
def room_one():
    # while true loop for lock
    while True:
        lock = input("It's Dark. You can't see well. ('cuz it's dark...) You are in the basement, and water is pooling around you ankles. You notice there is a locked door with a lock on it. (WOW! So smart!) Do you sit and accept your fate, or look at the lock? (say SIT or LOOK.)").strip().lower()
        if lock == "sit":
            print("You accepted your fate. You drowned. Imagine...")
            break
        elif lock == "look":
            print("You look at the lock. Its a password code thing. Sence you didn't give up, you are going to at least pretend to open the lock. (Yes I'm making you do this. You're welcome!)")
            ### CODE FOR GUESSING GAME ###
            
        else:
            print("Dude. You are either a looser or you can't spell. (I can't spell, but I'm not the one stuck in a flooding house...)")


#Alexia, Main Game Loop
while True:
    if outside == 1:
        print("You got outside. Nice. Work on your people skills, because I don't want to help you with this. AGAIN. But then again, knowing you I will have too. ugh.")
        replay = input("Welp. Might as well get it over with now. If you insist on getting locked up again say so now. (I for Insist or N for Nah I'll be smart)").strip().lower()
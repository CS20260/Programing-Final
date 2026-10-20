#AB fixed ticket code

while True:
    try:
        age = int(input("Enter your age: "))
    except:
            print("Invalid age.")
            break
    else:    
        if age < 5:
            price = 0
        elif age <= 12:
            price = 8
        elif age < 65:
            price = 12
        else:
            print("Invalid age.")
            break
        
        matinee = input("Is this a matinee? (yes/no): ").lower().strip()
        if matinee == "yes":
            if age > 5:
                price = price - 3
            print(f"Ticket price: ${price:.2f}")
        elif matinee == "no":
                print(f"Ticket price: ${price:.2f}")
        else:
            print("Invalid input. Please enter a matinee input of 'yes' or 'no'.")
        
       
        
        
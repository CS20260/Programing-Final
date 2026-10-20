while True:
    try:
        income = float(input("What is your monthly income? : "))
        break
    except:
        print("In numbers please...")

# while true loop

while True:
    try:
        rent = float(input("What is your monthly rent/mortgage? : "))
        break
    except:
        print("In numbers please...")

# while true loop

while True:
    try:
        utilities = float(input("What is the cost of your monthly utilities? : "))
        break
    except:
        print("In numbers please...")

# while true loop

while True:
    try:
        groceries = float(input("What is the cost of your monthly groceries? : "))
        break
    except:
        print("In numbers please...")

# while true loop

while True:
    try:
        transportation = float(input("What is the cost of your monthly transportation? : "))
        break
    except:
        print("In numbers please...")

# saving precent
savings = income*0.1

# Equality for precent
prent = rent/income*100

# Equality for precent
putilities = utilities/income*100

# Equality for precent
pgroceries = groceries/income*100

# Equality for precent
ptransportation = transportation/income*100

# equality for present


# print statements
print(f"Your rent is ${rent} and that is int({prent})% of your income.")

# print statements
print(f"Your utilities are ${utilities} and that is {putilities:.2f}% of your income.")

# print statements
print(f"Your groceries are ${groceries} and that is {pgroceries:.2f}% of your income.")

# print statements
print(f"Your transportation is ${transportation} and that is {ptransportation:.2f}% of your income.")

# print statements
print(f"Your savings are ${savings} and that is 10% of your income.")

# spending
spending = income-rent-utilities-groceries-transportation-savings

#total cost
total = income-spending

#print total and spending amount left
print(f"Your total base cost will be ${total}, and your amount left to spend is {spending}!")
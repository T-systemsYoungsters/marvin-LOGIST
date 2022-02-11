from operator import truediv
import random
from re import X
x = ''
#1.
print ("Welcome to Camel!")
print ("You have stolen a camel to make your way across the great Mobi desert.")
print ("The natives want their camel back and are chasing you down! Survive your")
print ("desert trek and out run the natives.")
print(x)

#2.
done = False

#8.
miles_traveled = 0
thirst = 0
camel_tiredness = 0

#9.
natives_distance = 20 #Änderung damit die Angabe im print nicht in negativen Zahlen ist

#10.
drinks_canteen = 5
#3.
while not done:
    #4.
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    print(x)
    
    #5.     
    user_choice = input("Your choice?: ")
    print ('')

    #6.
    if user_choice.upper() == "Q":
        done = True
    
    #11.
    elif user_choice.upper() == 'E':   
        print("Miles traveled:", miles_traveled)
        print("Drinks in canteen:", drinks_canteen)
        print(f"The natives are {natives_distance} miles behind you.")
        print(x)

    #12.
    elif user_choice.upper() == 'D':
        camel_tiredness = 0
        print("Camel is happy")
        print(x)
        natives_distance -= random.randrange(7,15)
    
    #13.
    elif user_choice.upper() == 'C':
        miles_traveled += random.randrange(10,21)
        thirst += 1
        camel_tiredness += random.randrange(1,3)
        natives_distance += random.randrange(7,15)
        print(f"You traveled {miles_traveled} so far")
        print(x)

    #14.
    elif user_choice.upper() == 'B':
        miles_traveled += random.randrange(5,13)
        print(f"You traveled {miles_traveled} so far")
        print(x)
        thirst += 1
        camel_tiredness += 1
        natives_distance -= random.randrange(7,15)
    #15.
    elif user_choice.upper() == 'A':
        if drinks_canteen > 0:
            drinks_canteen -= 1
            thirst = 0
        else:
            print("Error. You have nothing to drink left.")
            print(x)
        print("Canteens left: ", drinks_canteen)   
        print(x)

    #16.
    if thirst in range(5,7):
        print("You are thirsty.")
        print(x)

    #17.
    if thirst > 6:
        print("You died of thirst!")
        print(x)
        done = True
    
    #18.
    if camel_tiredness in range(6,9):
        print("Your camel is getting tired.")
        print(x)
    
    #19.
    if camel_tiredness > 8:
        print("Your camel is dead.")
        print(x)
        done = True
    
    #20.
    if natives_distance <= 0:
        print("The natives caught up. You are dead.")
        done = True
    
    #21.
    if natives_distance in range (1,15):
        print("The natives are getting close!")
        print(x)
    
    #22.
    if miles_traveled > 200 and natives_distance >= 0 and thirst <= 6 and camel_tiredness <= 8 :
        print("You won!")
        done = True
    
    #23.
    oasis_chance = random.randrange(1,20)
    if oasis_chance == 7 and done == False :
        drinks_canteen = 7
        thirst = 0
        camel_tiredness = 0
        print("You have found an oasis! You are reseting")
        print(x)

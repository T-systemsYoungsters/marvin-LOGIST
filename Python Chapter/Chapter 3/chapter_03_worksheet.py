# 1.
temperature = float(input("Temperature: "))
if temperature > 90:
    print("It is hot outside.")
else:
    print("It is not hot out.")

# 2.
number = float(input("Bitte Nummer eingeben: "))
if number > 0:
    print("Deine Zahl ist positiv")
elif number < 0:
    print ("Deine Zahl ist negativ")
else:
    print("Deine Zahl ist 0")

# 3.
number = float(input("Bitte Nummer eingeben: "))
if number >= -10 and number <= 10:
    print("Sucess")
else:
    print()

# 5.
x = 4
if x > 0:
    print("x is positive.")
elif x < 0:
    print("x is not positive.")
else:
    print("x is not positive or negative.")

# 6.
x = int(input("Enter a number: "))
if x == 3:
    print("You entered 3")

# 7.
answer = input("What is the name of Dr. Bunsen Honeydew's assistant? ")
if answer == "Beaker":
    print("Correct!")
else:
    print("Incorrect! It is Beaker.")

# 8.
x = input("How are you today?")
if x == "Happy" or x == "Glad":
    print("That is good to hear!")

# 9.
x = 5
y = x == 6
z = x == 5
print("x=", x)
print("y=", y)
print("z=", z)
if y:
    print("Fizz")
if z:
    print("Buzz")

# 10.
x = 5
y = 10
z = 10
print(x < y)
print(y < z)
print(x == 5)
print(not x == 5)
print(x != 5)
print(not x != 5)
print(x == "5")
print(5 == x + 0.00000000001)
print(x == 5 and y == 10)
print(x == 5 and y == 5)
print(x == 5 or y == 5)

# 11.
print("3" == "3")
print(" 3" == "3")
print(3 < 4)
print(3 < 10)
print("3" < "4")
print("3" < "10")
print( (2 == 2) == "True" )
print( (2 == 2) == True )
print(3 < "3")

# 12. 
print("Welcome to Oregon Trail!")
 
print("A. Banker")
print("B. Carpenter")
print("C. Farmer")
 
A = 'Banker'
B = 'Carpenter'
C = 'Farmer'
money = 0

user_input = input("What is your occupation? ")
 
if user_input == A:
    money = money + 100
elif user_input == B:
    money = money + 70
elif user_input == C:
    money = money + 50
 
print("Great! you will start the game with", money, "dollars.")

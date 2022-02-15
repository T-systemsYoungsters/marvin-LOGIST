#1
for i in range (10):
    print ("Marvin")
print ("Done")

#2
for i in range (20):
    print ("Red")
    print ("Gold")

#3
c = 1
for i in range (99):
    c = c + 1
    print (c)

#4
i = 10
while i >= 0:
    print(i)
    i = i - 1
print("Blast off!")

#5
print("This program takes three numbers and returns the sum.")
total = 0
 
for i in range(3):
    x = input("Enter a number: ") #Der Input hat einen string als Datentyp, es muss ein int sein
    total = total + i #falsche Variable, dort muss das x stehen
print("The total is:", x) #x ist unser input, dort muss "total" stehen

#6
import random
my_number = random.randrange(1,11)
print(my_number)

#7
import random
my_number = random.random() * 9 + 1
print(my_number)    

#8
total = 0  
positiveTotal = 0
negativeTotal = 0
zeroTotal = 0

for i in range(7):
    x = int(input("Enter a number: "))
    total += x
    if x > 0:
        positiveTotal += 1
    elif x < 0:
        negativeTotal += 1
    elif x == 0:
        zeroTotal += 1
   
print("The total is:", total) 
print("The total of positive numbers: ", positiveTotal)
print("The total of negative numbers: ", negativeTotal)
print("The total of zeros: ", zeroTotal)

#9
import random
heads = 0
tails = 0
for x in range(50):
    my_number = random.randrange(2)
    if my_number == 1:
        heads += 1
        print ("heads")
    else:
        tails += 1
        print ("tails")
print ("The total of heads is:", heads)
print ("The total of tails is:", tails)

#10
import random
print ("Willkommen zu Schere-Stein-Papier")
print ("Gebe deine Wahl zu erst ein um dann zusehen was der Computer geommen hat")
print ("Bitte gebe zur Vereinfachung Zahlen an\n1 = Schere\n2 = Stein\n3 = Papier")
user_pick = int(input("Gebe deine Wahl ein: "))
pc_pick = random.randrange(1,4)

#tie
if pc_pick == user_pick:
    if user_pick == 1:
        print ("Gleichstand! Der Computer hat auch Schere genommen")
    elif user_pick == 2:
        print ("Gleichstand! Der Computer hat auch Stein genommen")
    elif user_pick == 3:
        print ("Gleichstand! Der Computer hat auch Papier genommen")
#win
elif user_pick == 1 and pc_pick == 3:
    print ("Der Computer hat Papier genommen.\nDu hast gewonnen! Schere schneidet Papier")
elif user_pick == 2 and pc_pick == 1:
    print ("Der Computer hat Schere genommen.\nDu hast gewonnen! Stein zerstört Schere")
elif user_pick == 3 and pc_pick == 2:
    print ("Der Computer hat Stein genommen.\nDu hast gewonnen! Papier bedeckt Stein")
#lose
elif user_pick == 1 and pc_pick == 2:
    print ("Der Computer hat Stein genommen.\nDu hast verloren! Stein zerstört Schere")
elif user_pick == 2 and pc_pick == 3:
    print ("Der Computer hat Papier genommen.\nDu hast verloren! Papier bedeckt Stein")
elif user_pick == 3 and pc_pick == 1:
    print ("Der Computer hat Schere genommen.\nDu hast verloren! Schere schneidet Papier")

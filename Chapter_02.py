print("QUIZ TIME!")
print ("Was ist 1+1?")
true = ("Antwort ist richtig")
false = ("Antwort ist falsch")
a = 0
b = 0
c = 0
d = 0
e = 0
count = 0
a = int(input("Bitte Anwort eingeben: "))
if a == 2:
    print(true)
    count = count + 1
else:
    print(false)

print()

print("Wieviele Punkte hat das Telekom Logo")
print("1. 1\n2. 2\n3. 3\n4. 4")
b = int(input("Bitte Antwort eingeben: "))
if b == 4:
    print(true)
    count = count + 1
else:
    print(false)

print()

print("Wieviele Ecken hat ein Oktaeder")
print("1. 3\n2. 6\n3. 8\n4. 4")
c = int(input("Bitte Antwort eingeben: "))
if c == 3:
    print(true)
    count = count + 1
else:
    print(false)

print()

print("Wie heißt die erste deutsche Bundeskanzlerin?")
print("1. Angelo\n2. Frauke Petri\n3. Claudia Roth\n4. Angela Merkel")
d = int(input("Bitte Antwort eingeben: "))
if d == 4:
    print(true)
    count = count + 1
else:
    print(false)

print()

print("Wieviel sind 50 Prozent von 100?")
e = int(input("Bitte Antwort eingeben: "))
if e == 50:
    print(true)
    count = count + 1
else:
    print(false)

count_percent = (count /5) * 100 

print("Herzlichen Glückwunsch, du hast", count,"Fragen richtig")
print("Das entspricht", count_percent,"Prozent")

print("QUIZ TIME!")

true = ("\033[32m" + "Deine Antwort ist richtig!")
false = ("\033[31m" + "Deine Antwort ist leider falsch.")
a = 0
b = 0
c = 0
d = 0
e = 0
count = 0

print ("Was ist 1+1?")
print()
a = int(input("Bitte Anwort eingeben: "))
if a == 2:
    print(true)
    count = count + 1
else:
    print(false)

print("\033[0m")

print("Wie heißt der Vorstandsvositzende der Deustchen Telekom?")
print("1. Timotheus Höttges\n2. Adel Al-Saleh\n3. Srini Gopalan\n4. Thorsten Langheim")
print()
b = int(input("Bitte Antwort eingeben: "))
if b == 1 :
    print(true)
    count = count + 1
else:
    print(false)

print("\033[0m")

print("Wieviele Ecken hat ein Oktaeder?")
print()
c = int(input("Bitte Antwort eingeben: "))
if c == 8:
    print(true)
    count = count + 1
else:
    print(false)

print("\033[0m")

print("Wie heißt die erste deutsche Bundeskanzlerin?")
print("1. Angelo\n2. Frauke Petri\n3. Claudia Roth\n4. Angela Merkel")
print()
d = int(input("Bitte Antwort eingeben: "))
if d == 4:
    print(true)
    count = count + 1
else:
    print(false)

print("\033[0m")

print("Wieviel sind 50 Prozent von 100?")
print()
e = int(input("Bitte Antwort eingeben: "))
if e == 50:
    print(true)
    count = count + 1
else:
    print(false)

print("\033[0m")

count_percent = (count / 5) * 100 

if count == 1:
    print("Herzlichen Glückwunsch, du hast", count,"Frage richtig beantwortet!")
    print("Das entspricht", count_percent,"Prozent")
else:
    print("Herzlichen Glückwunsch, du hast", count,"Fragen richtig beantwortet!")
    print("Das entspricht", count_percent,"Prozent")

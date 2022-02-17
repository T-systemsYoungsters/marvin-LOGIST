# 1. What does this program print out? 
```
x = 0
while x < 10:
    print(x)
    x = x + 2
```
- Guess: 0 2 4 6 8 (vertical)
- Result: 0 2 4 6 8 (vertical)

# 2. What does this program print out?
```
x = 1
while x < 64:
    print(x)
    x = x * 2
```
- Guess: 1 2 4 8 16 32 (vertical)
- Result: 1 2 4 8 16 32 (vertical)

# 3. Why is the ``and x >= 0'' not needed?
```
x = 0
while x < 10 and x >= 0:
    print(x)
    x = x + 2
```
- x wird am Anfang auf 0 gesetzt, die Bedingung x>=0 ist also zu jederzeit erfüllt

# 4. What does this program print out?
```
x = 5
while x >= 0:
    print(x)
    if x == "1":
        print("Blast off!")
    x = x - 1
```
- Result: 5 4 3 2 1 0
- Der Wert der If Bedingung wurde als string und nicht als int angegeben, deshalb wird diese nie erfüllt

# 5. Fix the following code so it doesn't repeat forever, and keeps asking the user until he or she enters a number greater than zero:
```
x = float(input("Enter a number greater than zero: "))
 
while x <= 0:
    print("Too small. Enter a number greater than zero: ")
```
Fix:
```
x = float(input("Enter a number greater than zero: "))
done = False
while not done:
    if x <= 0:
        print("Too small. Enter a number greater than zero: ")
        x = float(input("Enter a number greater than zero: "))
    else:
        done = True
```

# 6. Fix the following code:
```
x = 10

while x < 0:
    print(x)
    x - 1
 
print("Blast-off")
```
Fix:
```
x = 10
while x >= 0:
    print(x)
    x = x - 1
 
print("Blast-off")
```

# 7. 
```
i = 0
for i in range(10):
    print(i)
    i += 1
```
Fix:
```
for i in range(10):
    print(i)
```
- i = 0 : unnötig, weil startwert ist standardmäßig 0
- i += 1: unnötig, weil schleife zählt standardmäßig den wert hoch

# 8. Explain why the values printed for x are so different.
```
# Sample 1
x = 0
for i in range(10):
    x += 1
for j in range(10):
    x += 1
print(x)
 
# Sample 2
x = 0
for i in range(10):
    x += 1
    for j in range(10):
        x += 1
print(x)
```
- Sample 1: x startwert = 0, die schleife addiert 10x die 1 auf den wert x und die zweite schleife tut das gleiche, vereinfacht:
```
for i in range(20):
    x += 1
```
- Sample 2: x startwert = 0, die schleifen multiplizieren sich
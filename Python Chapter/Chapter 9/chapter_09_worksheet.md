# 1. Block
```
for i in range(5):
    print(i + 1)
```
- Guess: 1 2 3 4 5 (vertical)
- Result: 1 2 3 4 5 (vertical)

# 2. Block
```
for i in range(5):
    print(i)
    i = i + 1
```
- Guess: 0 1 2 3 4 (vertical)
- Result: 0 1 2 3 4 (vertical)

# 3. Block
```
x = 0
for i in range(5):
    x += 1
print(x)
```
- Guess: 5
- Result: 5

# 4. Block
```
x = 0
for i in range(5):
    for j in range(5):
        x += 1
print(x)
```
- Guess: 25
- Result: 25

# 5. Block
```
for i in range(5):
    for j in range(5):
        print(i, j)
```
- Guess: 5 25 (vertical)
- Result: 0 0 0 1 0 2 0 3 0 4 1 0 1 1 1 2 1 3 1 4 2 0 2 1 2 2 2 3 2 4 3 0 3 1 3 2 3 3 3 4 4 0 4 1 4 2 4 3 4 4 (vertical)

# 6. Block
```
for i in range(5):
    for j in range(5):
        print("*", end="")
        print()
```
- Guess: * (x25 vertical)
- Result: * (x25 vertical)

# 7. Block
```
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()
```
- Guess: ***** (x5 vertical)
- Result: ***** (x5 vertical)

# 8. Block
```
for i in range(5):
    for j in range(5):
        print("*", end="")
print()
```
- Guess: *************************
- Result: *************************

# 9. Block
```
# This is supposed to sum a list of numbers
# What is the mistake here?
my_list = [5, 8, 10, 4, 5]
i = 0
for i in my_list:
    i = i + my_list[i]
print(i)
```
- Correct:
```
my_list = [5, 8, 10, 4, 5]
sum = 0
for i in range(len(my_list)):
    sum = sum + my_list[i]
print(sum)
```
- Guess: 32
- Result: 32

# 10. Block
```
for i in range(5):
    x = 0
    for j in range(5):
        x += 1
print(x)
```
- Guess: 5
- Result: 5

# 11. Block
```
import random
play_again = "y"
while play_again == "y":
    for i in range(5):
        print(random.randrange(2), end="")
    print()
    play_again = input("Play again? ")
print("Bye!")
```
- Guess: random 5 digit number from 0 to 1 and "Play again?"
- Result: random 5 digit number from 0 to 1 and "Play again?"

# 12. Block
```
def f1(x):
    print(x)
y = 3
f1(y)
```
- Guess: 3
- Result: 3

# 13. Block
```
def f2(x):
    x = x + 1
    print(x)
y = 3
f2(y)
print(y)
```
- Guess: 4 3 (vertical)
- Result: 4 3 (vertical)

# 14. Block
```
def f3(x):
    x = x + 1
    print(x)
x = 3
f3(x)
print(x)
```
- Guess: 4 3 (vertical)
- Result: 4 3 (vertical)

# 15. Block
```
def f4(x):
    z = x + 1
    print(z)
x = 3
f4(x)
print(z)
```
- Guess: 4 Error (vertical)
- Result: 4 Error (vertical)
- Error: 'z' is not defined

# 16. Block
```
def foo(x):
    x = x + 1
    print("x=", x)
 
x = 10
print("x=", x)
foo(x)
print("x=", x)
```
- Guess: x= 10 x= 11 x= 10 (vertical)
- Result: x= 10 x= 11 x= 10 (vertical)

# 17. Block
```
def f():
    print("f start")
    g()
    h()
    print("f end")
 
def g():
    print("g start")
    h()
    print("g end")
 
def h():
    print("h")
 
f()
```
- Guess: f start g start  h  g end  h  f end (vertical)
- Result: f start g start  h  g end  h  f end (vertical)

# 18. Block
```
def foo():
    x = 3
    print("foo has been called")
 
x = 10
print("x=", x)
foo()
print("x=", x)
```
- Guess: x= 10  foo has been called  x= 10 (verical)
- Result: x= 10  foo has been called  x= 10 (verical)

# 19. Block
```
def a(x):
    print("a", x)
    x = x + 1
    print("a", x)
 
x = 1
print("main", x)
a(x)
print("main", x)
 
def b(y):
    print("b", y[1])
    y[1] = y[1] + 1
    print("b", y[1])
 
y=[123, 5]
print("main", y[1])
b(y)
print("main", y[1])
 
def c(y):
    print("c", y[1])
    y = [101, 102]
    print("c", y[1])
 
y = [123, 5]
print("main", y[1])
c(y)
print("main", y[1])
```
- Guess: main 1  a 1  a 2  main 1  main 5  b 5  b 6  main 6  main 5  c 5  c 102  main 5 (vertical)
- Result: main 1  a 1  a 2  main 1  main 5  b 5  b 6  main 6  main 5  c 5  c 102  main 5 (vertical)

# Correting Code
# 1. Correct the following code: (Don't let it print out the word ``None'')
```
def sum(a, b, c):
    print(a + b + c)
 
print(sum(10, 11, 12))
```
- Correct:
```
def sum(a, b, c):
    print(a + b + c)

sum(10, 11, 12)
```

# 2. Correct the following code: (x should increase by one, but it doesn't.)
```
def increase(x):
    return x + 1
 
x = 10
print("X is", x, " I will now increase x." )
increase(x)
print("X is now", x)
```
- Correct:
```
def increase(x):
    return x + 1

x = 10
print("X is", x, " I will now increase x." )
x = increase(x)
print("X is now", x)
```

# 3. Correct the following code:
```
def print_hello:
    print("Hello")
 
print_hello()
```
- Correct: 
```
def print_hello():
    print("Hello")
 
print_hello()
```

# 4. Correct the following code:
```
def count_to_ten():
    for i in range[10]:
        print(i)
 
count_to_ten()
```
- Correct 0-9:
```
def count_to_ten():
    for i in range(10):
        print(i)
 
count_to_ten()
```
- Correct 1-10:
```
def count_to_ten():
    for i in range(1,11):
        print(i)
 
count_to_ten()
```

# 5. Correct the following code:
```
def sum_list(list):
    for i in list:
        sum = i
        return sum
 
list = [45, 2, 10, -5, 100]
print(sum_list(list))
```
- Correct: 
```
def sum_list(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    return sum
 
list = [45, 2, 10, -5, 100]
print(sum_list(list))
```

# 6.  Correct the following code:
```
def reverse(text):
    result = ""
    text_length = len(text)
    for i in range(text_length):
        result = result + text[i * -1]
    return result
 
text = "Programming is the coolest thing ever."
print(reverse(text))
```
- Correct: 
```
def reverse(text):
    result = ""
    text_length = len(text)
    for i in range(text_length):
        result = result + text[text_length -1 -i]
    return result
 
text = "Programming is the coolest thing ever."
print(reverse(text))
```

# 7.  Correct the following code:
```
def get_user_choice():
    while True:
        command = input("Command: ")
        if command = f or command = m or command = s or command = d or command = q:
            return command
 
        print("Hey, that's not a command. Here are your options:" )
        print("f - Full speed ahead")
        print("m - Moderate speed")
        print("s - Status")
        print("d - Drink")
        print("q - Quit")
 
user_command = get_user_choice()
print("You entered:", user_command)
```
- Correct:
```
def get_user_choice():
    while True:
        command = input("Command: ")
        if command == "f" or command == "m" or command == "s" or command == "d" or command == "q":
            return command
 
        print("Hey, that's not a command. Here are your options:" )
        print("f - Full speed ahead")
        print("m - Moderate speed")
        print("s - Status")
        print("d - Drink")
        print("q - Quit")
 
user_command = get_user_choice()
print("You entered:", user_command)
```

# Write Code
# 1. Write a function that prints out ``Hello World.''
```
def hello_world():
    print("Hello World")
```
# 2. Write code that will call the function in the prior problem.
```
hello_world()
```
# 3. Write a function that prints out ``Hello Bob'', and will take a parameter to let the caller specify the name. Do not put an input statement inside the function! Use a parameter.
```
def print_name(x):
    print("Hello", x)
```
# 4. Write code that will call the function in the prior problem.
```
print_name("Bob")
```
# 5. Write a function that will take two numbers as parameters (not as input from the user) and print their product (i.e. multiply them).
```
def product(x,y):
    print (x * y)
```
# 6. Write code that will call the prior function.
```
product(3,8)
```
# 7. Write a function that takes in two parameters. The first parameter will be a string named phrase. The second parameter will be a number named count. Print phrase to the screen count times. (e.g., the function takes in "Hello" and 5, then prints "Hello" five times.)
```
def copy(phrase,count):
    for i in range(count):
        print (phrase)
```
# 8. Write code that will call the prior function.
```
copy("Hallo",4)
```
# 9. Write code for a function that takes in a number, and returns the square of that number. (I'm not asking for the square root, but the number squared.) Note, this function should RETURN the answer, not print it out.
```
def square(x):
    return x*x
```
# 10. Write code to call the function above and print the output.
```
print(square(3))
```
# 11. Write a function that takes three numbers as parameters, and returns the centrifugal force.
```
def centrifugal(mass,radius,velocity):
    return (mass*(velocity**2/radius))
```
# 12. Write code to call the function above and display the result.
```
print(centrifugal(3,4,5))
```
# 13. Write a function that takes a list of numbers as a parameter, and prints out each number individually using a for loop.
```
def print_list(list):
    for i in range(len(list)):
        print(list[i])
```
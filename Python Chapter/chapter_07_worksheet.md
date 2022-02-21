# 1. List the four types of data we've covered, and give an example of each:
```
type(3)
type(3.145)
type("Hi there")
type(True)
```

# 2. What does this code print out? For this and the following problems, make sure you understand WHY it prints what it does. You don't have to explain it, but if you don't understand why, make sure to ask. Otherwise you are wasting your time doing these.
- PrintOut: 2 101 Error, because [5] is out of range and lists starts at 0
- Fix (index - 1):
```
my_list = [5, 2, 6, 8, 101]
print(my_list[0])
print(my_list[3])
print(my_list[4])
```
- PrintOut: 5 8 101 (vertical)

# 3. What does this code print out?
```
my_list=[5, 2, 6, 8, 101]
for my_item in my_list:
    print(my_item)
```
- Guess: 5 2 6 8 101
- Result: 5 2 6 8 101

# 4. What does this code print out?
```
my_list1 = [5, 2, 6, 8, 101]
my_list2 = (5, 2, 6, 8, 101)
my_list1[3] = 10
print(my_list1)
my_list2[2] = 10
print(my_list2)
```
- Guess: 5 2 6 10 101 5 2 6 8 101
- Result: [5, 2, 6, 10, 101] Error
- my_list2 is a tuple and can't be modified by "my_list2[2] = 10"

# 5. What does this code print out?
```
my_list = [3 * 5]
print(my_list)
my_list = [3] * 5
print(my_list)
```
- Guess: [15] [3, 3, 3, 3, 3]
- Result: [15] [3, 3, 3, 3, 3]

# 6. What does this code print out?
```
my_list = [5]
for i in range(5):
    my_list.append(i)
print(my_list)
```
- Guess: [5, 1, 2, 3, 4]
- Result: [5, 0, 1, 2, 3, 4] (lists starts at 0)

# 7. What does this code print out?
```
print(len("Hi"))
print(len("Hi there."))
print(len("Hi") + len("there."))
print(len("2"))
print(len(2))
```
- Guess: 2 9 8 1 2 (vertical)
- Result: 2 9 8 1 2 Error (vertical) (int has no len)

# 8. What does this code print out?
```
print("Simpson" + "College")
print("Simpson" + "College"[1])
print( ("Simpson" + "College")[1] 
```
- Guess: SimpsonCollege SimpsonC i (vertical)
- Result: SimpsonCollege SimpsonC i (vertical) 
- Why? number at the end is the index of the letter

# 9. What does this code print out?
```
word = "Simpson"
for letter in word:
    print(letter)
```
- Guess: S i m p s o n (vertical)
- Result: S i m p s o n (vertical)

# 10. What does this code print out?
```
word = "Simpson"
for i in range(3):
    word += "College"
print(word)
```
- Guess: SimpsonCollegeCollegeCollege
- Result: SimpsonCollegeCollegeCollege

# 11. What does this code print out?
```
word = "Hi" * 3
print(word)
```
- Guess: HiHiHi
- Result: HiHiHi

# 12. What does this code print out?
```
my_text = "The quick brown fox jumped over the lazy dogs."
print("The 3rd spot is: " + my_text[3])
print("The -1 spot is: " + my_text[-1])
```
- Guess: The 3rd spot is: (space) The -1 spot is: . 
- Result: The 3rd spot is: (space) The -1 spot is: . 

# 13. What does this code print out?
```
s = "0123456789"
print(s[1])
print(s[:3])
print(s[3:]
```
- Guess: 1 3456789 012345 (verical)
- Result: 1 3456789 012345 (verical)

# 14. Write a loop that will take in a list of five numbers from the user, adding each to an array. Then print the array. Try doing this without looking at the book.
```
my_list = []
for i in range(5):
    user_input = int(input("Input: " ))
    my_list.append(user_input)
print (my_list)
```

# 15. Write a program that take an array like the following, and print the average. Use the len function, don't just use 15, because that won't work if the list size changes. (There is a sum function I haven't told you about. Don't use that. Sum the numbers individually as shown in the chapter.) (Also, a common mistake is to calculate the average each time through the loop to add the numbers. Finish adding the numbers before you divide.)
```
my_list = [3,12,3,5,3,4,6,8,5,3,5,6,3,2,4]
sum = 0
for i in range(len(my_list)):
    sum = sum + my_list[i]
average = sum / len(my_list)
print("The average of the list is:",average)
```
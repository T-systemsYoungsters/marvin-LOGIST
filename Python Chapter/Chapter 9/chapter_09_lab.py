# 1. 
def min3(x,y,z):
    if x <= y and x <= z:
        return x
    elif y <= z and y <= x:
        return y
    elif z <= x and z <= y:
        return z
    else:
        print("There is a mistake")

print(min3(4, 7, 5))
print(min3(4, 5, 5))
print(min3(4, 4, 4))
print(min3(-2, -6, -100))
print(min3("Z", "B", "A"))

# 2.
def box(x,y):
    for i in range(x):
        for j in range(y):
            print("*",end=" ")
        print()

box(7,5)  # Print a box 7 high, 5 across
print()   # Blank line
box(3,2)  # Print a box 3 high, 2 across
print()   # Blank line
box(3,10) # Print a box 3 high, 10 across

# 3. 
def find(x,y):
    for i in range(len(x)):
        if x[i] == y:
            print (f"Found {y} at position {i}")

my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]
find(my_list, 12)
find(my_list, 91)
find(my_list, 80)

# 4.1
import random
def create_list(length):
    my_list = []
    for i in range(length):
        my_list.append(random.randrange(1,7))
    return my_list

#my_list = create_list(5)
#print (my_list)

# 4.2
def count_list(list,x):
    count = 0
    for i in range(len(list)):
        if list[i] == x:
            count += 1
    return count

#count = count_list([1,2,3,3,3,4,2,1],3)
#print(count)

# 4.3
def average_list(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    return (sum / len(list))

#avg = average_list([1,2,3])
#print(avg)

# 4.4
def main(length):
    new_list = create_list(length)
    for i in range(1,7):
        count = count_list(new_list, i)
        print(count)
    print(average_list(new_list))

main(10000)
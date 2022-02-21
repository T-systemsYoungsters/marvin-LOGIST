#6.2 Advanced Looping Problems
#1.
for x in range(10):
    print("*",end=" ")

#2.
for x in range(10):
    print("*",end=" ")
print()
for x in range(5):
    print("*",end=" ")
print()
for x in range(20):
    print("*",end=" ")

#3.
for x in range(10):
    for y in range(10):
        print("*",end=" ")
    print()

#4.
for x in range(10):
    for y in range(5):
        print("*",end=" ")
    print()

#5.
for x in range(5):
    for y in range(20):
        print("*",end=" ")
    print()

#6.
for i in range(10):
    for j in range(10):
        print(j,end=" ")
    print()

#7.
for i in range(10):
    for j in range(10):
        print(i,end=" ")
    print()

#8.
x = 0
for i in range(10):
    x = x + 1
    for j in range(x):
        print(j,end=" ")
    print()

#8. (Beispiellösung)
for i in range(10):
    for j in range(i+1):
        print (j,end=" ")
    print()

#9.
x = 11
for i in range(10):
    for j in range(i):
        print (" ",end=" ")
    x = x - 1
    for j in range(x):
        print(j,end=" ")
    print()

#9. Beispiellösung
for i in range(10):
    for j in range(i):
        print (" ",end=" ")
    for j in range(10-i):
        print (j,end=" ")
    print()

#10.
for i in range(1,10):
    for j in range(1,10):
        if i*j < 10:
            print (" ",end="")
        print (i*j,end=" " )
    print()

#11.
for i in range(10):
    # Print leading spaces
    for j in range(10-i):
        print (" ",end=" ")
    # Count up
    for j in range(1,i+1):
        print (j,end=" ")
    # Count down
    for j in range(i-1,0,-1):
        print (j,end=" ")
    # Next row
    print()

# 12.
for i in range(10):
    # Print leading spaces
    for j in range(10-i):
        print (" ",end=" ")
    # Count up
    for j in range(1,i+1):
        print (j,end=" ")
    # Count down
    for j in range(i-1,0,-1):
        print (j,end=" ")
    # Next row
    print()
for i in range(1,10):
    for j in range(i+1):
        print (" ",end=" ")
    for j in range(9-i):
        print (j+1,end=" ")
    print()

# 12. Beispiellösung
for i in range(10):
    # Print leading spaces
    for j in range(10-i):
        print (" ",end=" ")
    # Count up
    for j in range(1,i+1):
        print (j,end=" ")
    # Count down
    for j in range(i-1,0,-1):
        print (j,end=" ")
    # Next row
    print()
 
for i in range(10):
    # Print leading spaces
    for j in range(i+2):
        print (" ",end=" ")
    # Count down
    for j in range(1,9-i):
        print (j,end=" ")
    # Next row
    print()
    
# 13. Beispiellösung
for i in range(10):
    # Print leading spaces
    for j in range(10-i):
        print (" ",end=" ")
    # Count up
    for j in range(1,i+1):
        print (j,end=" ")
    # Count down
    for j in range(i-1,0,-1):
        print (j,end=" ")
    # Next row
    print()
for i in range(10):
    # Print leading spaces
    for j in range(i+2):
        print (" ",end=" ")
    # Count up
    for j in range(1,9-i):
        print (j,end=" ")
    # Count down
    for j in range(7-i,0,-1):
        print (j,end=" ")
    print()
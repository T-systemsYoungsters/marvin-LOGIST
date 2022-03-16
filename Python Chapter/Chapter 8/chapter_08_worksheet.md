# 1. Why does using this code in the main loop not work to move the rectangle?
```
rect_x = 50
pygame.draw.rect(screen, WHITE, [rect_x, 50, 50, 50])
rect_x += 1
```

# 2. The example code to bounce a rectangle used a total of four variables. What did each variable represent?

# 3. If the screen is 400 pixels tall, and the shape is 20 pixels high, at what point should the code check to see if the shape is in contact with the bottom of the screen.

# 4. Explain what is wrong with the following code (explain it, don't just correct the code):
```
if rect_y > 450 or rect_y < 0:
    rect_y = rect_y * -1
```

# 5. A student is animating a stick figure. He creates separate variables for tracking the position of the head, torso, legs, and arms. When the figure moves to the right he adds one to each of the variables. Explain an easier way to do this that only requires one pair of x, y variables. (And no, the answer has nothing to do with a list.)

# 6. When drawing a starry background, explain why it doesn't work to put code like this in the main program loop:
```
for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    pygame.draw.circle(screen, WHITE, [x, y], 2)
```

# 7. Explain how to animate dozens of items at the same time:

# 8. If you have a list of coordinates like the following, what code would be required to print out the array location that holds the number 33?
```
stars = [[ 3,  4],
         [33, 94],
         [ 0,  0]]
```

# 9. This code example causes snow to fall:
```
# Process each snow flake in the list
for i in range(len(snow_list)):
 
    # Get the x and y from the list
    x = snow_list[i][0]
    y = snow_list[i][1]
 
    # Draw the snow flake
    pygame.draw.circle(screen, WHITE, [x, y], 2)
 
    # Move the snow flake down one pixel
    snow_list[i][1] += 1
```
So does the example below. Explain why this example works as well.
```
# Process each snow flake in the list
for i in range(len(snow_list)):
 
    # Draw the snow flake
    pygame.draw.circle(screen, WHITE, snow_list[i], 2)
 
    # Move the snow flake down one pixel
    snow_list[i][1] += 1
```

# 10. Take a look at the radar_sweep.py program. You can find this example under the ``graphics examples'' subsection on the examples page. The radar_sweep.py is near the end of that list. Explain how this program animates the sweep to go in a circle.
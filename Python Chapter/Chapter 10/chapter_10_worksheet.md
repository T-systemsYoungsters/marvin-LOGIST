# 1. What's wrong with this code that uses a function to draw a stick figure? Assume the colors are already defined and the rest of the program is ok. What is wrong with the code in the function?
```
def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [96,83,10,10], 0)
 
    # Legs
    pygame.draw.line(screen, BLACK, [100,100], [105,110],2)
    pygame.draw.line(screen, BLACK, [100,100], [95,110],2)
 
    # Body
    pygame.draw.line(screen, RED, [100,100], [100,90], 2)
 
    # Arms
    pygame.draw.line(screen, RED, [100,90], [104,100], 2)
    pygame.draw.line(screen, RED, [100,90], [96,100], 2)
```
- the x and y coordinate are irrelevant, because the figure will be draw at the same location every time

# 2. Show how to grab the mouse coordinates, and then grab just the x coordinate of where the mouse is.
```
pos = pygame.mouse.get_pos()

# just the x coordinate

pos = pygame.mouse.get_pos()
x = pos[0]
```

# 3. Why is it important to keep the event processing loop "together" and only have one of them? It is more than organization, there will be subtle hard-to-detect errors. What are they and why will they happen without the event processing loop together? (Review "The Event Processing Loop" in Chapter 5 if needed.)
```
the program will only use the first main loop and ignore the others. so all inputs after the first loop are irrelevant
```
# 4. When we created a bouncing rectangle, we multiplied the speed times -1 when the rectangle hit the edge of the screen. Explain why that technique won't work for moving an object with the keyboard.
```
because if you want to move left, your press the left arrow key. if you multiply the value with -1, the left arrow key will be move to the right. the control is inverted
```
# 5. Why does movement with the keyboard or game controller need to have a starting x, y location, but the mouse doesn't?
```
keyboards and game controller are given you vector inputs 
mouse is given you coordinates for the current mouse position
```
# 6. What values will a game controller return if it is held all the way down and to the right?
```
(1,1)
```
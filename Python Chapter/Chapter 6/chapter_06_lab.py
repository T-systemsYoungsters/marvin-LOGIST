'''
#1
x = 9
for i in range(9):
    for j in range(i+1):
        x += 1
        print (x,end=" ")
    print()

#2.
user_input = int(input("Eingabe: "))
for x in range(user_input*2):
    print("°",end="")
print()
for x in range(user_input-2):
    for y in range(1):
        print("°",end="")
    for y in range(user_input*2-2):
        print(" ",end="")
    for y in range(1):
        print("°",end="")
    print()
for x in range(user_input*2):
    print("°",end="")
    '''
#4.
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    x_rect_origin = 10
    y_rect_origin = 10
    for i in range(10):
        for j in range(10):
            pygame.draw.rect(screen, GREEN, pygame.Rect(x_rect_origin, y_rect_origin, 20, 20))
            x_rect_origin = x_rect_origin + (j + 30)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
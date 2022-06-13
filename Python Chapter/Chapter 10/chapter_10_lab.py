# 1. Create at least two different functions that draw an object to the screen. 
# For example, draw_bird and draw_tree. Do not draw a stick figure, we did that one already.
# Create your own unique item. Do not simply draw a circle or rectangle. That's boring. 
# Draw a train, or cloud, or house, T-Rex or whatever. But minimal work = minimal points. 
# If you created your own object in the create-a-picture lab feel free to adapt it to this lab.
"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREY = (210, 210, 210)
GREEN = (102, 205, 0)
DIMGRAY = (105, 105, 105)
BROWN = (100, 40, 0)
SKYBLUE = (0, 191, 255)
YELLOW = (255, 255, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Marvin's bewegte Lok")

def draw_train(screen,x,y):
    # Chassi
    pygame.draw.rect(screen, RED, [490 + x, 350 + y, 125, 30])
    # Chimney
    pygame.draw.rect(screen, RED, [500 + x, 320 + y, 20, 50])
    # Cabin
    pygame.draw.rect(screen, RED, [600 + x, 300 + y, 50, 80])
    # Window
    pygame.draw.rect(screen, BLUE, [610 + x, 310 + y, 30, 30])
    # Wheels
    wheels_rad = 20
    x_wheels_origin = 500 + x
    y_wheels_origin = 400 + y
    for i in range(4):
        # Wheels
        pygame.draw.circle(screen, BLACK, (x_wheels_origin, y_wheels_origin), wheels_rad)
        x_wheels_origin = x_wheels_origin + 45
    
def draw_rectangle(screen,x,y):
    pygame.draw.rect(screen, YELLOW, [100 + x, 100 + y, 100, 100])

# Speed in pixels per frame
x_speed = 0
y_speed = 0
 
# Current position
x_coord = 10
y_coord = 10
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
        # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
    
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
    

    # Move the object according to the speed vector.
    if x_coord < -100:
        x_coord = -100
    if x_coord > 500:
        x_coord = 500
    if y_coord < -100:
        y_coord = -100
    if y_coord > 300:
        y_coord = 300

    x_coord += x_speed
    y_coord += y_speed



    # --- Game logic should go here
    pos = pygame.mouse.get_pos()
    x = pos[0] - (490 + 125/2)
    y = pos[1] - (350 + 30/2)

    # Hide the mouse cursor
    pygame.mouse.set_visible(False)

    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    draw_train(screen,x,y)
    draw_rectangle(screen, x_coord, y_coord)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
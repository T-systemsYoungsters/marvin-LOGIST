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
 
pygame.display.set_caption("6.4 Part 4")
 
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
    #Anfangskoordinaten
    x_rect_origin = 10
    y_rect_origin = 10
    
    for i in range(33): #Zeilen
        for j in range(46): #Spalten
            pygame.draw.rect(screen, GREEN, pygame.Rect(x_rect_origin, y_rect_origin, 10, 10)) #zeichnen des Rechtecks
            x_rect_origin = x_rect_origin + 15 #erhöhen der x Koordinate um 15 nach jedem Rechteck
        x_rect_origin = 10 #zurücksetzen der X Koordinate um die nächste Zeile wieder bei x=10 zu starten
        y_rect_origin = y_rect_origin + 15 ##erhöhen der y Koordinate/Zeilenabstand um 15 nach jeder Zeile
        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
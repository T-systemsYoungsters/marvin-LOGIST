import pygame
pygame.init()
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
 
PI = 3.141592653

screen_size = (500, 400)
screen = pygame.display.set_mode(screen_size)

done = False
clock = pygame.time.Clock()
 
pygame.display.set_caption("Marvin's Lok")
 
while not done:
 
    # Checking for pressing close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # Clear screen
    screen.fill(WHITE)

    # DRAWING
    # Chassi
    pygame.draw.rect(screen, RED, pygame.Rect(190, 250, 125, 30))

    # Cabin
    pygame.draw.rect(screen, RED, pygame.Rect(300, 200, 50, 80))
    #pygame.draw.polygon(screen, RED, [[60, 0], [25, 30], [95, 30]])

    # Window
    pygame.draw.rect(screen, BLUE, pygame.Rect(310, 210, 30, 30))

    # Wheels
    wheels_rad = 20
    x_wheels_origin = 200
    y_wheels_origin = 300

    for i in range(4):
        # Wheels
        pygame.draw.circle(screen, BLACK, (x_wheels_origin, y_wheels_origin), wheels_rad)

        x_wheels_origin = x_wheels_origin + (i + 45)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
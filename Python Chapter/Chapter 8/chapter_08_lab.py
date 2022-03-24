import pygame
import random
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

PI = 3.141592653

smoke_list = []

screen_size = (700, 500)
screen = pygame.display.set_mode(screen_size)

done = False
clock = pygame.time.Clock()
 
pygame.display.set_caption("Marvin's Lok")
 
chassi_x = 490
cabin_x = 600
chimney_x = 500
window_x = 610
wheels_x = 500

smoke1_x = 500
smoke2_x = 540
smoke3_x = 520
smoke4_x = 550

chassi_y = 350
cabin_y = 300
chimney_y = 320
window_y = 310
wheels_y = 400

smoke1_y = 300
smoke2_y = 300
smoke3_y= 270
smoke4_y = 270


change_x = 1

counter = 0

while not done:
 
    # Checking for pressing close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # Clear screen
    screen.fill(WHITE)

    # DRAWING    
    # Gras
    pygame.draw.rect(screen, GREEN, [0, 280 , 700, 350])

    # Sky
    pygame.draw.rect(screen, SKYBLUE, [0, 0 , 700, 280])

    # Sun
    pygame.draw.circle(screen, YELLOW,(20,0), 80)
    pygame.draw.line(screen, YELLOW, [50, 50], [100, 120], 4)
    pygame.draw.line(screen, YELLOW, [30, 60], [50, 120], 4)
    pygame.draw.line(screen, YELLOW, [80, 40], [200, 120], 4)

    # Rail Underground
    pygame.draw.rect(screen, BROWN, [0, 410 , 700, 10])

    # Rail
    pygame.draw.rect(screen, DIMGRAY, [0, 400 , 700, 10])
    pygame.draw.rect(screen, DIMGRAY, [0, 420 , 700, 10])
    rail_parts_x = 10
    for i in range (23):
        pygame.draw.rect(screen, DIMGRAY, [rail_parts_x, 395 , 10, 40])
        rail_parts_x = rail_parts_x + 30

    # Smoke
    for i in smoke_list: 
        pygame.draw.circle(screen,GREY, (i[0], smoke1_y), 30)
        pygame.draw.circle(screen,GREY, (i[1], smoke2_y), 30)
        pygame.draw.circle(screen,GREY, (i[2], smoke3_y), 30)
        pygame.draw.circle(screen,GREY, (i[3], smoke4_y), 30)

    if counter == 80:
        smoke_list.append([smoke1_x, smoke2_x, smoke3_x, smoke4_x])
        counter = 0
    counter += 1

    # Chassi
    pygame.draw.rect(screen, RED, [chassi_x, chassi_y, 125, 30])

    # Chimney
    pygame.draw.rect(screen, RED, [chimney_x, chimney_y, 20, 50])

    # Cabin
    pygame.draw.rect(screen, RED, [cabin_x, cabin_y, 50, 80])

    # Window
    pygame.draw.rect(screen, BLUE, [window_x, window_y, 30, 30])

    # Wheels
    wheels_rad = 20
    x_wheels_origin = wheels_x
    y_wheels_origin = wheels_y

    for i in range(4):
        # Wheels
        pygame.draw.circle(screen, BLACK, (x_wheels_origin, y_wheels_origin), wheels_rad)
        x_wheels_origin = x_wheels_origin + 45

    chassi_x -= change_x
    cabin_x -= change_x
    chimney_x -= change_x
    window_x -= change_x
    wheels_x -= change_x
    smoke1_x -= change_x
    smoke2_x -= change_x
    smoke3_x -= change_x
    smoke4_x -= change_x

    # STOP
    if cabin_x < -100:
        done = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()